# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 14:21:25 2020

@author: (Dell) Yang-Bin Fan
"""

import cv2 as cv 

img = cv.imread(r'C:\Users\bck10\Desktop\OpenCV\material\lena_01.jpg',1) 
US1 = cv.imread(r'C:\Users\bck10\Desktop\OpenCV\material\US1_600.jpg',1) 

cv.imshow("image",img) 
cv.imshow("banknote", US1) 

img_face = img[70:230,240:380] 
US1_face = US1[70:230,240:380] 

add = cv.addWeighted(img_face,1, US1_face,0.3,0) 
US1[70:230,240:380] = add 

cv.imshow('result', US1) 
cv.waitKey()
