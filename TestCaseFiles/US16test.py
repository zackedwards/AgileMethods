'''
Created on Mar 6, 2021

@author: Valentina Bustamente & Danielle Faustino
'''
import unittest
import pandas as pd

def MaleLastNames(fam_row, indi_df):
    errors = []
    husband_last_name = fam_row['Husband Name'][1]
    children_list = fam_row['Children']

    for index, row in indi_df.iterrows():
    #try:
        if row['Gender'] == 'M' and row['ID'] in children_list:
            if row['Name'][1] != husband_last_name:
                errors.append("ERROR: FAMILY: US16: {}: Child {} does not have father's last name".format(fam_row["ID"], row['ID']))

    print(errors)
    return errors


class Test(unittest.TestCase):

    def testMaleLastNames(self):
        file = pd.read_csv('families.csv')
        for index, row in file.iterrows():
            self.assertEqual(MaleLastNames(row, pd.read_csv('individuals.csv')), [])

    


if __name__ == "__main__":
    unittest.main()