# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 14:04:24 2020

@author: (Dell) Yang-Bin Fan
"""

import cv2 as cv 

img1 = cv.imread(r'C:\ ....... \\landscape512.jpg') 
img2 = cv.imread(r'C:\...... \\Lena512.jpg') 

result = cv.addWeighted (img1,0.6,img2,0.4,0) 

cv.imshow('image1',img1) 
cv.imshow('image2',img2) 
cv.imshow('image3',result) 
cv.waitKey()
