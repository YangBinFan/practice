# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 10:43:08 2020

@author: (Dell) Yang-Bin Fan
"""
import cv2 as cv

img = cv.imread(r"C:\Users\bck10\Desktop\OpenCV\material\Lena512.jpg") 
b,g,r = cv.split(img) 
bgr = cv.merge([b,g,r]) 
rgb = cv.merge([r,g,b]) 
cv.imshow('image',img) 
cv.imshow('bgr',bgr) 
cv.imshow('rgb',rgb) 
cv.waitKey()
