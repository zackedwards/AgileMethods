'''
Created on Apr 21, 2021

@author: Danielle Faustino
'''
import unittest
import pandas as pd

from ast import literal_eval

def ListLivingSingle(indi_df):
    livingSingle = []

    for index, row in indi_df.iterrows():
    #try:        
        name = row['Name']
        age = row['Age']
        spouse = row['Spouse']

        if (age > 30) and not isinstance(spouse, str):
            livingSingle.append(name)

    return livingSingle

class Test(unittest.TestCase):
    def testListLivingSingle(self):
        self.assertEqual(ListLivingSingle(pd.read_csv('../Data/individuals5.csv')), [])

if __name__ == "__main__":
    unittest.main()
