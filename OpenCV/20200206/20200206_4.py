# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 10:52:25 2020

@author: bck10
"""

import cv2 as cv 
import numpy as np 
d = 400 
img1 = np.ones((d,d,3), dtype="uint8")*255
img2 = np.ones((d,d,3), dtype="uint8")*255 
font = cv.FONT_HERSHEY_SIMPLEX 
cv.putText(img1, 'OpenCV',(20,150),font,3,(0,0,255),15,cv.LINE_AA) 
cv.putText(img1, 'OpenCV',(20,220),font,3,(0,255,0),15,cv.FONT_HERSHEY_SCRIPT_SIMPLEX,True) 
cv.putText(img2, 'OpenCV',(20,220),font,3,(0,255,0),15,True) 
cv.imshow("image1",img1)
cv.imshow("image2",img2)
cv.waitKey()
