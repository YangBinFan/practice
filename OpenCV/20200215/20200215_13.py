# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 15:46:51 2020

@author: (Dell) Yang-Bin Fan
"""

import cv2 as cv 
import numpy as np 

img1 = np.random.randint(0,255,(5,5),dtype=np.uint8) 
#size(5,5) grayscale is because of only two coordinates
img2 = np.zeros((5,5),dtype=np.uint8) 
#size(5,5) all zeros grayscale is because of only two coordinates
# [col,row]
img2[0:3,0:3] = 255
img2[4,4] = 255 
#The region are 1 and this point is 1,but others are 0
a = cv.bitwise_and(img1,img2) 
#by this operation, 1 are remained, 0 are zeros
print("img1 = \n", img1) 
print("img2 = \n", img2) 
print("a = \n", a)
