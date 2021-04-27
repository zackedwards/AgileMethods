'''
Created on Apr 21, 2021

@author: Danielle Faustino
'''
import unittest
import pandas as pd

from ast import literal_eval

def ListMultipleBirths(fam_df):
    multipleBirths = []

    for index, row in fam_df.iterrows():
    #try:        
        children_list = row['Children']

        if isinstance(children_list, str):
           if ',' in children_list:
               multipleBirths.append(children_list)

    return ["ERROR: FAMILY: US32: List of multiple births: {}".format(multipleBirths)]

class Test(unittest.TestCase):
    def testListMultipleBirths(self):
        self.assertEqual(ListMultipleBirths(pd.read_csv('../Data/families5.csv')), [])

if __name__ == "__main__":
    unittest.main()
