'''
Created on Feb 27, 2021

@author: Zack Edwards
'''
import unittest
import pandas as pd

from ged_reader import monthNumber

def BirthBeforeDeath(df):
    errors = []
    for index, row in df.iterrows():
    #try:
        if row['Alive'] == 'False':
            if int(row['Birthday'][2]) > int(row['Death'][2]):
                errors.append('ERROR: INDIVIDUAL: US03: Died', row['Death'], 'occurs before birth', row['Birthday'])
            elif row['Birthday'][2] == row['Death'][2]:
                if monthNumber(row['Birthday'][1]) > monthNumber(row['Death'][1]):
                    errors.append('ERROR: INDIVIDUAL: US03: Died', row['Death'], 'occurs before birth', row['Birthday'])
                elif monthNumber(row['Birthday'][1]) == monthNumber(row['Death'][1]):
                    if row['Birthday'][0] > row['Death'][0]:
                        errors.append('ERROR: INDIVIDUAL: US03: Died', row['Death'], 'occurs before birth', row['Birthday'])
    print(errors)
    return errors
#     except:
#         return 'invalid'

class Test(unittest.TestCase):


    def testBirthBeforeDeath(self):
        self.assertEqual(BirthBeforeDeath(pd.read_csv('individuals.csv')), [])


if __name__ == "__main__":
    unittest.main()