# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 13:54:26 2020

@author: (Dell) Yang-Bin Fan
"""

import cv2 as cv 
import numpy as np 
img1 = np.ones((3,4,3),dtype=np.uint8)*100 
img2 = np.ones((3,4,3),dtype=np.uint8)*10 
a = 3 
img3 = cv.addWeighted(img1, 0.6, img2, 5, a)
#img1*0.6+img2*5+3
#=100*0.6+10*5+3=60+50+3=113 
print(img3)
