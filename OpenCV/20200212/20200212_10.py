# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 15:43:25 2020

@author: (Dell) Yang-Bin Fan
"""

import cv2 as cv 

img = cv.imread(r'C:\Users\bck10\Desktop\OpenCV\material\Hallstatt.jpg',0) 

print("read pixel points img.item(3,2)=",img.item(3,2)) 
img.itemset((3,2),255) 
print("pixel points after modified img.item(3,2)=",img.item(3,2)) 
cv.imshow("before", img) 
for i in range(10,100): 
    for j in range(80,100):
        img.itemset((i,j),255) 

cv.imshow("after",img) 
cv.waitKey()
