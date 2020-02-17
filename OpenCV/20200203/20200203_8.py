# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 15:52:17 2020

@author: bck10
"""

import cv2 as cv 
import numpy as np 

d = 400 
img = np.ones((d,d,3),dtype="uint8")*255 

(centerX,centerY) = (round(img.shape[1]/2), round(img.shape[0]/2)) 

red = (5,5,5) 
for r in range(5,round(d/2),12):
    cv.circle(img, (centerX,centerY),r,red, 3) 
cv.imshow("image",img) 
cv.waitKey()
