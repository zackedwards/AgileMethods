import pandas as pd
import sys
sys.path.insert(0, '../AgileMethods/TestCaseFiles')

from US25test import unique_child_name_and_birth #Takes in individualsDF & famRow
from US26test import consistent_individuals_and_families #Takes in familiesDF & individualsDF
from US27test import include_age_check #Takes in individualsDF

from US28test import aunt_uncle_married_check #Takes in familiesDF
from US29test import correct_gender_check #Takes in individualsDF & familiesDF
from US30test import unique_ids_check #Takes in individualsDF & familiesDF

from US31test import ListLivingSingle #Takes in individualsDF
from US32test import ListMultipleBirths #Takes in familiesDF

individuals = pd.read_csv('./Data/individuals3.csv')
families = pd.read_csv('./Data/families3.csv')

errors = []
errors += consistent_individuals_and_families(individuals, families)
errors += include_age_check(individuals)
errors += ListLivingSingle(individuals)
errors += ListMultipleBirths(families)

for index, famRow in families.iterrows():
   errors += unique_child_name_and_birth(individuals, famRow) 

TestResults = open("sprint4TestResults.txt", "w")
terminalOutput = ""
terminalOutput += "People" + individuals.to_string() + "\n\nFamilies" + families.to_string() + "\n\n"
for error in errors:
    terminalOutput += error + "\n"

TestResults.write(terminalOutput)
print(terminalOutput)
