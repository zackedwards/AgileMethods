'''
Created on Feb 28, 2021

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

# checks if birth happened before marriage. if not, error message prints
'''def birth_before_marriage_check(individuals2, families2):
    errors = []
    for indi_id, birth in zip(individuals2.index.tolist(), individuals2["Birthday"]):
        for marriage_date, husb_id, wife_id in zip(families2["Married"], families2["Husband ID"], families2["Wife ID"]):
            if indi_id == husb_id or indi_id == wife_id:
                if isinstance(marriage_date, list):
                    birth_dt = datetime.datetime(int(birth[2]), monthNumber(birth[1]), int(birth[0]))
                    marriage_dt = datetime.datetime(int(marriage_date[2]), monthNumber(marriage_date[1]), int(marriage_date[0]))
                    if birth_dt < marriage_dt:
                        errors.append("ERROR: INDIVIDUAL: US02: {}: Married {} before born {}".format(indi_id, marriage_dt.date(), birth_dt.date()))
    return errors'''

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
        self.assertEqual(birth_before_marriage_check(pd.read_csv('../Data/individuals.csv'), pd.read_csv('../Data/families.csv')), [])
    def testbirth_before_marriage_check2(self):
        self.assertEqual(birth_before_marriage_check(pd.read_csv('../Data/individuals2.csv'), pd.read_csv('../Data/families.csv')), ['ERROR: INDIVIDUAL: US02: I2: Married 1998-07-02 before born 3044-10-15'])
    def testbirth_before_marriage_check3(self):
        self.assertEqual(birth_before_marriage_check(pd.read_csv('../Data/individuals3.csv'), pd.read_csv('../Data/families.csv')), ['ERROR: INDIVIDUAL: US02: I2: Married 1998-07-02 before born 2021-10-10', 'ERROR: INDIVIDUAL: US02: I7: Married 1960-07-02 before born 2021-09-05', 'ERROR: INDIVIDUAL: US02: I7: Married 1950-10-09 before born 2021-09-05'])
    def testbirth_before_marriage_check4(self):
        self.assertEqual(birth_before_marriage_check(pd.read_csv('../Data/individuals.csv'), pd.read_csv('../Data/families3.csv')), ['ERROR: INDIVIDUAL: US02: I2: Married 1920-07-02 before born 1963-10-10', 'ERROR: INDIVIDUAL: US02: I3: Married 1920-07-02 before born 1965-08-02'])
    def testbirth_before_marriage_check5(self):
        self.assertEqual(birth_before_marriage_check(pd.read_csv('../Data/individuals4.csv'), pd.read_csv('../Data/families2.csv')), ['ERROR: INDIVIDUAL: US02: I2: Married 1998-07-02 before born 3044-10-15', 'ERROR: INDIVIDUAL: US02: I9: Married 1950-10-09 before born 2020-11-02', 'ERROR: INDIVIDUAL: US02: I9: Married 1979-05-02 before born 2020-11-02', 'ERROR: INDIVIDUAL: US02: I10: Married 1979-05-02 before born 1980-09-02'])
    


if __name__ == "__main__":
    #print(file.head())
    unittest.main()