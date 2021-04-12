import pandas as pd
import sys
sys.path.insert(0, '../AgileMethods/TestCaseFiles')

from US17test import parents_marry_children_check #Takes in familiesDF & famRow
from US18test import siblings_married_check #Takes in familiesDF & famRow
from US19test import cousins_married_check #Takes in familiesDF & famRow
from US20test import aunt_uncle_married_check #Takes in familiesDF & famRow
from US21test import correct_gender_check #Takes in individualsDF & familiesDF
from US22test import unique_ids_check #Takes in individualsDF & familiesDF
from US23test import UniqueNameAndBirth #Takes in indiDF
from US24test import UniqueSpousesAndMarriage #Takes in famDF

individuals = pd.read_csv('./Data/individuals3.csv')
families = pd.read_csv('./Data/families3.csv')

errors = []

for index, famRow in families.iterrows():
    errors += parents_marry_children_check(families, famRow)
    errors += siblings_married_check(families, famRow)
    errors += cousins_married_check(families, famRow)
    errors += aunt_uncle_married_check(families, famRow)

errors += correct_gender_check(individuals, families)
errors += unique_ids_check(individuals, families)
errors += UniqueNameAndBirth(individuals)
errors += UniqueSpousesAndMarriage(families)

# for index, indiRow in individuals.iterrows():
#     errors += get_parents_death(families, famRow) #not in this sprint?



TestResults = open("sprint3TestResults.txt", "w")
terminalOutput = ""
terminalOutput += "People" + individuals.to_string() + "\n\nFamilies" + families.to_string() + "\n\n"
for error in errors:
    terminalOutput += error + "\n"

TestResults.write(terminalOutput)
print(terminalOutput)
