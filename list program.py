#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#write a program that prints out all the elements of the list that are less than 5.
'''a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
ab = list()
print("Displayed list = " ,a)
num = input("Please enter a whole number \n")
if(int(num) <= 0):
  print("Number is Zero or Negative")
else:
  for x in a:
    if(x < num):
      ab.append(x)
  print("%s %d %s %s" %("The numbers which are less then", int(num),"are ",ab))
  '''
"""a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print([x for x in a if x<5])
num = [y for y in a if y>10]
print(list(filter(lambda x : x < 5 ,a)))"""

import math


num = lambda x: math.sqrt(x)

print(num(4))
arg = lambda x: 'big' if x > 100 else 'small'
print(arg(37))
print(list(arg(167)))



""""
#important need to research on it
import numpy as np
print ([a[i] for i in np.where(np.array(a) < 5)[0]])
print(a[i] for i in np.where(np.array(a) < 5[0]))"""