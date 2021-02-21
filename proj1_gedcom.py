#Author: Zack Edwards
print('Please enter the path file for your GEDCOM file (.ged)')
#This is the local path file for my gedcom file
#path = r'C:\Users\Zack Edwards\Documents\trackwithease\ZackEdwardsFamilyTree.ged'
path = input("")
#open the file
file = open(path, 'r')
output = open('ged_output.txt', 'w')
#loop through each line in the file
for line in file:
    print('--> %s' %line[:-1])#the [:-1] removed a 'skip line' from the end of each line of the gedcom file 
    output.write('--> %s \n' %line[:-1])#writing to the output file
    words = line.split() #create an array of the words
    if 'INDI' in words[-1] or 'FAM' in words[-1]: #filter for special case
        words[-1],words[-2] = words[-2],words[-1] #swap the place of the tag
        words.insert(2,'Y') #insert 'Y' for valid tag
        out = '<-- ' + "|".join(words)
        print(out) #print the output
        output.write(out + '\n')
        continue
    tags = ['INDI', 'NAME', 'SEX','BIRT','DEAT','FAMC','FAMS','FAM','MARR','HUSB','WIFE',
            'CHILL','DIV','DATE','HEAD','TRLR','NOTE']#create a list of acceptable tags
    #filter for those tags
    if any(x in words for x in tags):
        words.insert(2,'Y') #insert 'Y' for valid tag
        out = '<-- ' + "|".join(words)
        print(out) #print the output
        output.write(out + '\n')
        continue
    else:
        words.insert(2,'N') #insert 'N' if it is not a valid tag
        out = '<-- ' + "|".join(words)
        print(out)
        output.write(out + '\n')
file.close()
output.close()