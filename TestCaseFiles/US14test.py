'''
Created on March 8, 2021

@author: William & Zack
'''
import unittest
import pandas as pd
import datetime
import sys
sys.path.insert(0, '../AgileMethods')

from numpy import NaN
from ast import literal_eval
from functions import monthNumber
 
# checks if birth happened before marriage. if not, error message prints
def no_more_than_5_kids_check(individualsDF, familiesDF):
    errors = []
    for index, famRow in familiesDF.iterrows():
        numTwins = 0
        if isinstance(famRow["Children"], str) and len(literal_eval(famRow["Children"])) > 5: # Needs to be greater than 5
            birthList=[]
            for childId in literal_eval(famRow['Children']):
                childBday=literal_eval(individualsDF.iloc[int(childId[1:])-1]["Birthday"])
                birthList.append(datetime.datetime(int(childBday[2]), monthNumber(childBday[1]), int(childBday[0])))
            for birth in birthList:
                for birth2 in birthList[(birthList.index(birth)+1):]:
                    if abs((birth-birth2).days) < 2:
                        numTwins += 1
            if(numTwins > 5):
                errors.append("ERROR: FAMILY: US14: {}: More than 5 children born at the same time (Within 2 days of eachother)".format(famRow["ID"]))

    return errors

class Test(unittest.TestCase):


    def testbirth_before_marriage_check(self):
        #print(row)
        self.assertEqual(no_more_than_5_kids_check(pd.read_csv('./Data/individuals.csv'), pd.read_csv('./Data/families.csv')), ['ERROR: FAMILY: US14: F6: More than 5 children born at the same time (Within 2 days of eachother)'])


if __name__ == "__main__":
    #print(file.head())
    unittest.main()