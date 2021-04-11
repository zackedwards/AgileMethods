import pandas as pd
import sys
sys.path.insert(0, '../AgileMethods/TestCaseFiles')

from US17test import parents_marry_children #Takes in familiesDF & famRow
from US18test import siblings_married_check #Takes in familiesDF & famRow
from US19test import  #Takes in a family
from US20test import 
from US21test import 
from US22test import  #Takes in individualsDF & familiesDF
from US23test import  UniqueNameAndBirth #Takes in indiRow
from US24test import  UniqueSpousesAndMarriage #Takes in indiRow

individuals = pd.read_csv('./Data/individuals.csv')
families = pd.read_csv('./Data/families.csv')

errors = []

for index, famRow in families.iterrows():
    errors += parents_marry_children(families, famRow)
    errors += siblings_married_check(individuals, famRow)


for index, indiRow in individuals.iterrows():
    errors += get_parents_death(families, famRow)



TestResults = open("sprint3TestResults.txt", "w")
terminalOutput = ""
terminalOutput += "People" + individuals.to_string() + "\n\nFamilies" + families.to_string() + "\n\n"
for error in errors:
    terminalOutput += error + "\n"

TestResults.write(terminalOutput)
print(terminalOutput)
