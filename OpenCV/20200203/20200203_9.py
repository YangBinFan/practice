# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 16:10:23 2020

@author: bck10
"""

import cv2 as cv 
import numpy as np 
img = np.zeros((512,512,3),dtype="uint8") 

for i in range(0,50):
    radius = np.random.randint(5,high = 20) 
    #半徑
    color = np.random.randint(0, high = 256,size = (3,)).tolist() 
    #顏色 ex:[215, 232, 173]
    #pt = np.random.randint(0,high = 512,size = (2,))
    #cv.circle(img, tuple(pt),radius,color,-1)
    cv.circle(img,radius,color,-1) 

cv.imshow('image',img) 
cv.waitKey()
