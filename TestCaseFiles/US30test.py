'''
Created on Apr 26, 2021

@author: William Escamilla
'''
import unittest
import pandas as pd

def listLivingAndMarried(famDF, indi_df):
    errors = []
    seen = []

    for index, famRow in famDF.iterrows():

        if (isinstance(famRow['Married'], str) and not isinstance(famRow['Divorced'], str)):
            if isinstance(famRow['Husband ID'], str):
                hus_id = famRow['Husband ID']
            if isinstance(famRow['Wife ID'], str):
                wife_id = famRow['Wife ID']

            for index, indiRow in indi_df.iterrows():
                if(indiRow['ID'] == hus_id or indiRow['ID'] == wife_id):
                    if(indiRow['Alive'] == True and not indiRow['ID'] in seen):
                        seen.append(indiRow['ID'])
                        errors.append("ANOMOLY: INDIVIDUAL: US30: {}: Is living and married".format(indiRow["ID"]))
                    
    #print(errors)
    return errors

class Test(unittest.TestCase):
    def testLivingAndMarried(self):
        self.assertEqual(listLivingAndMarried(pd.read_csv('./Data/families3.csv'), pd.read_csv('./Data/individuals3.csv')), [])

if __name__ == "__main__":
    unittest.main()