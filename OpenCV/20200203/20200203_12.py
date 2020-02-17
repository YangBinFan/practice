# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 17:17:57 2020

@author: bck10
"""

import cv2 as cv 
import numpy as np 
img = np.zeros((512, 512, 3), np.uint8) 
img.fill(200) 
pts = np.array([[170,55], [215, 125], [270, 130], [250, 110]], np.int32) 
pts = pts.reshape((-1, 1, 2)) 
cv.polylines(img, [pts], True, (255, 128, 0), 4)
cv.imshow('image', img) 
cv.waitKey()
