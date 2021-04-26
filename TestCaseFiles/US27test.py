'''
Created on April 24th, 2021

@author: Zack Edwards

Descripion: Creates error if an individuals age is not included
'''
import unittest
import pandas as pd

def include_age_check(individuals_df):
    errors=[]
    for index, row in individuals_df.iterrows():
        try:
            age=int(row['Age'])
        except:
            errors.append("ERROR: FAMILY: US27: {}: Age of indivudal is not recorded".format(row["ID"]))
    return errors

class Test(unittest.TestCase):
    def age_exists_check(self):
        file = pd.read_csv('./Data/individuals.csv')
        self.assertEqual(include_age_check(file), [])

if __name__ == "__main__":
    unittest.main()