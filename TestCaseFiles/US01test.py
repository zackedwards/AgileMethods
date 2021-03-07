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

# checks if birth happened before the current date. if not, error message prints
def birth_before_current_check(row):
    errors = []
    currDate = datetime.datetime.now()

    # row['Birthday'] comes in as a string from the csv, we convert it and store it as a list 'birth' here
    birth = literal_eval(row['Birthday'])
    birth_datetime = datetime.datetime(int(birth[2]), monthNumber(birth[1]), int(birth[0]))
    if birth_datetime > currDate:
        errors.append("ERROR: INDIVIDUAL: US01: {}: Birthday {} occurs in the future".format(row['ID'], birth_datetime.date()))

    #print(errors)
    return errors


class Test(unittest.TestCase):


    def testBirthBeforeCurrentDate(self):
        file1 = pd.read_csv('./Data/individuals.csv')
        for index, row in file1.iterrows():
            #print(row)
            self.assertEqual(birth_before_current_check(row), [])
        

if __name__ == "__main__":
    #print(file.head())
    unittest.main()