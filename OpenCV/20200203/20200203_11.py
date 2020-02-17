# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 16:54:21 2020

@author: bck10
"""

import cv2 as cv 
import numpy as np 

d = 400 

img = np.ones((d,d,3),dtype="uint8")*255 

center = (round(d/2),round(d/2))

size = (100,200)
 
for i in range(0,10):
    angle = np.random.randint(0,361) 
    color = np.random.randint(0, high = 256,size = (3,)).tolist() 
    thickness = np.random.randint(1,9)
    cv.ellipse(img, center,size,angle,0,360,color,thickness) 
cv.imshow("image",img) 
cv.waitKey()
