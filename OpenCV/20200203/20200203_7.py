# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 15:39:24 2020

@author: bck10
"""

import cv2 as cv 
import numpy as np 

img = np.zeros((512,512,3),dtype="uint8") 

for r in range(0,175,25):
    cv.circle(img,(img.shape[1] //2,img.shape[0] // 2),r,(255,255,255))
#[0]:horizontal size / [1]:vertical size
cv.imshow('image',img) 
cv.waitKey()
