#!/usr/bin/env python3
 
# Initializing list of dictionaries
lis = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
 
print ("The list printed sorting by Make: ")
print (sorted(lis, key = lambda i: i['make']))
 
print ("\r")
 
print ("The list printed sorting by Make and Model: ")
print (sorted(lis, key = lambda i: (i['make'], i['model'])))
 
print ("\r")
 
print ("The list printed sorting by make in descending order: ")
print (sorted(lis, key = lambda i: i['make'],reverse=True))