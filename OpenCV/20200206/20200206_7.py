# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 14:20:15 2020

@author: bck10
"""

import cv2 as cv 
import numpy as np 

def draw_circle(event,x,y,flags,param): 
  if event == cv.EVENT_LBUTTONDBLCLK:
      cv.circle(img,(x,y),10,(255,0,0),1) 

img = np.zeros((512,512,3), np.uint8)   
cv.namedWindow('image') 
cv.setMouseCallback('image',draw_circle) 

while(1):
    cv.imshow('image',img)
    if cv.waitKey(1) & 0xFF == 27:
        break 

cv.destroyAllWindows()
