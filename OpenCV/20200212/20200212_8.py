# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 14:58:26 2020

@author: (Dell) Yang-Bin Fan
"""

import numpy as np 
img = np.random.randint(10,99,size= [5,5],dtype=np.uint8) 
print("before modification img=\n",img) 
print("read pixel img.item(3,2)=",img.item(3,2)) 
img.itemset((3,2),255) 
print("after modification img=\n",img) 
print("after modification img.item(3,2)=",img.item(3,2))
