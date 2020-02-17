# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 15:23:40 2020

@author: bck10
"""

import cv2 as cv 
import numpy as np 
img = np.zeros((512,512,3), np.uint8) 
cv.circle(img,(44,63), 36, (0,100,255), -1) 
cv.imshow('image',img) 
cv.waitKey()
