import pandas as pd
import sys
sys.path.insert(0, '../AgileMethods/TestCaseFiles')

from US09test import get_parents_death #Takes in individualsDF & familiesDF
from US10test import marriage_after_fourteen #Takes in individualsDF & famRow
from US11test import NoBigamy #Takes in a family
from US12test import ParentsTooOld
from US13test import siblings_spacing
from US14test import no_more_than_5_kids_check #Takes in individualsDF & familiesDF
from US15test import LessThan15Siblings #Takes in familiesDF
from US16test import MaleLastNames #Takes in a famRow & individualsDF

individuals = pd.read_csv('./Data/individuals.csv')
families = pd.read_csv('./Data/families.csv')

errors = []

for index, famRow in families.iterrows():
    errors += get_parents_death(individuals, famRow)
    errors += MaleLastNames(famRow, individuals)

errors += marriage_after_fourteen(individuals, families)
errors += NoBigamy(families)
errors += ParentsTooOld(individuals, families)
errors += siblings_spacing(individuals, families)
errors += no_more_than_5_kids_check(individuals, families)
errors += LessThan15Siblings(families)

TestResults = open("sprint2TestResults.txt", "w")
terminalOutput = ""
terminalOutput += "People" + individuals.to_string() + "\n\nFamilies" + families.to_string() + "\n\n"
for error in errors:
    terminalOutput += error + "\n"

TestResults.write(terminalOutput)
print(terminalOutput)
