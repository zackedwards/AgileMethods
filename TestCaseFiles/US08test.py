'''
Created on Mar 4, 2021
@author: Danielle Faustino
'''
import unittest
import pandas as pd
import sys
sys.path.insert(0, '../AgileMethods')

from functions import convertStringToDatetime

def birth_before_parent_marriage(fam_row, indi_df):
    errors = []
    if isinstance(fam_row["Married"], str):
        marriage_dt = convertStringToDatetime(fam_row['Married'])
        children_list = fam_row['Children']
        for index, row in indi_df.iterrows():
        #try:
            if type(children_list) != float and row['ID'] in children_list:
                birth_dt = convertStringToDatetime(row['Birthday'])
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