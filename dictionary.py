import random
import sys
import os

children = {'1' : 'edwin', '2': 'ganesh', '3': 'kalyan'}
print(children['1'])
del children['2']
children['2'] ='ganesh'


children['3'] = 'Ravi'
new = list(children)
print(new)
print(len(children))
print(children.get('1'))
print(children.keys())
print(children.values())