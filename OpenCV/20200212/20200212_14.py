# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 17:01:16 2020

@author: (Dell) Yang-Bin Fan
"""

import cv2 as cv 
import numpy as np 
img = cv.imread(r'C:\Users\bck10\Desktop\OpenCV\material\Lena512.jpg',1) 
cv.imshow("image",img) 
face = np.random.randint(0,256,(180,160,3)) 
img[220:400,200:360] = face 
#400-220=180,360-200=160
cv.imshow("result",img) 
cv.waitKey()
