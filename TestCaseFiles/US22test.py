
'''
Created on April 11th, 2021

@author: William Escamilla

Descripion: All individual and family ids should be unique
'''
import unittest
import pandas as pd
import sys
sys.path.insert(0, './')

from functions import convertStringToDatetime

# Checks if husband and wife are male and female respectively
def unique_ids_check(individualsDF, familiesDF):
    errors = []
    famIdList = []
    indiIdList = []
    for index, famRow in familiesDF.iterrows():
        if famRow['ID'] not in famIdList:
            famIdList.append(famRow['ID'])
        else:
            errors.append("ERROR: FAMILY: US22: {}: Family's ID already seen before, not unique".format(famRow["ID"]))

    for index, indiRow in individualsDF.iterrows():
        if indiRow['ID'] not in indiIdList:
            indiIdList.append(indiRow['ID'])
        else:
            errors.append("ERROR: INDIVIDUAL: US22: {}: Individual's ID already seen before, not unique".format(indiRow["ID"]))
    return errors

class Test(unittest.TestCase):
    
    def test_unique_ids(self):
        self.assertEqual(unique_ids_check(file1, file2), [])

if __name__ == "__main__":
    file1 = pd.read_csv('./Data/individuals3.csv')
    file2 = pd.read_csv("./Data/families3.csv")
    unittest.main()