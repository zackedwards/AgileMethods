'''
Created on Feb 27, 2021

@author: Zack Edwards
'''
import sys
import unittest
import pandas as pd
import datetime
sys.path.insert(0, '../AgileMethods')

from ged_reader import monthNumber
from ast import literal_eval


def NoBigamy(row):
    msg = ''
    if isinstance(row['Married'], str) and isinstance(row['Divorced'], str):
        married = literal_eval(row['Married'])
        divorce = literal_eval(row['Divorced'])
        married_datetime = datetime.datetime(int(married[2]), monthNumber(married[1]), int(married[0]))
        divorce_datetime = datetime.datetime(int(divorce[2]), monthNumber(divorce[1]), int(divorce[0]))

        if married_datetime > divorce_datetime:
            msg = ('ERROR: INDIVIDUAL: US03: ' + str(row['ID']) + ': Divorced: ' + str(divorce) +
                   ' occurs before married: ' + str(married))
    if msg != '':
        print(msg)
        return False
    else:
        return True


class Test(unittest.TestCase):

    def testNoBigamyAll(self):
        file = pd.read_csv('./Data/families.csv')
        for index, row in file.iterrows():
            self.assertEqual(NoBigamy(row), True)

    def testNoBigamy1(self):
        file = pd.read_csv('./Data/families.csv')
        self.assertEqual(NoBigamy(file.iloc[2]), True)

    def testNoBigamy2(self):
        file = pd.read_csv('./Data/families.csv')
        self.assertEqual(NoBigamy(file.iloc[3]), True)

    def testNoBigamy3(self):
        file = pd.read_csv('./Data/families.csv')
        self.assertEqual(NoBigamy(file.iloc[1]), True)

    def testNoBigamy4(self):
        file = pd.read_csv('./Data/families.csv')
        self.assertEqual(NoBigamy(file.iloc[5]), True)

    def testNoBigamy5(self):
        expected_err = ["ERROR: FAMILY: US03: Test: Divorced: ['10','NOV','1998'] "
                        "occurs before Marriage: ['11','DEC','1999']"]
        self.assertEqual(NoBigamy({'ID': 'Test', 'Married': "['11','DEC','1999']",
                                           'Divorced': "['10','NOV','1998']"}), False)


if __name__ == "__main__":
    unittest.main()
