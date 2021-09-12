#!/usr/bin/env python3

''' Requirement:
Create a dictionary that contains a list of people and one interesting fact about each of them.
Display each person and their interesting fact to the screen. Next, change a fact about one of
the people. Also add an additional person and corresponding fact. Display the new list of people
and facts. Run the program multiple times and notice if the order changes. '''

def displayPrint():
    for i in behavior:
        print ("{0}: {1}".format(i,behavior[i]));
    print ('\n')

behavior = {'Jeff':'Is afraid of clowns','David':'Plays the Piano','Jason':'Can fly an airplane'}
displayPrint()

behavior['Jeff'] = 'Is afraid of heights.'
displayPrint()

behavior['Jill']="Can hula dance."
displayPrint()
