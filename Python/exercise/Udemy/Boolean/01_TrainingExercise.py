#!/usr/bin/env python3

''' Requirement:
Create a program that asks the user how far they want to travel. If they want to travel less than
three miles tell them to walk. If they want to travel more than three miles, but less than three
hundred miles, tell them to drive. If they want to travel three hundred miles or more tell them to
fly. '''

howFar=int(input('How far do you want to travel: '));

if howFar < 3:
    print('It is advised to walk to your destination.');
else:
    if howFar < 300:
        print('It is advised to drive to your destination.');
    else:
        print('It is advised to fly to your destination.');