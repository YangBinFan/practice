# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 14:58:08 2020

@author: bck10
"""

import cv2 as cv 
import numpy as np 

n = 300 
img = np.ones((n,n,3), np.uint8)*255 
img = cv.rectangle(img, (50,50), (n-100,n-100),(0,0,120),-1)
img = cv.rectangle(img, (50,50), (n-100,n-100),(200,200,200),20) 
cv.imshow("image",img) 
cv.waitKey()
