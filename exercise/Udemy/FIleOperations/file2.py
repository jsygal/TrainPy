#!/usr/bin/env python3

'''
Requirement:
Create a program that opens file.txt. Read each line of the file and prepend it with a line
number.'''

import time

with open('/Users/jishnusygal/VSCode/myCode/pythonBegin/exercise/Udemy/FIleOperations/animals.txt') as file:
    animals=[];
    for line in file:
        animals.append(line.rstrip());
    print("Unsorted:",animals);
    print("Sorted:",sorted(animals));
    sortAnimal=sorted(animals);
    with open('/Users/jishnusygal/VSCode/myCode/pythonBegin/exercise/Udemy/FIleOperations/animals-sort.txt',mode='w') as sFile:
        sFile.truncate();
    for animal in sortAnimal:
        with open('/Users/jishnusygal/VSCode/myCode/pythonBegin/exercise/Udemy/FIleOperations/animals-sort.txt',mode='a+') as sFile:
            sFile.write(animal);
            sFile.write('\n');
    print(time.asctime());