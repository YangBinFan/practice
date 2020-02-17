# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 10:40:44 2020

@author: bck10
"""

import cv2 as cv 
import numpy as np 
d = 400 
img = np.ones((d,d,3),dtype="uint8")*255 
font = cv.FONT_HERSHEY_SIMPLEX 
cv.putText(img, 'OpenCV',(0,200),font,3,(0,255,0),15) 
cv.putText(img, 'OpenCV',(0,200),font,3,(0,0,255),5) 
cv.imshow("image",img) 
cv.waitKey()
