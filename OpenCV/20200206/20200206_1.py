# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 09:40:11 2020

@author: bck10
"""

import cv2 as cv 
import numpy as np 
img1 = np.zeros((512,512,3), np.uint8) 
img2 = np.zeros((512,512,3), np.uint8)

font = cv.FONT_HERSHEY_SIMPLEX 
cv.putText(img1,'OpenCV',(10,350), font, 4,(255,255,255),2,cv.LINE_AA)
 
cv.putText(img2,'OpenCV',(10,350), font, 4,(255,255,255),2) 
#斜線的部分有反鋸齒
cv.imshow('image1', img1)
cv.imshow('image2', img2) 
cv.waitKey()


