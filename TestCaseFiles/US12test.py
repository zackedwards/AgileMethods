'''
Created on Mar 28, 2021

@author: Zack Edwards
'''
import sys
import unittest
import pandas as pd
import datetime
sys.path.insert(0, '../AgileMethods')

from functions import convertStringToDatetime
from datetime import timedelta
from ast import literal_eval

def ParentsTooOld(IndividualsDF, FamiliesDF):
    msg=[]
    for index, row in FamiliesDF.iterrows():
        wife_id = row['Wife ID']
        hus_id = row['Husband ID'] #save husband id
        if isinstance(row['Children'], str):
            chil_ids = literal_eval(row['Children'])
            child_birth=[]
            for index2, indi_row in IndividualsDF.iterrows():
                if isinstance(wife_id, str) and indi_row['ID'] == wife_id:
                    wife_birth = convertStringToDatetime(indi_row['Birthday'])
                if isinstance(hus_id, str) and indi_row['ID'] == hus_id:
                    hus_birth = convertStringToDatetime(indi_row['Birthday'])
                if indi_row['ID'] in chil_ids:
                    child_birth.append(convertStringToDatetime(indi_row['Birthday']))
            year = timedelta(days=365)
            mdelta =  60*year
            fdelta = 80*year
            counter=0
            for birth in child_birth:
                if isinstance(wife_id, str) and birth - mdelta >= wife_birth:
                    #print(type(chil_ids))
                    msg.append("ERROR: FAMILY: US12: "+str(row['ID'])+": "+str(wife_id)+" is more than 60 years older than her child "+ str(chil_ids[counter]))
                if isinstance(hus_id, str) and birth - fdelta >= hus_birth:
                    msg.append("ERROR: FAMILY: US12: "+str(row['ID'])+": "+str(hus_id)+" is more than 80 years older than his child "+ str(chil_ids[counter]))
                counter+=1
    return msg

class Test(unittest.TestCase):

    def testNoBigamyAll(self):
        file1 = pd.read_csv('./Data/families.csv')
        file2 = pd.read_csv('./Data/individuals.csv')
        #print(ParentsTooOld(file2, file1))
        self.assertEqual(ParentsTooOld(file2, file1), [])

if __name__ == "__main__":
    unittest.main()