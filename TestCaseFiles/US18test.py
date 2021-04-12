'''
Created on March 29th, 2021

@author: Valentina Bustamante

Descripion: Creates error if siblings are married)
'''
import unittest
import pandas as pd
from ast import literal_eval

# Checks if husband id and wife id from a family are both in the children list of another family 
def siblings_married_check(families, row_fam_children):
    errors = []
    if isinstance(row_fam_children["Children"], str):
        children = literal_eval(row_fam_children["Children"])
        if not isinstance(children ,float):
            for index, row_fam in families.iterrows():
                if isinstance(row_fam["Wife ID"],str) and isinstance(row_fam["Husband ID"],str):
                    if row_fam["Husband ID"] in children and row_fam["Wife ID"] in children:
                        errors.append("ERROR: FAMILY: US18: {}: Spouses {} and {} are siblings in family {}".format(row_fam["ID"], row_fam["Wife ID"], row_fam["Husband ID"], row_fam_children["ID"]))
                        children.remove(row_fam["Wife ID"])
                        children.remove(row_fam["Husband ID"])

    return errors

class Test(unittest.TestCase):
    
    def test_siblings_married(self):
        file = pd.read_csv('../Data/families.csv')
        errors = []
        for index, row_fam in file.iterrows():
            errors += (siblings_married_check(pd.read_csv('../Data/families.csv'), row_fam))
        self.assertEqual(errors, ['ERROR: FAMILY: US18: F1: Spouses I3 and I2 are siblings in family F10'])

if __name__ == "__main__":
    unittest.main()