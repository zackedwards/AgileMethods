'''
Created on Apr 9, 2021

@author: Valentina Bustamante
'''
import unittest
import pandas as pd
from ast import literal_eval
import sys
sys.path.insert(0, '../')

from functions import convertStringToDatetime

def consistent_individuals_and_families(individuals, families):
    errors = []
    seen = {}
    has_spouse = False

    # True if spouse id and indi id are in the same family
    spouse_match = False

    for index, row in individuals.iterrows():

        if not isinstance(row["Spouse"] ,float):
            has_spouse = True

        for index, fam_row in families.iterrows():
            children = fam_row['Children']
            fam_id = fam_row["ID"]
            if not isinstance(children ,float):
                if row["Child"] == fam_id:
                    if not (row["ID"] in children):
                        errors.append("ERROR: INDIVIDUAL: US26: {}: Individual does not have correct family ID under child".format(row["ID"]))
        
    for index, fam_row in families.iterrows():
        no_children = False
        if isinstance(children ,float):
            no_children = True
        else:
            children = literal_eval(fam_row['Children'])
        for index, indi_row in individuals.iterrows():
            if indi_row["ID"] == fam_row["Husband ID"] or indi_row["ID"] == fam_row["Wife ID"]:
                if indi_row["Spouse"] != fam_row["ID"] and not isinstance(fam_row["Divorced"] ,float) :
                    errors.append("ERROR: INDIVIDUAL: US26: {}: Individual does not have correct family ID {} under spouse".format(indi_row["ID"], indi_row["Spouse"]))
                if indi_row["ID"] == fam_row["Wife ID"]: 
                    wife_found = True
                if indi_row["ID"] == fam_row["Husband ID"]: 
                    husband_found = True
            if not isinstance(children ,float) and children != [] and indi_row["ID"] in children:
                children.remove(indi_row["ID"] )
        if not (wife_found and husband_found):
            errors.append("ERROR: FAMILY: US26: {}: No individual in individuals record found for spouses in the family record".format(fam_row["ID"]))
        if not no_children and children != []:
            for i in children:
                errors.append("ERROR: FAMILY: US26: {}: Child {} is not an individual in individuals record".format(fam_row["ID"], indi_row["ID"]))

    return errors

class Test(unittest.TestCase):
    def testUniqueSpousesAndMarriage(self):
        self.assertEqual(consistent_individuals_and_families(pd.read_csv('../Data/individuals4.csv'), pd.read_csv('../Data/families4.csv')), 
        ['ERROR: INDIVIDUAL: US26: I1: Individual does not have correct family ID under spouse', 
        'ERROR: INDIVIDUAL: US26: I9: Individual does not have correct family ID under spouse', 
        'ERROR: INDIVIDUAL: US26: I10: Individual does not have correct family ID under spouse', 
        'ERROR: FAMILY: US26: I9: Individual does not have correct family ID under spouse'
        ])

if __name__ == "__main__":
    unittest.main()