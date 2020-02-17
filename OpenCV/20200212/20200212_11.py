# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 15:59:06 2020

@author: (Dell) Yang-Bin Fan
"""

import numpy as np 
img = np.random.randint(10,99, size=[2,4,3],dtype=np.uint8) 
print("before modified img=\n", img) 
print("read pixel points img[1,2,0]=",img.item(1,2,0)) 
print("read pixel points img[0,2,1]=",img.item(0,2,1)) 
print("read pixel points img(1,0,2]=",img.item(1,0,2)) 
img.itemset((1,2,0),255) 
img.itemset((0,2,1),255) 
img.itemset((1,0,2),255) 
print("after modified img=\n", img) 
print("modified pixel points img[1,2,0]=",img.item(1,2,0)) 
print("modified pixel points img[0,2,1]=",img.item(0,2,1)) 
print("modified pixel points img[1,0,2]=",img.item(1,0,2))
