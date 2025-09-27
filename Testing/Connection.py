'''
Created on 23-Oct-2021

@author: jeete
'''
# Q11. How many entries (people) are above the mean level of 'Glucose'? (3 points)
import pandas as pd
df = pd.read_csv('C:\\Users\\jeete\\eclipse-workspace\\AshuProject\\Testing\\diabetes.csv')
criteria = df[df['Glucose'] > df["Glucose"].mean()]
print("Entries (people) are above the mean level of 'Glucose' ::", criteria["Glucose"].count())

#----------------------------------------------------------------------------------------------------
# Q14. How many entries (people) have their 'BloodPressure' equal to the median of 'BloodPressure' and their 'BMI' less than the mode of 'BMI'? (3 points)
criteria1 = df[df['BloodPressure'] == df["BloodPressure"].median()]
criteria2 = criteria1[criteria1['BMI'] < criteria1.mode()['BMI'][0]]
print("Entries (people) have their 'BloodPressure' equal to the median of 'BloodPressure' and their 'BMI' less than the mode of 'BMI':: ",criteria2["BloodPressure"].count())
# ------------------------------------------------------------------------------------
# Q18. How many entries (people) are there who has the diabetes disease and how many entries (people) do not have the diabetes disease? (4 points)

