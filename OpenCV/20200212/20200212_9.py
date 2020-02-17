# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 15:20:19 2020

@author: (Dell) Yang-Bin Fan
"""

import numpy as np 
import cv2 as cv 
img = np.random.randint(0,256,size=[256,256],dtype=np.uint8) 
cv.imshow("image", img) 
cv.waitKey()
