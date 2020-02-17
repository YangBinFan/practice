# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 11:31:36 2020

@author: (Dell) Yang-Bin Fan
"""

import cv2 as cv 
import numpy as np 
img = np.zeros((8,8),dtype=np.uint8) 
#generate a 8*8 all black image by numpy
print("image=",img) 

cv.imshow("one",img) 
print("Read pixel points img[0,3]=",img[0,3]) 
img[0,3]=255 
#img[col,row]

print("After modification img=\n", img) 
print("Pixel points after modification img[0,3]=",img[0,3]) 
cv.imshow("two",img) 
cv.waitKey()
