'''
Created on April 11th, 2021

@author: Zack Edwards

Descripion: Creates error if aunts/uncles are married to neice/nephew
'''
import unittest
import pandas as pd
import sys

# Checks if husband id and wife id from a family are both in the children list of siblings in a list called row_fam
def aunt_uncle_married_check(families, row_fam):
    aunts_uncle = row_fam["Children"] #aunts and uncles
    errors = []
    if not isinstance(aunts_uncle ,float):
        #getting a list of cousins
        all_cousins=[]
        for index, row_fam1 in families.iterrows():
            if isinstance(row_fam1["Wife ID"],str) and isinstance(row_fam1["Husband ID"],str):
                if row_fam1["Wife ID"] or row_fam1["Husband ID"] in aunts_uncle: #if hus or wif in the list of aunts/uncles
                    if not isinstance(row_fam1['Children'], float):
                        for i in row_fam1['Children']:
                            all_cousins.append(i) #add cousins to a list

        for index, row_fam2 in families.iterrows():
            if isinstance(row_fam2["Wife ID"],str) and isinstance(row_fam2["Husband ID"],str):
                if row_fam2["Husband ID"] in all_cousins or row_fam2["Wife ID"] in all_cousins:
                    if row_fam2["Husband ID"] in aunts_uncles or row_fam2["Wife ID"] in aunts_uncles:
                        errors.append("ERROR: FAMILY: US20: {}: Spouses {} and {} are aunt/uncle and niece/nephew in family {}".format(row_fam2["ID"], row_fam2["Wife ID"], row_fam2["Husband ID"], row_fam["ID"]))
        return errors
    else: 
        return []

class Test(unittest.TestCase):
    
    def aunt_uncle_married_check(self):
        file = pd.read_csv('./Data/families.csv')
        errors = []
        for index, row_fam in file.iterrows():
            errors += (cousins_married_check(file, row_fam))
        self.assertEqual(errors, [])

if __name__ == "__main__":
    unittest.main()