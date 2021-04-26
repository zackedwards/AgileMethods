'''
Created on Apr 26, 2021

@author: William Escamilla
'''
import unittest
import pandas as pd

def listDeceased(indi_df):
    errors = []
    seen = []

    for index, row in indi_df.iterrows():
        #try:         
        if (row['Alive'] == False):
            errors.append("ANOMOLY: INDIVIDUAL: US29: {}: Is deceased".format(row["ID"]))
                    
    #print(errors)
    return errors

class Test(unittest.TestCase):
    def testAllDeceased(self):
        self.assertEqual(listDeceased(pd.read_csv('./Data/individuals3.csv')), [])

if __name__ == "__main__":
    unittest.main()