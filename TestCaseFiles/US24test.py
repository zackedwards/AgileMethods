'''
Created on Apr 9, 2021

@author: Danielle Faustino
'''
import unittest
import pandas as pd

def UniqueSpousesAndMarriage(fam_df):
    errors = []
    seen = []

    for index, row in fam_df.iterrows():
        #try:      
        #if isinstance(row['Married'], str) and isinstance(row['Husband Name'], str)  and isinstance(row['Wife Name'], str):
            if (row['Married'], row['Husband Name'], row['Wife Name']) in seen:
                errors.append("ANOMOLY: FAMILY: US24: {}: Does not have unique spouses, {} and {}, and marriage date {}".format(row["ID"], row['Husband Name'], row['Wife Name'], row['Married']))
            else:
                seen.append((row['Married'], row['Husband Name'], row['Wife Name']))
                    
    #print(errors)
    return errors

class Test(unittest.TestCase):
    def testUniqueSpousesAndMarriage(self):
        self.assertEqual(UniqueSpousesAndMarriage(pd.read_csv('../Data/families3.csv')), [])

if __name__ == "__main__":
    unittest.main()