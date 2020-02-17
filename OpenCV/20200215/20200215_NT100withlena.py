# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 16:37:56 2020

@author: (Dell) Yang-Bin Fan
"""
import cv2 as cv 
img = cv.imread(r"C:\Users\bck10\Desktop\OpenCV\material\lena.jpg",1) 
NT100 = cv.imread(r"C:\Users\bck10\Desktop\OpenCV\material\NT100.jpg",1) 
cv.imshow("image", img) 
cv.imshow("banknote",NT100) 
face = img[140:240,140:220] 
NT100[30:130,60:140] = face 
cv.imshow("final", NT100) 
cv.waitKey()
