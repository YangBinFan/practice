# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 10:10:27 2020

@author: (Dell) Yang-Bin Fan
"""

import cv2 as cv 
img = cv.imread(r"C:\Users\bck10\Desktop\OpenCV\material\Lena512.jpg") 
#分
b = cv.split(img)[0]
g = cv.split(img)[1] 
r = cv.split(img)[2]
#b,g,r = cv.split(img)
cv.imshow('B',b) 
cv.imshow('G',g) 
cv.imshow('R',r) 
cv.waitKey()
