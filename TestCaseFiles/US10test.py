'''
Created on March 1st, 2021

@author: Valentina Bustamante

Descripion: Marriage should be at least 
14 years after birth of both spouses 
(parents must be at least 14 years old)
'''
import unittest
import pandas as pd
import datetime
import sys
sys.path.insert(0, '../AgileMethods')

from ast import literal_eval
from functions import monthNumber, convertStringToDatetime

#get marriage date and both ages of the people married
def marriageAfterFourteen(individuals2, families2):
    errors = []
    for index, row_indi in individuals2.iterrows():
        for index, row_fam in families2.iterrows():
            if row_indi["ID"] == row_fam["Husband ID"] or row_indi["ID"] == row_fam["Wife ID"]:
                if isinstance(row_fam["Married"], str):
                    # compare marriage and birthdate and get the difference
                    # if difference is less than 14 then print an error
                    birth_dt = convertStringToDatetime(row_indi['Birthday'])
                    marriage_dt = convertStringToDatetime(row_fam['Married'])
                    duration_in_s = (marriage_dt - birth_dt).total_seconds()
                    years = divmod(duration_in_s, 31536000)[0]
                    if years < 14:
                        errors.append("ERROR: INDIVIDUAL: US10: {}: Married {} before age 14".format(row_indi["ID"], marriage_dt.date()))
    return errors

class Test(unittest.TestCase):


    def testMarriageAfterFourteen(self):
        self.assertEqual(marriageAfterFourteen(pd.read_csv('./Data/individuals.csv'), pd.read_csv('./Data/families.csv')), [])

if __name__ == "__main__":
    unittest.main()