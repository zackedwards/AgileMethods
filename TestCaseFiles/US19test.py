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
def cousins_married_check(families, row_fam): #aunts and uncles
    errors = []
    if not isinstance(row_fam['Children'] ,float):
        children = literal_eval(row_fam["Children"])
        #getting a list of cousins
        cousins=[]
        all_cousins=[]
        for index, row_fam1 in families.iterrows():
            if isinstance(row_fam1["Wife ID"],str) and isinstance(row_fam1["Husband ID"],str):
                if row_fam1["Wife ID"] in children or row_fam1["Husband ID"] in children: #if hus or wif in the list of aunts/uncles
                    if not isinstance(row_fam1['Children'], float):
                        cousins.append(literal_eval(row_fam1['Children'])) #append a list fo their kids to my list of cousins
                        for i in literal_eval(row_fam1['Children']):
                            all_cousins.append(i)

        if len(cousins) >= 2:
            for index, row_fam2 in families.iterrows():
                if isinstance(row_fam2["Wife ID"],str) and isinstance(row_fam2["Husband ID"],str):
                    if row_fam2["Husband ID"] in all_cousins and row_fam2["Wife ID"] in all_cousins:
                        errors.append("ERROR: FAMILY: US19: {}: Spouses {} and {} are cousins in family {}".format(row_fam2["ID"], row_fam2["Wife ID"], row_fam2["Husband ID"], row_fam["ID"]))
        return errors
    else: 
        return []

    cousinsList = []
    for index, famRow in families.iterrows():
        if isinstance(famRow['Children'], str):
            siblingsList = literal_eval(famRow['Children'])
            for sibling in siblingsList:
                if isinstance(individualsDF.iloc[int(sibling[1:])-1]["Child"], str):
                    for indiCousin in literal_eval(individualsDF.iloc[int(sibling[1:])-1]["Child"]):
                        cousinsList.append(indiCousin)
        for index, indiRow in individuals.iterrows():
            # Check if the current individual is in cousinsList
                #if so, check if this current individual is married to anyone else in cousinsList


class Test(unittest.TestCase):
    
    def test_cousins_married(self):
        file = pd.read_csv('./Data/families3.csv')
        errors = []
        for index, row_fam in file.iterrows():
            errors += (cousins_married_check(file, row_fam))
        self.assertEqual(errors, [])

if __name__ == "__main__":
    unittest.main()