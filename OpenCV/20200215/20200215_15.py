# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 16:43:00 2020

@author: (Dell) Yang-Bin Fan
"""

import cv2 as cv 
import numpy as np 
img1 = np.ones((4,4),dtype = np.uint8)*3 
img2 = np.ones((4,4),dtype = np.uint8)*5 
mask = np.zeros((4,4),dtype = np.uint8) 
mask[2:4,2:4] = 1 
img3 = np.ones((4,4),dtype = np.uint8)*66 
print('img1 = \n', img1) 
print('img2 = \n',img2) 
print('mask = \n',mask) 
print('initial value img3 = \n',img3) 
img3 = cv.add(img1,img2,mask = mask) 
print('after adding img3 = \n',img3)
