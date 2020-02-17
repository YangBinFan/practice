# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 16:04:15 2020

@author: bck10
"""

import cv2 as cv 

drawing = False 
ix = -1 
iy = -1 

def draw_rectangle(event, x, y, flags, params):
    global ix, iy, drawing 
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y 
    elif event == cv.EVENT_MOUSEMOVE: 
        if drawing == True:
            cv.rectangle(img, (ix, iy), (x,y),(0,0, 255),-1) 
        elif event == cv.EVENT_LBUTTONUP:
            drawing = False
            cv.rectangle(img, (ix, iy), (x,y),(0, 0, 255),-1) 

img = cv.imread(r'C:\Users\bck10\Desktop\OpenCV\material\Lena512.jpg') 
cv.namedWindow(winname = 'my_drawing') 
cv.setMouseCallback('my_drawing', draw_rectangle) 

while True:
    cv.imshow('my_drawing', img) 
    if cv.waitKey(1) & 0xFF == 27:
        break 

cv.destroyAllWindows()
