'''
Created on Feb 28, 2021

@author: William Escamilla
'''
import unittest
import pandas as pd
import datetime
import sys
sys.path.insert(0, '../AgileMethods')

from ast import literal_eval
from functions import monthNumber
    
# Makes sure divorce happened before death of either spouse. If not, error thrown
def divorce_before_death_check(famRow, individualsDF):
    errors = []
    # Only runs if the family was actually married and does not have a value of "NaN"
    if isinstance(famRow["Divorced"], str):
        # Retrieves the married date and converts it to a number using "datetime.datetime"
        divorcedDate = literal_eval(famRow["Divorced"])
        divorced_dt = datetime.datetime(int(divorcedDate[2]), monthNumber(divorcedDate[1]), int(divorcedDate[0]))

        # Checks if the husband in the family is dead, if so, proceed
        if individualsDF.iloc[int(famRow["Husband ID"][1:])-1]["Alive"] == False:
            # Retrieves the husband's death date and converts it to a number using "datetime.datetime"
            husbandDeathDate = literal_eval(individualsDF.iloc[int(famRow["Husband ID"][1:])-1]["Death"])
            husbandDeath_dt = datetime.datetime(int(husbandDeathDate[2]), monthNumber(husbandDeathDate[1]), int(husbandDeathDate[0]))

            # Finally checks if divorce occured after the husband died, if so, append an error
            if divorced_dt > husbandDeath_dt:
                errors.append("ERROR: INDIVIDUAL: US05: {}: Death {} before Divorced {}".format(famRow["Husband ID"], husbandDeath_dt.date(), divorced_dt.date()))
        
        # Checks if the wife in the family is dead, if so, proceed
        if individualsDF.iloc[int(famRow["Wife ID"][1:])-1]["Alive"] == False:
            # Retrieves the wife's death date and converts it to a number using "datetime.datetime"
            wifeDeathDate = literal_eval(individualsDF.iloc[int(famRow["Wife ID"][1:])-1]["Death"])
            wifeDeath_dt = datetime.datetime(int(wifeDeathDate[2]), monthNumber(wifeDeathDate[1]), int(wifeDeathDate[0]))

            # Finally checks if divorce occured after the wife died, if so, append an error
            if divorced_dt > wifeDeath_dt:
                errors.append("ERROR: INDIVIDUAL: US05: {}: Death {} before Divorced {}".format(famRow["Wife ID"], wifeDeath_dt.date(), divorced_dt.date()))

    return errors

class Test(unittest.TestCase):

    # Inputs each row from the families DataFrame into our function and checks if the errors returned equals an empty list []
    def testDivorce(self):
        for index, famRow in familiesDF.iterrows():
            self.assertEqual(divorce_before_death_check(famRow, individualsDF), [])


if __name__ == "__main__":
    # Pulls family and individual data and turns it back into a DataFrame
    familiesDF = pd.read_csv('./Data/families.csv')
    individualsDF = pd.read_csv('./Data/individuals.csv')
    #print(familiesDF.head(10))
    #print(individualsDF.head(10))
    unittest.main()