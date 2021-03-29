'''
Created on March 29th, 2021

@author: Valentina Bustamante

Descripion: Creates an error if parents marry descendants)
'''
import unittest
import pandas as pd
import sys
sys.path.insert(0, '../AgileMethods')

from functions import convertStringToDatetime

# Checks if husband id and wife id from a family are both in the children list of another family 
def parents_marry_children_check(families, row_fam):
    children = row_fam["Children"]
    mother = row_fam["Wife ID"]
    father = row_fam["Husband ID"]
    errors = []

    if not isinstance(children ,float):
        for index, row_fam2 in families.iterrows():
            if isinstance(row_fam2["Wife ID"],str) and isinstance(row_fam2["Husband ID"],str):
                if mother == row_fam2["Wife ID"] and row_fam2["Husband ID"] in children:
                    errors.append("ERROR: FAMILY: US18: {}: Spouse {} is the mother of {} in family {} and are married".format(row_fam2["ID"], mother, row_fam2["Husband ID"], row_fam["ID"]))
                elif father == row_fam2["Husband ID"] and row_fam2["Wife ID"] in children:
                    errors.append("ERROR: FAMILY: US18: {}: Spouse {} is the father of {} in family {} and are married".format(row_fam2["ID"], father, row_fam2["Wife ID"], row_fam["ID"]))
        return errors
    else: 
        return []

class Test(unittest.TestCase):
    
    def test_parents_marry_children_check(self):
        file = pd.read_csv('../Data/families.csv')
        errors = []
        for index, row_fam in file.iterrows():
            errors += (parents_marry_children_check(pd.read_csv('../Data/families.csv'), row_fam))
        self.assertEqual(errors, [])

if __name__ == "__main__":
    unittest.main()