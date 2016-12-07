import random
import sys
import os


test_file = open("test.txt", 'wb')
test_file.write("this is the first text in the file\n")
print(test_file.name)
test_file.close()

test_file = open("test.txt", 'r+')
rem = test_file.read()
print(rem)

os.remove('test.txt')

