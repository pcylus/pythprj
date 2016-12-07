#Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

import sys
from datetime import date

while(True):
  print("Please enter your name and your age")
  name = input("Name = \t")
  age = input("Age =  \t")

  if (isinstance(name,str) and isinstance(int(age),int)):
    print('Entered name and age is', str(name), int(age))
    current_year = date.today().year
    log = 100 - int(age)
    ans = current_year + log
    name = name.swapcase()
    print(" %s %s %d" % (name, 'will turn 100 years old in the year ',ans))
    break
  else:
    print("The format is incorrect please reenter \n")



