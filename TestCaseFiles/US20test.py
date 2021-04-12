'''
Created on April 11th, 2021

@author: Zack Edwards

Descripion: Creates error if aunts/uncles are married to neice/nephew
'''
import unittest
import pandas as pd

from ast import literal_eval

# Checks if husband id and wife id from a family are both in the children list of siblings in a list called row_fam
def aunt_uncle_married_check(families):
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

        for index, row_fam2 in families.iterrows():
            if isinstance(row_fam2["Wife ID"],str) and isinstance(row_fam2["Husband ID"],str):
                if row_fam2["Husband ID"] in cousinsList and row_fam2["Wife ID"] in siblingsList:
                    errors.append("ERROR: FAMILY: US20: {}: Spouses {} and {} are aunt/uncle and niece/nephew in family {}".format(row_fam2["ID"], row_fam2["Wife ID"], row_fam2["Husband ID"], famRow["ID"]))
                if row_fam2["Husband ID"] in siblingsList and row_fam2["Wife ID"] in cousinsList:
                    errors.append("ERROR: FAMILY: US20: {}: Spouses {} and {} are aunt/uncle and niece/nephew in family {}".format(row_fam2["ID"], row_fam2["Wife ID"], row_fam2["Husband ID"], famRow["ID"]))
    return errors
    

class Test(unittest.TestCase):
    
    def aunt_uncle_married_check(self):
        file = pd.read_csv('./Data/families3.csv')
        print(aunt_uncle_married_check(file))
        self.assertEqual(aunt_uncle_married_check(file), ['ERROR: FAMILY: US20: F7: Spouses I1 and I3 are aunt/uncle and niece/nephew in family F3'])

if __name__ == "__main__":
    file = pd.read_csv('./Data/families3.csv')
    print(aunt_uncle_married_check(file))
    unittest.main()