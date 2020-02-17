# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 15:32:52 2020

@author: (Dell) Yang-Bin Fan
"""

import cv2 as cv 
img = cv.imread(r'C:\Users\bck10\Desktop\OpenCV\material\Hallstatt.jpg',0) 
cv.imshow("before",img) 

for i in range(10,100): 
    for j in range(80,100):
        img[i,j] = 255 

cv.imshow("after",img) 
cv.waitKey()
