#!/usr/bin/env python3

'''
1.	Create employee data excel file with duplicate record that contain the fallowing field
•	Emp id
•	Emp Name
•	Emp Salary
Write a python code to display duplicate employee record and count no of duplicate record available into a employee data file.
'''

csvFile = '/Users/jishnusygal/VSCode/myCode/pythonBegin/exercise/Manoj/emp.csv'
outFile = '/Users/jishnusygal/VSCode/myCode/pythonBegin/exercise/Manoj/out.csv'

entries = []
duplicate_entries = []
with open(csvFile, 'rt') as my_file:
    for line in my_file:
        columns = line.strip().split(',')
        if columns[2] not in entries:
            entries.append(columns[2])
        else:
            duplicate_entries.append(columns[2]) 
dupCount = len(duplicate_entries)
if dupCount > 0:
    print('There are {} Duplicate entries in {}.\nThe Dumplicate Entries are as below:'.format(dupCount,csvFile))
    
    with open(outFile, 'w') as out_file:
        with open(csvFile, 'r') as my_file:
            for line in my_file:
                columns = line.strip().split(',')
                if columns[2] in duplicate_entries:
                    print (line.strip())
                    out_file.write(line)
else:
    print ("No repetitions")