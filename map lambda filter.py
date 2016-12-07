#usr/bin/local/python

import sys
import math
import os
from functools import reduce

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(list(map(lambda x: x-2,a)))




#program to add coordinates in a list
"""
coords =[]
for x in range(0,5):
    for y in range(0,5):
        coordinates =(x,y)
        coords.append(coordinates)
print(coords)
"""
#Suppose we want to take a list of names and find only those starting with the letter B:
""""
names = ['Anne', 'Amy', 'Bob', 'David', 'Carrie', 'Barbara', 'Zach']
b_names =[]

for name in names:
    if name.startswith('B'):
        b_names.append(name)
print(b_names)

#sample names read file
for one in open('names.txt'):
    print(one)"""

"""Iterator for looping over a sequence backwards."""

"""string = 'maps'
print(len(string))
for char in range(len(string)-1, -1, -1):
    print(char)
    #print(string[char])"""

"""strn = "how are you doing bro what plans for future"

vag = strn.split()
print(vag)
print(len(vag))
for char in range(len(vag)-1,-1,-1):
    #print(char)
    print(vag[char])"""
#generators
"""
from math import pi,cos
rem = sum(i for i in range(10))
print(rem)
cos_table =  {x: cos(x*pi/180) for x in range(0,91)}
print(cos_table)"""







