# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 16:41:22 2020

@author: bck10
"""

import cv2 as cv 
import numpy as np 
img = np.zeros((512, 512,3), np.uint8) 
img.fill(200) 
cv.ellipse(img, (180, 200), (100, 60), 45, 0, 360, (128, 0, 255), 2) 
cv.ellipse(img, (180, 200), (50, 100), 45, 0, 180, (255, 0, 128), -1) 
cv.imshow('image', img) 
cv.waitKey()
