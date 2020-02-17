# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 16:28:00 2020

@author: (Dell) Yang-Bin Fan
"""

import cv2 as cv 
import numpy as np 

img1 = cv.imread(r'C:\Users\bck10\Desktop\OpenCV\material\lena512.jpg',0) 
img2 = np.zeros(img1.shape,dtype=np.uint8) 

img2[100:400,200:400] = 255 
img2[100:500,100:200] = 255 

a = cv.bitwise_or(img1,img2) 
cv.imshow("img1",img1) 
cv.imshow("img2",img2) 
cv.imshow("a",a) 
cv.waitKey()
