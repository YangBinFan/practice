# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 13:45:51 2020

@author: (Dell) Yang-Bin Fan
"""

import cv2 as cv 
import numpy as np 
img1 = np.zeros((300,300,3),dtype=np.uint8) 

img1[:,0:100,0] = 255 
img1[:,100:200] = 255 
img1[:,200:300,2] = 255 

print("img1 = \n", img1) 
cv.imshow("French_image1",img1) 

img2 = np.zeros((300,300,3),dtype=np.uint8) 

img2[0:100,:,0] = 0 
img2[100:200,:,2] = 255 
img2[200:300,:,1] = 255 
img2[200:300,:,2] = 255
print("img2 = \n", img2) 
cv.imshow("Germany_image2",img2) 

img3 = np.zeros((300,300,3),dtype=np.uint8) 

img3[:,0:100,1] = 200 
img3[:,100:200] = 255 
img3[:,200:300,2] = 255 
#row
print("img3 = \n", img3) 
cv.imshow("Italy_image3",img3) 

img4 = np.zeros((300,300,3),dtype=np.uint8) 

img4[:,0:100,0] = 255 
img4[:,100:200,1] = 255 
img4[:,200:300,2] = 255 
#row
print("img4 = \n", img4) 
cv.imshow("image4",img4) 

cv.waitKey()
