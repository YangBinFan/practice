# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 16:13:35 2020

@author: (Dell) Yang-Bin Fan
"""

import cv2 as cv 
import numpy as np 
img = np.random.randint(0,256,size= [256,256,3],dtype=np.uint8) 
cv.imshow("image",img) 
cv.waitKey()
