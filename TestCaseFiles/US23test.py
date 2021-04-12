'''
Created on Apr 9, 2021

@author: Danielle Faustino
'''
import unittest
import pandas as pd

def UniqueNameAndBirth(indi_df):
    errors = []
    seen = []

    for index, row in indi_df.iterrows():
        #try:         
        if (row['Name'], row['Birthday']) in seen:
            errors.append("ANOMOLY: INDIVIDUAL: US23: {}: Does not have unique name {} and birthday {}".format(row["ID"], row['Name'], row['Birthday']))
        else:
            seen.append((row['Name'], row['Birthday']))
                    
    #print(errors)
    return errors

class Test(unittest.TestCase):
    def testUniqueNameAndBirth(self):
        self.assertEqual(UniqueNameAndBirth(pd.read_csv('../Data/individuals3.csv')), [])

if __name__ == "__main__":
    unittest.main()