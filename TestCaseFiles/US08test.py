'''
Created on Mar 4, 2021
@author: Danielle Faustino
'''
import unittest
import pandas as pd
import datetime
import sys
sys.path.insert(0, '../AgileMethods')

from ast import literal_eval
from functions import monthNumber

def birth_before_parent_marriage(fam_row, indi_df):
    errors = []
    if isinstance(fam_row["Married"], str):
        marriage = literal_eval(fam_row['Married'])
        marriage_dt = datetime.datetime(int(marriage[2]), monthNumber(marriage[1]), int(marriage[0]))
        children_list = fam_row['Children']
        for index, row in indi_df.iterrows():
        #try:
            if type(children_list) != float and row['ID'] in children_list:
                birth = literal_eval(row['Birthday'])
                birth_dt = datetime.datetime(int(birth[2]), monthNumber(birth[1]), int(birth[0]))
                if birth_dt < marriage_dt:
                    errors.append("ANOMOLY: FAMILY: US08: {}: Child {} born {} before marriage on {}".format(fam_row['ID'], row['ID'], birth_dt.date(), marriage_dt.date()))

    #print(errors)
    return errors


class Test(unittest.TestCase):
    def testBirthBeforeParentMarriage(self):
        file = pd.read_csv('./Data/families.csv')
        for index, row in file.iterrows():
            self.assertEqual(birth_before_parent_marriage(row, pd.read_csv('./Data/individuals.csv')), [])


if __name__ == "__main__":
    unittest.main()