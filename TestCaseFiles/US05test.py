'''
Created on Feb 28, 2021

@author: William Escamilla
'''
import unittest
import pandas as pd
import datetime
import sys
sys.path.insert(0, '../AgileMethods')

from ged_reader import monthNumber
    
# Makes sure marriage happened before death of either spouse. If not, error thrown
def marriage_before_death_check(individualsDF, familiesDF):
    errors = []
    for indi_id, marriage in zip(individualsDF.index.tolist(), individualsDF["Birthday"]):
        for death_date, husb_id, wife_id in zip(familiesDF["Death"], familiesDF["Husband ID"], familiesDF["Wife ID"]):
            if indi_id == husb_id or indi_id == wife_id:
                if isinstance(death_date, list):
                    marriage_dt = datetime.datetime(int(marriage[2]), monthNumber(marriage[1]), int(marriage[0]))
                    death_dt = datetime.datetime(int(death_date[2]), monthNumber(death_date[1]), int(death_date[0]))
                    if marriage_dt < death_dt:
                        errors.append("ERROR: INDIVIDUAL: US05: {}: Death {} before Married {}".format(indi_id, death_dt.date(), marriage_dt.date()))
    return errors

class Test(unittest.TestCase):


    def testBirthBeforeCurrentDate(self):
        #print(row)
        self.assertEqual(marriage_before_death_check(individualsDF, familiesDF), [])


if __name__ == "__main__":
    individualsDF = pd.read_csv('./Data/individuals.csv')
    familiesDF = pd.read_csv('./Data/families.csv')
    #print(file.head())
    unittest.main()