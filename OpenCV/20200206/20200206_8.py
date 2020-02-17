# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 15:13:32 2020

@author: bck10
"""

import cv2 as cv 
import numpy as np 

drawing = False 
mode = True 
ix,iy = -1,-1 
#滑鼠
def draw_circle(event,x,y,flags,param):
    global ix,iy, drawing, mode 
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True 
        ix,iy = x,y 
    elif event == cv.EVENT_MOUSEMOVE: 
        if drawing == True: 
            if mode == True:
                cv.rectangle(img, (ix,iy),(x,y),(0,255,0),-1) 
            else:
                cv.circle(img, (x,y),5,(0,0,255),-1) 
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False 
        if mode == True:
            cv.rectangle(img, (ix,iy) (x,y),(0,255,0),-1) 
        else:
            cv.circle(img, (x,y),5,(0,0,255),-1) 

#img = np.zeros((512,512,3), np.uint8)

img = cv.imread(r'C:\Users\bck10\Desktop\OpenCV\material\Lena512.jpg')  

cv.namedWindow('image') 
cv.setMouseCallback('image',draw_circle) 
#鍵盤
while(1):
    cv.imshow('image',img) 
    k = cv.waitKey(1) & 0xFF 
    if k == ord('m'):
        mode = not mode 
    elif k == 27:
        break 
    
cv.destroyAllWindows()
