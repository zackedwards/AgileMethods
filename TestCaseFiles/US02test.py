'''
Created on Feb 28, 2021

@author: Valentina Bustamante
'''
import unittest
import pandas as pd
import datetime
import sys
sys.path.insert(0, '../AgileMethods')

from ast import literal_eval
from functions import monthNumber
 
# checks if birth happened before marriage. if not, error message prints
def birth_before_marriage_check(individuals2, families2):
    errors = []
    for index, row_indi in individuals2.iterrows():
        for index, row_fam in families2.iterrows():
            if row_indi["ID"] == row_fam["Husband ID"] or row_indi["ID"] == row_fam["Wife ID"]:
                if isinstance(row_fam["Married"], str):
                    birth = literal_eval(row_indi['Birthday'])
                    birth_dt = datetime.datetime(int(birth[2]), monthNumber(birth[1]), int(birth[0]))
                    marriage = literal_eval(row_fam['Married'])
                    marriage_dt = datetime.datetime(int(marriage[2]), monthNumber(marriage[1]), int(marriage[0]))
                    if birth_dt > marriage_dt:
                        errors.append("ERROR: INDIVIDUAL: US02: {}: Married {} before born {}".format(row_indi["ID"], marriage_dt.date(), birth_dt.date()))
    return errors

class Test(unittest.TestCase):


    def testbirth_before_marriage_check(self):
        #print(row)
        self.assertEqual(birth_before_marriage_check(pd.read_csv('./Data/individuals.csv'), pd.read_csv('./Data/families.csv')), [])


if __name__ == "__main__":
    #print(file.head())
    unittest.main()