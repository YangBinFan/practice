# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 14:06:22 2020

@author: (Dell) Yang-Bin Fan
"""

import cv2 as cv 
img = cv.imread(r'C:\Users\bck10\Desktop\OpenCV\material\Hallstatt.jpg') 
cv.imshow("image_before",img) 
print("access img[0,0] = ",img[0,0]) 
print("access img[0,0,0] = ",img[0,0,0]) 
print("access img[0,0,1] = ",img[0,0,1]) 
print("access img[0,0,2] = ",img[0,0,2]) 
print("access img[50,0] = ",img[50,0]) 
print("access img[100,0] = ",img[100,0]) 

for i in range(0,50): # column
    for j in range(0,100): # row
        for k in range(0,3): # channel
                  img[i,j,k] = 255 

for i in range(50,100): 
    for j in range(0,100):
          img[i,j] = [128,128,128]
          
for i in range(100,150): 
    for j in range(0,100):
        img[i,j] = 0 
        
cv.imshow("image_after", img) 
print("after modification img[0,0] = ",img[0,0]) 
print("after modification img[0,0,0] = ", img[0,0,0]) 
print("after modification img[0,0,1] = ",img[0,0,1]) 
print("after modification img[0,0,2] = ", img[0,0,2]) 
print("after modification img[50,0] = ",img[50,0]) 
print("after modification img[100,0] = ", img[100,0]) 
cv.waitKey()
