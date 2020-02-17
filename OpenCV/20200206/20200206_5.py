# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 11:39:54 2020

@author: bck10
"""

from PIL import ImageFont, ImageDraw, Image 

import cv2 as cv 
import numpy as np 
img = np.zeros((512,512,3), np.uint8) 
img.fill(64) 
img[:] = (0,0,192) 
text ='恭賀\n新囍' 
fontPath = r'C:\Users\bck10\Desktop\OpenCV\material\TaipeiSansTCBeta-Bold.TTF'
font = ImageFont.truetype(fontPath, 224) 
imgPil = Image.fromarray(img) 
draw = ImageDraw.Draw(imgPil) 
draw.text((30, 30), text, font = font, fill = (0,0,0,0)) 
img = np.array(imgPil) 
cv.imshow('image', img) 
cv.waitKey()
