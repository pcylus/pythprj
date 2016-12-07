a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print([x for x in a if x<5])
num = [y for y in a if y>10]
print(num)
#print(list(filter(lambda x : x < 5 ,a)))
