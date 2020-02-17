# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 14:06:34 2020

@author: bck10
"""

import cv2
import numpy as np

img=np.zeros((512,512,3),np.uint8)
# generate a 512*512 column*row block window
cv2.line(img,(0,0),(511,511),(0,0,255),10)
# RGB model (B,G,R)
cv2.imshow('image',img)
cv2.waitKey()
