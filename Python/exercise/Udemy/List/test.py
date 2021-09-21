#!/usr/bin/env python3

family = ["Jithu Sygal","Jishnu Sygal","Indu Sygal","Sygal Vasukutty"]
#lastLen=len(variable)
#endVal=int(lastLen-1)
#print(variable[1:endVal])
#search=input('Search the family memeber: ')

sortFamily = sorted(family);

''' try:
    familyIndex=family.index(search)
    print ("{} is in the family list.".format(search));
except:
    print("{} is not in the familty yet.".format(search))

for i in family:
    print(i) '''

for i in sortFamily:
    print(i)