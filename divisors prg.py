#Create a program that asks the user for a number and then prints out a list of all the divisors of that number
#Program using for loop
num = int(input("Enter a number"))
li = list()
"""for x in range(2,num):
    if(num%x==0):
     li.append(x)
print(li)"""

#program using iterators
def divisors():
    li =[x for x in range(2,num) if num%x==0]
    return li

print(divisors())





