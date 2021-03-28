'''
Created on March 1st, 2021

@author: Valentina Bustamante

Descripion: Child should be born 
before death of mother and before 
9 months after death of father
'''
import unittest
import pandas as pd
import sys
sys.path.insert(0, '../AgileMethods')

from dateutil.relativedelta import relativedelta
from functions import convertStringToDatetime

# compare children birth dates to parents' death dates
def birth_before_parents_death(individuals2, fam, mother_death, father_death, children):
    errors = []
    for index, row_indi in individuals2.iterrows():
        if row_indi["ID"] in children:
            birth_dt = convertStringToDatetime(row_indi['Birthday'])
            if mother_death[0] and birth_dt > mother_death[1]:
                errors.append("ERROR: FAMILY: US09: {}: Child {} born {} after mother's death on {}".format(fam, row_indi["ID"], birth_dt.date, mother_death[1].date))
            nine_month = relativedelta(months=9)
            if father_death[0] and (birth_dt-nine_month) > father_death[1]:
                errors.append("ERROR: FAMILY: US09: {}: Child {} born {} after more than nine months after father's death on {}".format(fam, row_indi["ID"], birth_dt.date(), father_death[1].date()))
    return errors

# collect mother and father death dates
# collect children ids
def get_parents_death(individuals2, row_fam):
    children = row_fam["Children"]
    mother_death = [False, None]
    father_death = [False, None]
    for index, row_indi in individuals2.iterrows():
        if isinstance(row_indi["Death"], str):
            if row_indi["ID"] == row_fam["Wife ID"][1:] or row_indi["ID"] == row_fam["Husband ID"]:
                death_dt = convertStringToDatetime(row_indi['Death'])
                if row_indi["ID"] == row_fam["Wife ID"]:
                    mother_death = [True, death_dt]
                else:
                    father_death = [True, death_dt] 
    if not isinstance(children ,float):
        return birth_before_parents_death(individuals2, row_fam["ID"], mother_death, father_death, children)
    else: 
        return []
 

class Test(unittest.TestCase):
    
    def testbirthBeforeParentsDeath(self):
        file = pd.read_csv('../Data/families.csv')
        for index, row_fam in file.iterrows():
            self.assertEqual(get_parents_death(pd.read_csv('../Data/individuals.csv'), row_fam), ["ERROR: FAMILY: US09: F1: Child I1 born 2001-10-04 after more than nine months after father's death on 2000-10-10", "ERROR: FAMILY: US09: F1: Child I4 born 2003-02-12 after more than nine months after father's death on 2000-10-10"])
            break
    
    def testbirthBeforeParentsDeath2(self):
        file = pd.read_csv('../Data/families.csv')
        for index, row_fam in file.iterrows():
            if index == 1:
                self.assertEqual(get_parents_death(pd.read_csv('../Data/individuals.csv'), row_fam), [])
                break

if __name__ == "__main__":
    unittest.main()