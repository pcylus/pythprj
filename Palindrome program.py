import random
import sys
"""num = list(input("Please provide an input to check wheather it is a palindrome or not \n"))
rev = list(reversed(num))
if num == rev:
    print('Yes it is a palindrome')
else:
    print("Nope it is not a palindrome")

"""
#secondary approach
string = (input("Put in your text")).lower()
'''revstring = string[::-1]
print(revstring)
if string == revstring:
  print("A palindrome")
'''
#another approach
rev = ""
for i in string[::-1]:
    rev = rev+i
print(rev)
if string == rev:
    print("its a palindrome")
else:
    print('its is not a palindrome')



