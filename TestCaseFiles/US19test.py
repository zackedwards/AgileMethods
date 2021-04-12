'''
Created on April 11th, 2021

@author: Zack Edwards

Descripion: Creates error if first cousins are married)
'''
import unittest
import pandas as pd
import sys
sys.path.insert(0, '../AgileMethods')

from ast import literal_eval

# Checks if husband id and wife id from a family are both in the children list of siblings in a list called row_fam
def cousins_married_check(families): #aunts and uncles
    errors = []
    for index, famRow in families.iterrows():
        cousinsList = []
        if isinstance(famRow['Children'], str):
            siblingsList = literal_eval(famRow['Children']) #get list of siblings who are aunts and uncles
            for index, famRow1 in families.iterrows():
                if isinstance(famRow1['Wife ID'], str):
                    if famRow1['Wife ID'] in siblingsList:
                        if isinstance(famRow1['Children'], str):
                            for cousin in literal_eval(famRow1['Children']):
                                cousinsList.append(cousin) #append the cousins, neice/nephew of the above siblings
                if isinstance(famRow1['Husband ID'], str):
                    if famRow1['Husband ID'] in siblingsList:
                        if isinstance(famRow1['Children'], str):
                            for cousin in literal_eval(famRow1['Children']):
                                cousinsList.append(cousin) #for husband as well

            for index, famRow2 in families.iterrows():
                if isinstance(famRow2['Wife ID'], str) and isinstance(famRow2['Husband ID'], str):
                    if famRow2['Wife ID'] in cousinsList and famRow2['Husband ID'] in cousinsList:
                        errors.append("ERROR: FAMILY: US19: {}: Spouses {} and {} are cousins in family {}".format(famRow2["ID"], famRow2["Wife ID"], famRow2["Husband ID"], famRow["ID"]))
    return errors


class Test(unittest.TestCase):
    
    def test_cousins_married(self):
        print(cousins_married_check(pd.read_csv('./Data/families.csv')))
        self.assertEqual(cousins_married_check(pd.read_csv('./Data/families.csv')), ['ERROR: FAMILY: US19: F10: Spouses I17 and I20 are cousins in family F6'])

if __name__ == "__main__":
    unittest.main()