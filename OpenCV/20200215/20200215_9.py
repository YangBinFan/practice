# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 12:10:21 2020

@author: (Dell) Yang-Bin Fan
"""

import cv2 as cv 
img = cv.imread(r'C:\Users\bck10\Desktop\OpenCV\material\Lena512.jpg',0) 
a = img 
result1 = a + img 
result2 = cv.add(img, a) 
cv.imshow('image',img) 
cv.imshow('imagel',result1)
#加法運算子，>255取mod 256，值變小，影像整體變按
cv.imshow('image2',result2) 
#add()函數，飽和值255，值變大，影像整體變亮
cv.waitKey()
