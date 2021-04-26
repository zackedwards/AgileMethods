import pandas as pd
import sys
sys.path.insert(0, '../AgileMethods/TestCaseFiles')

from US25test import unique_child_name_and_birth #Takes in individualsDF & famRow
from US26test import consistent_individuals_and_families #Takes in familiesDF & individualsDF
from US27test import include_age_check #Takes in individualsDF

from US28test import sibling_age_check #Takes in familiesDF and individualsDF
from US29test import listDeceased #Takes in individualsDF
from US30test import listLivingAndMarried #Takes in familiesDF & individualsDF

from US31test import ListLivingSingle #Takes in individualsDF
from US32test import ListMultipleBirths #Takes in familiesDF

individuals = pd.read_csv('./Data/individuals4.csv')
families = pd.read_csv('./Data/families4.csv')
errors = []

for index, famRow in families.iterrows():
   errors += unique_child_name_and_birth(individuals, famRow) 

errors += consistent_individuals_and_families(individuals, families)
errors += include_age_check(individuals)
errors += sibling_age_check(families, individuals)
errors += listDeceased(individuals)
errors += listLivingAndMarried(families, individuals)
errors += ListLivingSingle(individuals)
errors += ListMultipleBirths(families)

TestResults = open("sprint4TestResults.txt", "w")
terminalOutput = ""
terminalOutput += "People" + individuals.to_string() + "\n\nFamilies" + families.to_string() + "\n\n"
for error in errors:
    terminalOutput += error + "\n"

TestResults.write(terminalOutput)
print(terminalOutput)
