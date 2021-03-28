import pandas as pd
import sys
sys.path.insert(0, '../AgileMethods/TestCaseFiles')

from US09test import get_parents_death #Takes in individualsDF & familiesDF
from US10test import marriage_after_fourteen #Takes in individualsDF & famRow
#from US11test import NoBigamy #Takes in a indiRow
#from US12test import  
#from US13test import  
from US14test import no_more_than_5_kids_check #Takes in individualsDF & familiesDF
#from US15test import  
from US16test import MaleLastNames #Takes in a famRow & individualsDF

individuals = pd.read_csv('./Data/individuals.csv')
families = pd.read_csv('./Data/families.csv')

errors = marriage_after_fourteen(individuals, families)
errors += no_more_than_5_kids_check(individuals, families)

for index, indiRow in individuals.iterrows():
    #errors += NoBigamy(indiRow)
    break

for index, famRow in families.iterrows():
    errors += MaleLastNames(famRow, individuals)
    errors = get_parents_death(individuals, famRow)

TestResults = open("sprint2TestResults.txt", "w")
terminalOutput = ""
terminalOutput += "People" + individuals.to_string() + "\n\nFamilies" + families.to_string() + "\n\n"
for error in errors:
    terminalOutput += error + "\n"

TestResults.write(terminalOutput)
print(terminalOutput)
