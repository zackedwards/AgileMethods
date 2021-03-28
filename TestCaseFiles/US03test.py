'''
Created on Feb 27, 2021

@author: Zack Edwards
'''
import sys
import unittest #testing library
import pandas as pd #data frame library
import datetime
sys.path.insert(0, '../AgileMethods')

from functions import monthNumber, convertStringToDatetime #converts word to number for months
from ast import literal_eval #converts string to list


def BirthBeforeDeath(individualsDF):
    msg = [] #empty list, this is where error messages will go
    for index, row in individualsDF.iterrows(): #checking each individual in the family tree
        if row['Alive'] == False: #only if the individual is dead
            birth_datetime = convertStringToDatetime(row['Birthday'])
            death_datetime = convertStringToDatetime(row['Death'])
            #The rows above isolate the birth and death
            if birth_datetime > death_datetime: #if the birth is after the death
                msg.append('ERROR: INDIVIDUAL: US03: ' + str(row['ID']) + ' Died: ' + str(death_datetime.date()) +
                    ' occurs before Birth: ' + str(birth_datetime.date()))
                #append the error message
    return msg

#defining unit tests
class Test(unittest.TestCase):

    def testBirthBeforeDeathAll(self):
        self.assertEqual(BirthBeforeDeath(file), [])

if __name__ == "__main__":
    file = pd.read_csv('./Data/individuals.csv')
    unittest.main()
