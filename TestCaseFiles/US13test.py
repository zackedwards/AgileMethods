'''
Created on March 29, 2021

@author: William
'''
import unittest
import pandas as pd
import sys
sys.path.insert(0, '../AgileMethods')
import datetime

from ast import literal_eval
from functions import convertStringToDatetime
 
# checks if birth happened before marriage. if not, error message prints
def siblings_spacing(individualsDF, familiesDF):
    errors = []
    for index, famRow in familiesDF.iterrows():
        if isinstance(famRow["Children"], str) and len(literal_eval(famRow["Children"])) > 1: # No need to check if there is only one child in this family
            childList = literal_eval(famRow['Children'])
            for childId in childList:
                child1Bday_dt = convertStringToDatetime(individualsDF.iloc[int(childId[1:])-1]["Birthday"])
                for childId2 in childList[(childList.index(childId)+1):]:
                    child2Bday_dt = convertStringToDatetime(individualsDF.iloc[int(childId2[1:])-1]["Birthday"])
                    if (child1Bday_dt-child2Bday_dt).total_seconds() >= 2*24*60*60 and (child1Bday_dt-child2Bday_dt).total_seconds() <= 8*31*24*60*60:
                        errors.append("ERROR: FAMILY: US13: {}: Birthday of siblings {} & {} are between 2 days and 8 months".format(famRow["ID"], childId, childId2))

    return errors

class Test(unittest.TestCase):


    def testSiblingSpacing(self):
        #print(row)
        self.assertEqual(siblings_spacing(pd.read_csv('./Data/individuals.csv'), pd.read_csv('./Data/families.csv')), [])


if __name__ == "__main__":
    #print(file.head())
    unittest.main()