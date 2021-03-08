'''
Created on Feb 27, 2021

@author: Zack Edwards
'''
import sys
import unittest
import pandas as pd
import datetime
sys.path.insert(0, '../AgileMethods')

from functions import monthNumber
from ast import literal_eval


def BirthBeforeDeath(row):
    msg = []
    if row['Alive'] == False:
        birth = literal_eval(row['Birthday'])
        death = literal_eval(row['Death'])
        birth_datetime = datetime.datetime(int(birth[2]), monthNumber(birth[1]), int(birth[0]))
        death_datetime = datetime.datetime(int(death[2]), monthNumber(death[1]), int(death[0]))

        if birth_datetime > death_datetime:
            msg.append('ERROR: INDIVIDUAL: US03: ' + str(row['ID']) + ' Died: ' + str(death) +
                   ' occurs before Birth: ' + str(birth))
    return msg


class Test(unittest.TestCase):

    def testBirthBeforeDeathAll(self):
        file = pd.read_csv('./Data/individuals.csv')
        for index, row in file.iterrows():
            self.assertEqual(BirthBeforeDeath(row), [])

    def testBirthBeforeDeath1(self):
        file = pd.read_csv('./Data/individuals.csv')
        self.assertEqual(BirthBeforeDeath(file.iloc[2]), [])

    def testBirthBeforeDeath2(self):
        file = pd.read_csv('./Data/individuals.csv')
        self.assertEqual(BirthBeforeDeath(file.iloc[6]), [])

    def testBirthBeforeDeath3(self):
        file = pd.read_csv('./Data/individuals.csv')
        self.assertEqual(BirthBeforeDeath(file.iloc[8]), [])

    def testBirthBeforeDeath4(self):
        file = pd.read_csv('./Data/individuals.csv')
        self.assertEqual(BirthBeforeDeath(file.iloc[7]), [])

    def testBirthBeforeDeath5(self):
        expected_err = ["ERROR: INDIVIDUAL: US03: Test Died: ['10', 'NOV', '1998'] "
                        "occurs before Birth: ['11', 'DEC', '1999']"]
        self.assertEqual(BirthBeforeDeath({'Alive': False, 'ID': 'Test', 'Birthday': "['11','DEC','1999']",
                                           'Death': "['10','NOV','1998']"}), expected_err)


if __name__ == "__main__":
    unittest.main()
