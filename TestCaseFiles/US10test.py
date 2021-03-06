'''
Created on March 1st, 2021

@author: Valentina Bustamante
'''
import unittest
import pandas as pd
import datetime
import sys
#sys.path.insert(0, '../AgileMethods')

from ast import literal_eval
#from ged_reader import monthNumber

def monthNumber(month):
    months = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
    return months.index(month) + 1
#get marriage date and both ages of the people married
def marriageAfterFourteen(individuals2, families2):
    errors = []
    for index, row_indi in individuals2.iterrows():
        for index, row_fam in families2.iterrows():
            if row_indi["ID"] == row_fam["Husband ID"] or row_indi["ID"] == row_fam["Wife ID"]:
                if isinstance(row_fam["Married"], str):
                    # compare marriage and birthdate and get the difference
                    # if difference is less than 14 then print an error
                    birth = literal_eval(row_indi['Birthday'])
                    birth_dt = datetime.datetime(int(birth[2]), monthNumber(birth[1]), int(birth[0]))
                    marriage = literal_eval(row_fam['Married'])
                    marriage_dt = datetime.datetime(int(marriage[2]), monthNumber(marriage[1]), int(marriage[0]))
                    duration_in_s = (marriage_dt - birth_dt).total_seconds()
                    years = divmod(duration_in_s, 31536000)[0]
                    print(years)
                    if years < 14:
                        errors.append("ERROR: INDIVIDUAL: US10: {}: Married {} before age 14".format(row_indi["ID"], marriage_dt.date()))
    return errors

class Test(unittest.TestCase):


    def testMarriageAfterFourteen(self):
        self.assertEqual(marriageAfterFourteen(pd.read_csv('../Data/individuals.csv'), pd.read_csv('../Data/families.csv')), [])

if __name__ == "__main__":
    #print(file.head())
    unittest.main()