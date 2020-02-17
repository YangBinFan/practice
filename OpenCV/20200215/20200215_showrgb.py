# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 09:52:16 2020

@author: (Dell) Yang-Bin Fan
"""

import cv2 as cv 
img = cv.imread(r"C:\Users\bck10\Desktop\OpenCV\material\Lena512.jpg") 
cv.imshow('image',img) 
b = img[:,:,0] 
g = img[:,:,1] 
r = img[:,:,2] 
cv.imshow('b',b) 
cv.imshow('g',g) 
cv.imshow('r',r) 
img[:,:,0] = 0 
cv.imshow('imgb0',img) 
img[:,:,1] = 0 
cv.imshow('imgg0',img) 
img[:,:,2] = 0 
cv.imshow('imgro',img) 
cv.waitKey()
