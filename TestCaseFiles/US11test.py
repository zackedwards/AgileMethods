'''
Created on Feb 27, 2021

@author: Zack Edwards
'''
import sys
import unittest
import pandas as pd
sys.path.insert(0, '../AgileMethods')

from functions import convertStringToDatetime


def NoBigamy(dataframe):
    msg = ''
    for index, row in dataframe.iterrows():
        if isinstance(row['Husband ID'], str):
            hus_id = row['Husband ID'] #save husband id
        if isinstance(row['Wife ID'], str):
            wife_id = row['Wife ID'] #save wife id
        if isinstance(row['Married'], str):
            married_datetime1 = convertStringToDatetime(row['Married'])
            for index2, row2 in dataframe.iterrows():
                if row2.all() == row.all(): #dont compare row to itself
                    continue
                if wife_id == row2['Wife ID']:
                    if isinstance(row2['Married'], str): #get second marriage date
                        married_datetime2 = convertStringToDatetime(row2['Married'])
                        if isinstance(row['Divorced'], str): #different case if family is divorced or not
                            divorce_datetime1 = convertStringToDatetime(row['Divorced']) #save divorce date
                            if married_datetime2 > married_datetime1 and married_datetime2 < divorce_datetime1: 
                                msg+=('ERROR: FAMILY: US11: ' + str(row['ID']) + ': '+wife_id+' married to both ' + hus_id +
                                            ' and ' + str(row2['Husband ID'])+' at the same time')
                        elif isinstance(row2['Divorced'], str):
                            divorce_datetime2 = convertStringToDatetime(row2['Divorced']) #save divorce date
                            if married_datetime1 > married_datetime2 and married_datetime1 < divorce_datetime2: 
                                msg+=('ERROR: FAMILY: US11: ' + str(row['ID']) + ': '+wife_id+' married to both ' + hus_id +
                                            ' and ' + str(row2['Husband ID'])+' at the same time')
                        else:
                            msg+=('ERROR: FAMILY: US11: ' + str(row['ID']) + ': '+wife_id+' married to both ' + hus_id +
                                            ' and ' + str(row2['Husband ID'])+' at the same time')
                if hus_id == row2['Husband ID']:
                    if isinstance(row2['Married'], str): #get second marriage date
                        married_datetime2 = convertStringToDatetime(row2['Married'])
                        if isinstance(row['Divorced'], str): #different case if family is divorced or not
                            divorce_datetime1 = convertStringToDatetime(row['Divorced']) #save divorce date
                            if married_datetime2 > married_datetime1 and married_datetime2 < divorce_datetime1:
                                msg+=('ERROR: FAMILY: US11: ' + str(row['ID']) + ': '+hus_id+' married to both ' + wife_id +
                                        ' and ' + str(row2['Wife ID'])+' at the same time')
                        elif isinstance(row2['Divorced'], str):
                            divorce_datetime2 = convertStringToDatetime(row2['Divorced']) #save divorce date
                            if married_datetime1 > married_datetime2 and married_datetime1 < divorce_datetime2: 
                                msg+=('ERROR: FAMILY: US11: ' + str(row['ID']) + ': '+ hus_id+' married to both ' + wife_id +
                                        ' and ' + str(row2['Wife ID'])+' at the same time')
                        else:
                            msg+=('ERROR: FAMILY: US11: ' + str(row['ID']) + ': '+ hus_id + ' married to both ' + wife_id +
                                        ' and ' + str(row2['Wife ID'])+' at the same time')
    return msg


class Test(unittest.TestCase):

    def testNoBigamyAll(self):
        file = pd.read_csv('./Data/families.csv')
        #print(NoBigamy(file))
        self.assertEqual(NoBigamy(file), '')

    def testNoBigamy5(self):
        expected_err = "ERROR: FAMILY: US11: Test: I2 married to both I3 and I4 at the same time"
        test=pd.DataFrame(columns=['ID','Married','Divorced','Husband ID','Wife ID'])
        test = test.append({'ID': 'Test', 'Married': "['11','DEC','1999']",'Divorced': "['10','NOV','2003']",'Husband ID':'I2','Wife ID': 'I3'}, ignore_index=True)
        test = test.append({'ID': 'Test', 'Married': "['14','JAN','2000']",'Divorced': "['10','NOV','2009']",'Husband ID':'I2','Wife ID': 'I4'}, ignore_index=True)
        #print(NoBigamy(test))
        self.assertEqual(NoBigamy(test), expected_err)


if __name__ == "__main__":
    unittest.main()
