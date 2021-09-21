#!/usr/bin/env python3
csvFile = '/Users/jishnusygal/VSCode/myCode/pythonBegin/exercise/Manoj/emp.csv'

with open(csvFile, 'r') as my_file:
    for line in my_file:
        columns = line.strip().split(',')
        print (line.strip())
    