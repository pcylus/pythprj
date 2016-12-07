import random
import sys
import os

class animal:
    __name= " "
   # __height= 0
    #__breed = ""

    def __init__(self,name):
      self.__name = name

    def set_name(self,name):
        self.__name = name
    def get_name(self):
        return self.__name
    def go_type(self,name):
        print(name)

cat = animal("cat")



