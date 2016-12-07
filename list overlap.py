#write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
#  Make sure your program works on two lists of different sizes.
import random
"""a = [random.randrange(1,101) for i in range(random.randrange(3,20))]
b = [random.randrange(1,101) for i in range(random.randrange(3,20))]
print(sorted(a))
print(sorted(b))
print(list(set(a+b)))
"""

#Another approach
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
a.extend(b)
print(a)
print(list(set(a)))



'''a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#li = list(set(a+b))

#creates a set which has mutiples entries of a list grouped as one which are mutable
a =  set(a)
b = frozenset(b) # imutable set

a.add(12)
#b.remove(1)  -- items cannot be changed not added nor removed
#remoes the common elements between two sets
#print(a.difference_(b))
print(a)
#creates a back up of the set
a_backup = a.copy()
a.clear()
print(a_backup)
print(a_backup.intersection(b))
'''