#!/usr/bin/env python3

'''
1.	Create employee data excel file with duplicate record that contain the fallowing field
•	Emp id
•	Emp Name
•	Emp Salary
Write a python code to display duplicate employee record and count no of duplicate record available into a employee data file.
'''

import os
import csv

csvFile = '/Users/jishnusygal/VSCode/myCode/pythonBegin/exercise/Manoj/emp.csv'
# initializing the titles and rows list
fields = []
rows = []
  
# reading csv file
with open(csvFile, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
  
    # 