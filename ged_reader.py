#Author: Zack Edwards, Valentina Bustamante, William Escamilla, Dana Faustino
from numpy import NaN
import pandas as pd
import datetime
from functions import monthNumber
#print('Please enter the path file for your GEDCOM file (.ged)')
#This is the local path file for my gedcom file
#path = r'FamilyTree.ged'
#path = input("")
#open the file
def main():
    filePath = input("Enter the ged file path to be read: ")
    file = open(filePath, 'r')

    #Grab the current date
    currDate = datetime.datetime.now()

    #create dataframes for the individuals and families
    individuals = pd.DataFrame(columns = ['ID','Name','Gender','Birthday','Age','Alive','Death','Child','Spouse'])
    families = pd.DataFrame(columns = ['ID','Married','Divorced','Husband ID','Husband Name','Wife ID','Wife Name','Children'])

    #defining variables to be used in the while loop
    row = {}
    birthFlag = False
    deathFlag = False
    marrFlag = False
    divFlag = False
    #looping through lines in the gedcom file
    for line in file:
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
                elif 'Birthday' in row.keys():
                    #calculate age if alive
                    #print(row)
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
                row = {}  # reset dictionary
            row = {'ID': words[1][1:-1]}  # start new row
        elif 'FAM' in words[-1]:  # filter for families
            if str(individuals.index[0])[0] != 'I':  # insert the last individual in the dataframe
                individuals = individuals.append(row, ignore_index=True)
                row = {}  # reset the row
                individuals = individuals.set_index('ID')  # set index to ID
            elif row != {}:  # if row is not blank
                if "Children" not in row.keys():
                    row["Children"] = NaN
                families = families.append(row, ignore_index=True)  # append row to database
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
                    row["Children"].append(words[-1][1:-1]) #mid kid list
                else:
                    row['Children'] = []
                    row["Children"].append(words[-1][1:-1]) #start kid list
            elif deathFlag == True: #fulfilling the deathFlag
                row["Death"] = words[2:]
                deathFlag = False
            elif birthFlag == True:
                row["Birthday"] = words[2:]
                birthFlag = False
            elif marrFlag == True:
                row["Married"] = words[2:]
                marrFlag = False
            elif divFlag == True:
                row["Divorced"] = words[2:]
                divFlag = False
    families = families.append(row, ignore_index=True)
    #print and send to csv
    individuals.to_csv('./Data/individuals.csv')
    families.to_csv('./Data/families.csv')
    print(individuals)
    print(families)
    file.close()

#part 2: print identifiers and names
# individuals = individuals.rename(columns={'Name': 'Names'})
# print('List of individuals with ID and Name')
# for index, row in individuals.iterrows():
#     print('ID: ' + index + '    Name:', row['Names'])
# print()
# print('List of families')
# for index, row in families.iterrows():
#     print('ID:', index, '      Husband:', row['Husband Name'], '     Wife:',row['Wife Name'])
main()
print("Done creating csv's")