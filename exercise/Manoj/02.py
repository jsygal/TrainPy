#!/usr/bin/env python3

'''
Requirement:
2.	Search and count the word available in file. 
'''

inFile='/Users/jishnusygal/VSCode/myCode/pythonBegin/exercise/Manoj/word.txt'
word_count = 0

with open(inFile) as file:
	for line in file:
		word_count += len(line.split())

print ("{1} words are available in file {0}".format(inFile, word_count)
)