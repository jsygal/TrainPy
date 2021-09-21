#!/usr/bin/env python3

'''
Requirement:
Create a program that opens file.txt. Read each line of the file and prepend it with a line
number.'''

import os

with open('/Users/jishnusygal/VSCode/myCode/pythonBegin/exercise/Udemy/FIleOperations/file.txt') as file:
    lineNum=1
    for line in file:
        print('{}:{}'.format(lineNum,line.rstrip()))
        lineNum=lineNum+1