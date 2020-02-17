# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 12:15:42 2020

@author: (Dell) Yang-Bin Fan
"""

import cv2 as cv 
import numpy as np 
blue = np.zeros((300,300,3),dtype=np.uint8) 
# set blue channel 
blue[:,:,0] = 255 
# all elements 
print("blue = \n",blue) 
cv.imshow("blue",blue) 
green = np.zeros((300,300,3),dtype=np.uint8) 
green[:,:,1] = 255 
print("green = \n",green) 
cv.imshow("green",green) 
red = np.zeros((300,300,3),dtype=np.uint8) 
red[:,:,2] = 255 
print("red = \n",red)
cv.imshow("red",red)




cv.waitKey()
