'''
Created on March 1st, 2021

@author: Valentina Bustamante
'''
import unittest
import pandas as pd
import datetime
import sys
#sys.path.insert(0, '../AgileMethods')

from ast import literal_eval
from dateutil.relativedelta import relativedelta
#from ged_reader import monthNumber

def monthNumber(month):
    months = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
    return months.index(month) + 1

# checks if birth
def birthBeforeParentsDeath(individuals2, row_fam):
    errors = []
    children = row_fam["Children"]
    mother_death = [False, None]
    father_death = [False, None]
    for index, row_indi in individuals2.iterrows():
        if isinstance(row_indi["Death"], str):
            if row_indi["ID"] == row_fam["Wife ID"] or row_indi["ID"] == row_fam["Husband ID"]:
                death = literal_eval(row_indi['Death'])
                death_dt = datetime.datetime(int(death[2]), monthNumber(death[1]), int(death[0]))
                if row_indi["ID"] == row_fam["Wife ID"]:
                    mother_death = [True, death_dt]
                else:
                    father_death = [True, death_dt] 
         
    for index, row_indi in individuals2.iterrows():
        if row_indi["ID"] in children:
            birth = literal_eval(row_indi['Birthday'])
            birth_dt = datetime.datetime(int(birth[2]), monthNumber(birth[1]), int(birth[0]))
            if mother_death[0] and birth_dt > mother_death[1]:
                errors.append("ERROR: FAMILY: US09: {}: Child {} born {} after mother's death on {}".format(row_fam["ID"], row_indi["ID"], birth_dt.date, mother_death[1].date))
            nine_month = relativedelta(months=9)
            if father_death[0] and (birth_dt-nine_month) > father_death[1]:
                errors.append("ERROR: FAMILY: US09: {}: Child {} born {} after more than nine months after father's death on {}".format(row_fam["ID"], row_indi["ID"], birth_dt.date(), father_death[1].date()))
    print( errors)
    return errors

class Test(unittest.TestCase):
    
    def testbirthBeforeParentsDeath(self):
        file = pd.read_csv('../Data/families.csv')
        for index, row_fam in file.iterrows():
            self.assertEqual(birthBeforeParentsDeath(pd.read_csv('../Data/individuals.csv'), row_fam), [])
            break

if __name__ == "__main__":
    #print(file.head())
    unittest.main()