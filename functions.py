import random
import sys
import os

def add(num1, num2):
    sumv = num1+num2
    return sumv
def multi(num1, num2):
    mul = num1 * num2
    return mul

print("enter operation add or multiply")
opr = input()
if(opr == add):
    print('enter the two numbers to add\nadd')
    num1 = input()
    num2 = input()
    print(add(num1,num2))
elif(opr == multi ):
    print('enter the two numbers to multiply')
    num1= input()
    num2 = input()
    print(multi(num1,num2))

