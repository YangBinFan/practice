# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 16:20:03 2020

@author: (Dell) Yang-Bin Fan
"""

import cv2 as cv 

img1 = cv.imread(r'C:\Users\bck10\Desktop\OpenCV\material\lena.jpg',1) 
img2 = cv.imread(r'C:\Users\bck10\Desktop\OpenCV\material\lena_01.jpg',1) 
img3 = cv.imread(r'C:\Users\bck10\Desktop\OpenCV\material\tpe101.jpg',1) 

face = img1[120:240,120:240] 
eye = img2[100:160,250:350]
#tpe101 = img3[220:350,200:360]

cv.imshow("image1",img1) 
cv.imshow("face",face) 

cv.imshow("image2",img2) 
cv.imshow("eye",eye) 

#cv.imshow("image3",img3) 
#cv.imshow("tpe10l",tpe101) 


cv.waitKey()
