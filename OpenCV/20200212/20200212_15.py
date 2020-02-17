# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 17:15:09 2020

@author: (Dell) Yang-Bin Fan
"""
import cv2 as cv 
#import numpy as np 
img1 = cv.imread(r'C:\Users\bck10\Desktop\OpenCV\material\lena.jpg',1) 
img2 = cv.imread(r'C:\Users\bck10\Desktop\OpenCV\material\NT100.jpg',1) 


img2[55:155,30:130]=img1[140:240,140:240]
# position coordinate with Microsoft Paint first 
cv.imshow("image2",img2) 
cv.waitKey()