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
from ged_reader import monthNumber
    
'''def birth_before_parent_marriage(individuals2, families2):
    errors = []
    for marriage, children_id_list in zip(families2['Married'], families2['Children']):
        for indi_id, birth in zip(individuals2.index.tolist(), individuals2["Birthday"]):
            if isinstance(indi_id, children_id_list):
                marriage_dt = datetime.datetime(int(marriage[2]), monthNumber(marriage[1]), int(marriage[0]))
                birth_dt = datetime.datetime(int(birth[2]), monthNumber(birth[1]), int(birth[0]))
                if birth_dt < marriage_dt:
                    errors.append("ANOMOLY: INDIVIDUAL: US08: {}: Child {} born {} before marriage on ".format(indi_id, indi_id, birth_dt.date(), marriage_dt.date()))
    return errors'''

def birth_before_parent_marriage(fam_row, indi_df):
    errors = []
    if isinstance(fam_row["Married"], str):
        marriage = literal_eval(fam_row['Married'])
        marriage_dt = datetime.datetime(int(marriage[2]), monthNumber(marriage[1]), int(marriage[0]))
        children_list = fam_row['Children']
        for index, row in indi_df.iterrows():
        #try:
            if row['ID'] in children_list:
                birth = literal_eval(row['Birthday'])
                birth_dt = datetime.datetime(int(birth[2]), monthNumber(birth[1]), int(birth[0]))
                if birth_dt < marriage_dt:
                    errors.append("ANOMOLY: FAMILY: US08: {}: Child {} born {} before marriage on {}".format(fam_row['ID'], row['ID'], birth_dt.date(), marriage_dt.date()))

    print(errors)
    return errors
    

'''def birth_before_marriage_check(individuals2, families2):
    errors = []
    for index, row_indi in individuals2.iterrows():
        for index, row_fam in families2.iterrows():
            if row_indi["ID"] == row_fam["Husband ID"] or row_indi["ID"] == row_fam["Wife ID"]:
                if isinstance(row_fam["Married"], str):
                    birth = literal_eval(row_indi['Birthday'])
                    birth_dt = datetime.datetime(int(birth[2]), monthNumber(birth[1]), int(birth[0]))
                    marriage = literal_eval(row_fam['Married'])
                    marriage_dt = datetime.datetime(int(marriage[2]), monthNumber(marriage[1]), int(marriage[0]))
                    if birth_dt > marriage_dt:
                        errors.append("ERROR: INDIVIDUAL: US02: {}: Married {} before born {}".format(row_indi["ID"], marriage_dt.date(), birth_dt.date()))
    return errors'''


class Test(unittest.TestCase):
    def testBirthBeforeParentMarriage(self):
        file = pd.read_csv('families.csv')
        for index, row in file.iterrows():
            self.assertEqual(birth_before_parent_marriage(row, pd.read_csv('individuals.csv')), [])


if __name__ == "__main__":
    unittest.main()