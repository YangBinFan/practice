# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 17:02:55 2020

@author: (Dell) Yang-Bin Fan
"""

import cv2 as cv 
import numpy as np 
img = cv.imread(r'C:\Users\bck10\Desktop\OpenCV\material\lena512.jpg',1) 
w,h,x= img.shape 
# has to be three returns
mask = np.zeros((w,h),dtype = np.uint8) 
mask[100:400,200:400] = 255 
mask[100:500,100:200] = 255 
c = cv.bitwise_and(img,img, mask=mask) 
print('img.shape = ',img.shape) 
print('mask.shape = ',mask.shape) 
cv.imshow('img', img) 
cv.imshow('mask',mask) 
cv.imshow('c',c) 
cv.waitKey()
