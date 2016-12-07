import random
import sys
import os

grocery_list = ['Juice','tomatoes','milk','coco']
todo_list = ['prog', 'license']

things_list = [grocery_list,todo_list]
todo_list.insert(2,'doctor')
todo_list.remove('license')
grocery_list.append("chocolates")
del grocery_list[3]
print(len(things_list))
print(things_list)
print(max(todo_list))
print(min(grocery_list))

