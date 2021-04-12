'''
Created on April 11th, 2021

@author: William Escamilla

Descripion: Husband in family should be male anfd wife in family should be female
'''
import unittest
import pandas as pd
import sys
sys.path.insert(0, './')

from functions import convertStringToDatetime

# Checks if husband and wife are male and female respectively
def correct_gender_check(individualsDF, familiesDF):
    errors = []
    for index, famRow in familiesDF.iterrows():
        if isinstance(famRow['Husband ID'], str):
            hus_id = famRow['Husband ID']
        if isinstance(famRow['Wife ID'], str):
            wife_id = famRow['Wife ID']

        for index, indiRow1 in individualsDF.iterrows():
            if isinstance(indiRow1['ID'], str):
                if indiRow1['ID'] == hus_id:                    
                    if isinstance(indiRow1['Gender'], str):
                        hus_gender = indiRow1['Gender']
                if indiRow1['ID'] == wife_id:
                    if isinstance(indiRow1['Gender'], str):
                        wife_gender = indiRow1['Gender']

        if hus_gender != "M":
            errors.append("ERROR: FAMILY: US21: {}: Gender of Husband {} is not Male".format(famRow["ID"], hus_id))

        if wife_gender != "F":
            errors.append("ERROR: FAMILY: US21: {}: Gender of Wife {} is not Female".format(famRow["ID"], wife_id))
    return errors

class Test(unittest.TestCase):
    
    def test_gender(self):
        self.assertEqual(correct_gender_check(file1, file2), [])

if __name__ == "__main__":
    file1 = pd.read_csv('./Data/individuals3.csv')
    file2 = pd.read_csv("./Data/families3.csv")
    unittest.main()
