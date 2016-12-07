#maps
import random
import sys
def square(x):
  return x**2

squares = map(square, range(10))
#print(squares)

names = ['Anne', 'Amy', 'Bob', 'David', 'Carrie', 'Barbara', 'Zach']
mem = map(len, names)
print([x for x in names if x.__contains__('Carrie')])

