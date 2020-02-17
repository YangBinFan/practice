# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 16:43:12 2020

@author: bck10
"""

import cv2 as cv 
import numpy as np 
def changecolor(x):
    r = cv.getTrackbarPos('R', 'image') 
    g = cv.getTrackbarPos('G', 'image') 
    b = cv.getTrackbarPos('B', 'image')
    img[:] = [b,g,r] 

img = np.zeros((100,700,3), np.uint8) 
cv.namedWindow('image') 
cv.createTrackbar('R', 'image',0,255,changecolor) 
cv.createTrackbar('G', 'image',0,255,changecolor) 
cv.createTrackbar('B', 'image',0,255,changecolor) 

while(1):
    cv.imshow('image',img) 
    x = cv.waitKey(1) & 0xFF 
    if x == 27: break 

cv.destroyAllWindows()
