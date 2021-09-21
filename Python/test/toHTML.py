#!/usr/bin/env python3

import os
import textile

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(__location__+'/file.txt') as infile:
    with open (__location__+'/outFile.eml','w') as outfile:
        for line in infile:
            print(textile.textile(line.strip()))
            html=textile.textile(line.strip())
            outfile.write(html)