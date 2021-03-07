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

def are_any_people_over_150(df):
    list_of_people_over_150 = []

    for index, row in df.iterrows():
        if row['Age'] >= 150:
            list_of_people_over_150.append(row['Name'])

    if list_of_people_over_150 == []:
        return False
    else:
        return True

class Test(unittest.TestCase):


    def testAgeLessThan150(self):
        for index, row in file.iterrows():
            #print(row)
            self.assertEqual(age_less_than_150(row), [])
            #if row['Alive'] == 'True':
                #self.asserEqual(age_less_than_150(row), ["ERROR: INDIVIDUAL: US07: I1: More than 150 years old - Birth ['11', 'NOV', '1999']"])
            self.assertFalse(are_any_people_over_150(file))


if __name__ == "__main__":
    file = pd.read_csv('./Data/individuals.csv')
    #print(file.head())
    unittest.main()