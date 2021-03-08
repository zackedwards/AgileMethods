import pandas as pd
import sys
sys.path.insert(0, '../AgileMethods/TestCaseFiles')

from US01test import birth_before_current_check #Takes in a indiRow
from US02test import birth_before_marriage_check #Takes in individualsDF & familiesDF
from US03test import BirthBeforeDeath #Takes in a indiRow
from US04test import MarriageBeforeDivorce #Takes in a famRow
from US05test import marriage_before_death_check #Takes in a famRow & individualsDF
from US06test import divorce_before_death_check #Takes in a famRow & individualsDF
from US07test import age_less_than_150 #Takes in a indiRow
from US08test import birth_before_parent_marriage #Takes in a famRow & individualsDF

individuals = pd.read_csv('./Data/individuals.csv')
families = pd.read_csv('./Data/families.csv')

errors = birth_before_marriage_check(individuals, families)

for index, indiRow in individuals.iterrows():
    errors += birth_before_current_check(indiRow)
    errors += BirthBeforeDeath(indiRow)
    errors += age_less_than_150(indiRow)

for index, famRow in families.iterrows():
    errors += MarriageBeforeDivorce(famRow)
    errors += marriage_before_death_check(famRow, individuals)
    errors += divorce_before_death_check(famRow, individuals)
    errors += birth_before_parent_marriage(famRow, individuals)

TestResults = open("sprint1TestResults.txt", "w")
terminalOutput = ""
terminalOutput += "People" + individuals.to_string() + "\n\nFamilies" + families.to_string() + "\n\n"
for error in errors:
    terminalOutput += error + "\n"

TestResults.write(terminalOutput)
print(terminalOutput)
