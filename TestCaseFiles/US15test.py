'''
Created on Mar 28, 2021

@author: Danielle Faustino
'''
import unittest
import pandas as pd
from ast import literal_eval

def LessThan15Siblings(fam_df):
    errors = []

    for index, row in fam_df.iterrows():
    #try:
        if isinstance(row['Children'], str): # Children is only a list after using literal_eval on it
            if (len(literal_eval(row['Children'])) >= 15) :
                errors.append("ANOMOLY: FAMILY: US15: {}: Family has 15 or more siblings".format(row["ID"]))

    #print(errors)
    return errors


class Test(unittest.TestCase):

    def testLessThan15Siblings(self):
        self.assertEqual(LessThan15Siblings(pd.read_csv('./Data/families.csv')), [])


if __name__ == "__main__":
    unittest.main()