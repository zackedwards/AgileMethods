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
from ged_reader import monthNumber
    
# checks if birth happened before marriage. if not, error message prints
def birth_before_marriage_check(individuals2, families2):
    errors = []
    for indi_id, birth in zip(individuals2.index.tolist(), individuals2["Birthday"]):
        for marriage_date, husb_id, wife_id in zip(families2["Married"], families2["Husband ID"], families2["Wife ID"]):
            if indi_id == husb_id or indi_id == wife_id:
                if isinstance(marriage_date, list):
                    birth_dt = datetime.datetime(int(birth[2]), monthNumber(birth[1]), int(birth[0]))
                    marriage_dt = datetime.datetime(int(marriage_date[2]), monthNumber(marriage_date[1]), int(marriage_date[0]))
                    if birth_dt < marriage_dt:
                        errors.append("ERROR: INDIVIDUAL: US02: {}: Married {} before born {}".format(indi_id, marriage_dt.date(), birth_dt.date()))
    return errors

class Test(unittest.TestCase):


    def testBirthBeforeCurrentDate(self):
        #print(row)
        self.assertEqual(birth_before_marriage_check(individualsDF, familiesDF), [])


if __name__ == "__main__":
    individualsDF = pd.read_csv('./Data/individuals.csv')
    familiesDF = pd.read_csv('./Data/families.csv')
    #print(file.head())
    unittest.main()