'''
Created on Feb 28, 2021

@author: Valentina Bustamante
'''
import unittest
import pandas as pd
import datetime
import sys
sys.path.insert(0, '../AgileMethods')

from functions import monthNumber, convertStringToDatetime

# checks if birth happened before the current date. if not, error message prints
def birth_before_current_check(row):
    errors = []
    currDate = datetime.datetime.now()

    # row['Birthday'] comes in as a string from the csv, we convert it and store it as a list 'birth' here
    birth_datetime = convertStringToDatetime(row['Birthday'])
    if birth_datetime > currDate:
        errors.append("ERROR: INDIVIDUAL: US01: {}: Birthday {} occurs in the future".format(row['ID'], birth_datetime.date()))

    #print(errors)
    return errors


class Test(unittest.TestCase):


    def testBirthBeforeCurrentDate(self):
        file = pd.read_csv('../Data/individuals.csv')
        for index, row in file.iterrows():
            #print(row)
            self.assertEqual(birth_before_current_check(row), [])

    def testBirthBeforeCurrentDate2(self):
        file = pd.read_csv('../Data/individuals2.csv')
        counter = 0
        for index, row in file.iterrows():
            counter+=1
            #print(row)
            if counter == 15:
                self.assertEqual(birth_before_current_check(row), ['ERROR: INDIVIDUAL: US01: I14: Birthday 2021-06-01 occurs in the future'])

    def testBirthBeforeCurrentDate3(self):
        file = pd.read_csv('../Data/individuals2.csv')
        counter = 0
        for index, row in file.iterrows():
            counter+=1
            #print(row)
            if counter == 1:
                self.assertEqual(birth_before_current_check(row), ['ERROR: INDIVIDUAL: US01: I1: Birthday 4506-11-11 occurs in the future'])

    def testBirthBeforeCurrentDate4(self):
        file = pd.read_csv('../Data/individuals2.csv')
        counter = 0
        for index, row in file.iterrows():
            counter+=1
            #print(row)
            if counter == 5:
                self.assertEqual(birth_before_current_check(row), [])

    def testBirthBeforeCurrentDate5(self):
        file = pd.read_csv('../Data/individuals2.csv')
        counter = 0
        for index, row in file.iterrows():
            counter+=1
            #print(row)
            if counter == 2:
                self.assertEqual(birth_before_current_check(row), ['ERROR: INDIVIDUAL: US01: I2: Birthday 3044-10-15 occurs in the future'])
        

if __name__ == "__main__":
    #print(file.head())
    unittest.main()