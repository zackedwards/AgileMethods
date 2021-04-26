'''
Created on April 24th, 2021

@author: Zack Edwards

Descripion: Creates error if an siblings are not ordered in decreasing age
'''
import unittest
import pandas as pd

from ast import literal_eval

def sibling_age_check(families_df, individuals_df):
    errors=[]
    for index, row in families_df.iterrows():
        if not isinstance(row['Children'], float):
            sibs=literal_eval(row['Children'])
            ages=[]
            if len(sibs) > 1:
                for sib in sibs:
                    row_number=int(sib[1:])-1
                    try:
                        int_age=int(individuals_df.at[row_number, 'Age'])
                        ages.append(int_age)
                    except:
                        continue
                sorted_ages=sorted(ages, reverse=True)
                if ages != sorted_ages:
                    errors.append("ERROR: FAMILY: US28: {}: Age of Children is not in order".format(row["ID"]))
    return errors


class Test(unittest.TestCase):
    def test_age_exists_check(self):
        file1=pd.read_csv('./Data/families4.csv')
        file2=pd.read_csv('./Data/individuals4.csv')
        self.assertEqual(sibling_age_check(file1, file2), ['ERROR: FAMILY: US28: F6: Age of Children is not in order'])

if __name__ == "__main__":
    unittest.main()