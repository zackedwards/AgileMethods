'''
Created on Apr 9, 2021

@author: Danielle Faustino
'''
import unittest
import pandas as pd
import sys
sys.path.insert(0, '../')

from functions import convertStringToDatetime

def unique_child_name_and_birth(individuals, fam_row):
    errors = []
    seen = {}
    children = fam_row['Children']
    if not isinstance(children ,float):
        fam_id = fam_row["ID"]
        for index, row in individuals.iterrows():
            if row["ID"] in children:
                birth_dt = convertStringToDatetime(row['Birthday'])
                if row["Name"] in seen and seen.get(row["Name"]) == birth_dt:
                    errors.append("ANOMOLY: FAMILY: US25: {}: More than one child is not unique".format(fam_id))
                else:
                    seen[row["Name"]] = birth_dt
    return errors

class Test(unittest.TestCase):
    def testUniqueSpousesAndMarriage(self):
        file = pd.read_csv('../Data/families4.csv')
        errors = []
        for index, row_fam in file.iterrows():
            if index == 0:
                print(row_fam["ID"])
                self.assertEqual(unique_child_name_and_birth(pd.read_csv('../Data/individuals4.csv'), row_fam), ['ANOMOLY: FAMILY: US25: F10: More than one child is not unique'])

if __name__ == "__main__":
    unittest.main()