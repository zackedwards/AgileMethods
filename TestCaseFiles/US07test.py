'''
Created on Feb 28, 2021

@author: Dana Faustino
'''
import unittest
import pandas as pd

    
def age_less_than_150(row):
    error = []
    age = row['Age']
    ifAlive = row['Alive']
    # checks if age is less than 150
    if age >= 150:
        if ifAlive == 'False':
            error.append("ERROR: INDIVIDUAL: US07: {}: More than 150 years old at death - Birth {}: Death {}".format(row['ID'], row['Birthday'], row['Death']))
        else:
            error.append("ERROR: INDIVIDUAL: US07: {}: More than 150 years old - Birth {}".format(row['ID'], row['Birthday']))
    # Prints out errors for age less than 150: US07
    print(error)
    return error

def people_over_150(df):
    name_list = []

    for index, row in df.iterrows():
        if row['Age'] >= 150:
            name_list.append(row['Name'])

    if name_list == []:
        return False
    else:
        return True

def people_under_150(df):
    name_list = []

    for index, row in df.iterrows():
        if row['Age'] < 150:
            name_list.append(row['Name'])

    if len(name_list) == (len(df) - 1):
        return True
    else:
        return False
    

class Test(unittest.TestCase):

    def testAgeLessThan150(self):
        for index, row in file.iterrows():
            print(row)
            self.assertEqual(age_less_than_150(row), [])

    def testAgeLessThan150_2(self):
        for index, row in file.iterrows():
            print(row)
            self.assertFalse(people_over_150(file))

    def testAgeLessThan150_3(self):
        for index, row in file.iterrows():
            print(row)
            self.assertTrue(people_under_150(file))

    def testAgeLessThan150_4(self):
        for index, row in file.iterrows():
            print(row)
            if row['Alive'] == 'True' and row['Age'] >= 150 :
                self.assertEqual(age_less_than_150(row), "ERROR: INDIVIDUAL: US07: {}: More than 150 years old - Birth {}".format(row['ID'], row['Birthday']))

    def testAgeLessThan150_5(self):
        for index, row in file.iterrows():
            print(row)
            if row['Alive'] == 'False' and row['Age'] >= 150 :
                self.assertEqual(age_less_than_150(row), "ERROR: INDIVIDUAL: US07: {}: More than 150 years old at death - Birth {}: Death {}".format(row['ID'], row['Birthday'], row['Death']))


if __name__ == "__main__":
    file = pd.read_csv('./Data/individuals.csv')
    #print(file.head())
    unittest.main()