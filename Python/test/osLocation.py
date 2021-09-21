#/usr/bin/env python3

import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

print (__location__+'/file.txt')