#!/usr/bin/env python3

'''
Requirement:
Create a list of airports that includes a series of tuples containing an airport's name and its code.
Loop through the list and utilize tuple assignment. Use one variable to hold the airport name and
another variable to hold the airport code. Display the airport's name and code to the screen.
'''

airports = [("O’Hare International Airport","ORD"), ("Los Angeles International Airport","LAX"),
    ("Dallas/Fort Worth International Airport","DFW"), ("Denver International Airport","DEN")]

for (airport, code) in airports:
    print("The code for {} is {}".format(airport, code))