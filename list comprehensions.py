#Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#length appraoch
lst =[]
for x in a:
  if x%2 == 0:
        lst.append(x)
print(lst)

#single line approach
print([x for x in a if x%2==0])

#another approach
print(list(filter(lambda x: x%2==0 ,a)))