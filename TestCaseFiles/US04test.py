'''
Created on Feb 27, 2021

@author: Zack Edwards
'''
import sys
import unittest
import pandas as pd
sys.path.insert(0, '../AgileMethods')

from functions import convertStringToDatetime


def MarriageBeforeDivorce(row):
    msg = []
    if isinstance(row['Married'], str) and isinstance(row['Divorced'], str):
        married_datetime = convertStringToDatetime(row['Married'])
        divorce_datetime = convertStringToDatetime(row['Divorced'])

        if married_datetime > divorce_datetime:
            msg.append('ERROR: FAMILY: US04: ' + str(row['ID']) + ': Divorced: ' + str(divorce_datetime.date()) +
                   ' occurs before Marriage: ' + str(married_datetime.date()))
    return msg
    


class Test(unittest.TestCase):

    def testMarriageBeforeDivorceAll(self):
        file = pd.read_csv('./Data/families.csv')
        for index, row in file.iterrows():
            self.assertEqual(MarriageBeforeDivorce(row), [])

    def testMarriageBeforeDivorce1(self):
        file = pd.read_csv('./Data/families.csv')
        self.assertEqual(MarriageBeforeDivorce(file.iloc[2]), [])

    def testMarriageBeforeDivorce2(self):
        file = pd.read_csv('./Data/families.csv')
        self.assertEqual(MarriageBeforeDivorce(file.iloc[3]), [])

    def testMarriageBeforeDivorce3(self):
        file = pd.read_csv('./Data/families.csv')
        self.assertEqual(MarriageBeforeDivorce(file.iloc[1]), [])

    def testMarriageBeforeDivorce4(self):
        file = pd.read_csv('./Data/families.csv')
        self.assertEqual(MarriageBeforeDivorce(file.iloc[5]), [])

    def testMarriageBeforeDivorce5(self):
        expected_err = ["ERROR: FAMILY: US04: Test: Divorced: 1998-11-10 "
                        "occurs before Marriage: 1999-12-11"]
        self.assertEqual(MarriageBeforeDivorce({'ID': 'Test', 'Married': "['11','DEC','1999']",
                                           'Divorced': "['10','NOV','1998']"}), expected_err)


if __name__ == "__main__":
    unittest.main()
