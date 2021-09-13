#!/usr/bin/env python3

'''
Requirement:
3.	Replace the word into file and count.
'''

#input file
inFile='/Users/jishnusygal/VSCode/myCode/pythonBegin/exercise/Manoj/word.txt'
outFile='/Users/jishnusygal/VSCode/myCode/pythonBegin/exercise/Manoj/word-out.txt'
sWord=input("Enter the word to search: ")
rWord=input("Enter the word to be replaced with: ")
word_count = 0
with open(inFile, "rt") as fIn:
#output file to write the result to
    with open(outFile, "wt") as fOut:
    #for each line in the input file
        for line in fIn:
            fOut.write(line.replace(sWord, rWord))