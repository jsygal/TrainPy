#!/usr/bin/env python3

list_of_tuples = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

print ('Unsorted list of tuples: {}'.format(list_of_tuples));

list_of_tuples.sort(key=lambda x:x[1])

print('Sorted list of tuples: {}'.format(list_of_tuples))

