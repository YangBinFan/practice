# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 09:38:04 2020

@author: (Dell) Yang-Bin Fan
"""
class test():
    def __init__(self,data=1):
        self.data = data
# default data=1,change it at test(input),ex:test(3)
    def __next__(self):
        if self.data > 6:
            raise StopIteration
# self.data upper limit,ex:text(4)_4+1=5,5+1=6,6+1=7,ok
# ex:text(5)_5+1=6,6+1=7,ok,7>6 so output with StopIteration
        else:
            self.data+=1
            return self.data

t = test(3)   
for i in range(3):
    print(t.__next__())

