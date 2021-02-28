#Author: Zack Edwards, Valentina Bustamante, William Escamilla, Dana Faustino
import pandas as pd
import datetime

print('Please enter the path file for your GEDCOM file (.ged)')
#This is the local path file for my gedcom file
#path = r'/Users/zackedwards/OneDrive - stevens.edu/Semester 6/555/AgileMethods/FamilyTree.ged'
path = input("")
#open the file
file = open(path, 'r')

#Grab the current date
currDate = datetime.datetime.now()

#create dataframes for the individuals and families
individuals = pd.DataFrame(columns = ['ID','Name','Gender','Birthday','Age','Alive','Death','Child','Spouse'])
families = pd.DataFrame(columns = ['ID','Married','Divorced','Husband ID','Husband Name','Wife ID','Wife Name','Children'])

#Errors list
errors_us01 = []

#define a function which determines the number of a month
def monthNumber(month):
    months = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
    return months.index(month) + 1

#defining variables to be used in the while loop
row = {}
birthFlag = False
deathFlag = False
marrFlag = False
divFlag = False

# keeps track of current line number in GED file
counter = 0

# checks if birth happened before the current date. if not, error message prints
def birth_before_current_check(birth, id, counter):
    birth_datetime = datetime.datetime(int(birth[2]), monthNumber(birth[1]), int(birth[0]))
    if birth_datetime < currDate:
        errors_us01.append("ERROR: INDIVIDUAL: US01: {}: {}: Birthday {} occurs in the future".format(counter, id, birth_datetime.date()))

# checks if birth happened before marriage. if not, error message prints
def birth_before_marriage_check(individuals2, families2):
    errors_us02 = []
    for indi_id, birth in zip(individuals2.index.tolist(), individuals2["Birthday"]):
        for marriage_date, husb_id, wife_id in zip(families2["Married"], families2["Husband ID"], families2["Wife ID"]):
            if indi_id == husb_id or indi_id == wife_id:
                if isinstance(marriage_date, list):
                    birth_dt = datetime.datetime(int(birth[2]), monthNumber(birth[1]), int(birth[0]))
                    marriage_dt = datetime.datetime(int(marriage_date[2]), monthNumber(marriage_date[1]), int(marriage_date[0]))
                    if birth_dt < marriage_dt:
                        errors_us02.append("ERROR: INDIVIDUAL: US02: {}: Married {} before born {}".format(indi_id, marriage_dt.date(), birth_dt.date()))
    return errors_us02

#looping through lines in the gedcom file
for line in file:
    counter = counter + 1
    words = line.split() #create an array of the words
    if 'INDI' in words[-1]: #filter for individuals
        if row != {}: #this filters for the base case where no data is in row yet
            #this if statement summarizes age info and appends the row to the dataframe
            if 'Death' in row.keys(): 
                #calculating age if dead
                yearDiff = int(row['Death'][-1]) - int(row['Birthday'][-1])
                monthDiff = int(monthNumber(row['Death'][-2])) - int(monthNumber(row['Birthday'][-2]))
                dayDiff = int(row['Death'][-3]) - int(row['Birthday'][-3])
                age = yearDiff
                if monthDiff < 0:
                    age -= 1
                elif monthDiff == 0:
                    if dayDiff < 0:
                        age -= 1
                row['Age'] = age
                row['Alive'] = 'False'
            else:
                #calculate age if alive
                yearDiff = int(currDate.year) - int(row['Birthday'][-1])
                monthDiff = currDate.month - int(monthNumber(row['Birthday'][-2]))
                dayDiff = int(currDate.day) - int(row['Birthday'][-3])
                age = yearDiff
                if monthDiff < 0:
                    age -= 1
                elif monthDiff == 0:
                    if dayDiff < 0:
                        age -= 1
                row['Age'] = age
                row['Alive'] = 'True'
            #append info to dataframe
            individuals = individuals.append(row, ignore_index=True)
            row = {} #reset dictionary
        row = {'ID': words[1][1:-1]} #start new row

    elif 'FAM' in words[-1]: #filter for families
        if str(individuals.index[0])[0] != 'I': #insert the last individual in the dataframe
            individuals = individuals.append(row, ignore_index=True)
            row = {} #reset the row
            individuals = individuals.set_index('ID') #set index to ID
        elif row != {}: #if row is not blank
            row["Children"] = str(row['Children']) + '}' #add final child
            families = families.append(row, ignore_index=True)#append row to database
            row = {}
        row = {'ID': words[1][1:-1]}
    #if '1' in words[0] and words[1] != 
    elif row != {}:
        if 'NAME' in words: #filter for name
            row["Name"] = words[2:]
        elif 'SEX' in words: #filter for sex
            row["Gender"] = words[2]
        elif 'BIRT' in words: #filter for birth
            birthFlag = True #an indicator for the next loop 
        elif 'DEAT' in words:
            deathFlag = True
        elif 'MARR' in words:
            marrFlag = True
        elif 'DIV' in words:
            divFlag = True
        elif 'FAMC' in words:
            row['Child'] = words[-1][1:-1]
        elif 'FAMS' in words:
            row['Spouse'] = words[-1][1:-1]
        elif "HUSB" in words:
            row["Husband ID"] = words[-1][1:-1]
            row['Husband Name'] = individuals.loc[row["Husband ID"]]["Name"] #get name using ID
        elif "WIFE" in words:
            row["Wife ID"] = words[-1][1:-1]
            row['Wife Name'] = individuals.loc[row["Wife ID"]]["Name"]
        elif "CHIL" in words:
            if "Children" in row.keys():
                row["Children"] = str(row['Children']) + ', ' + str((words[-1][1:-1])) #mid kid list
            else:
                row["Children"] = '{' + words[-1][1:-1] #start kid list
        elif deathFlag == True: #fulfilling the deathFlag
            row["Death"] = words[2:]
            deathFlag = False
        elif birthFlag == True:
            row["Birthday"] = words[2:]
            birth_before_current_check(row['Birthday'], row['ID'], counter) #US01: birth < current date check
            birthFlag = False
        elif marrFlag == True:
            row["Married"] = words[2:]
            marrFlag = False
        elif divFlag == True:
            row["Divorced"] = words[2:]
            divFlag = False

        
row["Children"] = str(row['Children']) + '}' #add final child for final row of families
families = families.append(row, ignore_index=True)
#print and send to csv
individuals.to_csv('individuals.csv')
families.to_csv('families.csv')
print("\nPeople:\n", individuals.head(10), "\n")
print("Families:\n", families.head(10))
file.close()

# Prints out errors for birth before current day check: US01
for error in errors_us01:
    print(error)

# Prints out errors for birth before marriage check: US02
errors_us02 = birth_before_marriage_check(individuals, families)
for error in errors_us02:
    print(error)



#part 2: print identifiers and names
individuals = individuals.rename(columns={'Name': 'Names'})
print('\nList of individuals with ID and Name')
for index, row in individuals.iterrows():
    print('ID: ' + index + '    Name:', row['Names'])
print()
print('List of families')
for index, row in families.iterrows():
    print('ID:', index, '      Husband:', row['Husband Name'], '     Wife:',row['Wife Name'])