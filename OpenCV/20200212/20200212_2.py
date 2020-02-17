# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 11:15:47 2020

@author:(Dell) Yang-Bin Fan
"""

import cv2 as cv 

Type = 0 
Value = 0 

def onType(a):
    Type = cv.getTrackbarPos(tType,windowName) 
    Value = cv.getTrackbarPos(tValue,windowName) 
    ret, dst = cv.threshold(o, Value, 255, Type)
    cv.imshow(windowName,dst) 
def onValue(a):
    Type = cv.getTrackbarPos(tType,windowName) 
    Value = cv.getTrackbarPos(tValue, windowName) 
    ret, dst = cv.threshold(o, Value, 255, Type)
    cv.imshow(windowName,dst) 

o = cv.imread(r'C:\Users\bck10\Desktop\OpenCV\material\lena_01.jpg',0) 

windowName = 'image' 
cv.namedWindow(windowName) 
cv.imshow(windowName,o) 

tType = "Type" 
tValue = "Value" 

cv.createTrackbar(tType, windowName,0,4,onType) 
cv.createTrackbar(tValue,windowName,0,255,onValue) 

if cv.waitKey() == 27:
    cv.destroyAllWindows()
