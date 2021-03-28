'''
Created on Feb 28, 2021

@author: Valentina Bustamante
'''
import unittest
import pandas as pd
import sys
sys.path.insert(0, '../AgileMethods')

from functions import convertStringToDatetime
 
# checks if birth happened before marriage. if not, error message prints
def birth_before_marriage_check(individuals2, families2):
    errors = []
    for index, row_indi in individuals2.iterrows():
        for index, row_fam in families2.iterrows():
            if row_indi["ID"] == row_fam["Husband ID"] or row_indi["ID"] == row_fam["Wife ID"]:
                if isinstance(row_fam["Married"], str):
                    birth_dt = convertStringToDatetime(row_indi['Birthday'])
                    marriage_dt = convertStringToDatetime(row_fam['Married'])
                    if birth_dt > marriage_dt:
                        errors.append("ERROR: INDIVIDUAL: US02: {}: Married {} before born {}".format(row_indi["ID"], marriage_dt.date(), birth_dt.date()))
    return errors

class Test(unittest.TestCase):


    def testbirth_before_marriage_check(self):
        #print(row)
        self.assertEqual(birth_before_marriage_check(pd.read_csv('../Data/individuals.csv'), pd.read_csv('../Data/families.csv')), ['ERROR: INDIVIDUAL: US02: I8: Married 2020-09-12 before born 2020-11-09', 'ERROR: INDIVIDUAL: US02: I17: Married 1925-08-08 before born 1940-09-13'])
    def testbirth_before_marriage_check2(self):
        self.assertEqual(birth_before_marriage_check(pd.read_csv('../Data/individuals2.csv'), pd.read_csv('../Data/families.csv')), ['ERROR: INDIVIDUAL: US02: I2: Married 2001-10-08 before born 3044-10-15', 'ERROR: INDIVIDUAL: US02: I14: Married 2005-10-12 before born 2021-06-01'])
    def testbirth_before_marriage_check3(self):
        self.assertEqual(birth_before_marriage_check(pd.read_csv('../Data/individuals3.csv'), pd.read_csv('../Data/families.csv')), ['ERROR: INDIVIDUAL: US02: I2: Married 2001-10-08 before born 2021-10-10', 'ERROR: INDIVIDUAL: US02: I7: Married 2020-09-12 before born 2021-09-05'])
    def testbirth_before_marriage_check4(self):
        self.assertEqual(birth_before_marriage_check(pd.read_csv('../Data/individuals.csv'), pd.read_csv('../Data/families3.csv')), ['ERROR: INDIVIDUAL: US02: I7: Married 1960-07-02 before born 1960-11-08', 'ERROR: INDIVIDUAL: US02: I7: Married 1950-10-09 before born 1960-11-08', 'ERROR: INDIVIDUAL: US02: I8: Married 1960-07-02 before born 2020-11-09', 'ERROR: INDIVIDUAL: US02: I9: Married 1950-10-09 before born 1969-11-12'])
    def testbirth_before_marriage_check5(self):
        self.assertEqual(birth_before_marriage_check(pd.read_csv('../Data/individuals4.csv'), pd.read_csv('../Data/families2.csv')), ['ERROR: INDIVIDUAL: US02: I2: Married 1998-07-02 before born 3044-10-15', 'ERROR: INDIVIDUAL: US02: I9: Married 1950-10-09 before born 2020-11-02', 'ERROR: INDIVIDUAL: US02: I9: Married 1979-05-02 before born 2020-11-02', 'ERROR: INDIVIDUAL: US02: I10: Married 1979-05-02 before born 1980-09-02'])

if __name__ == "__main__":
    #print(file.head())
    unittest.main()