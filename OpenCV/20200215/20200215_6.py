# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 10:43:07 2020

@author: (Dell) Yang-Bin Fan
"""

import cv2 as cv 
img_color = cv.imread(r"C:\Users\bck10\Desktop\OpenCV\material\Lena512.jpg") 
img_gray = cv.imread(r"C:\Users\bck10\Desktop\OpenCV\material\lena_01.jpg",0) 
print("properties of img_color :") 
print("img_color.shape = ",img_color.shape) 
print("img_color.size = ",img_color.size) 
print("img_color.dtype = ",img_color.dtype) 
print("properties of img_gray  :") 
print("img_gray.shape = ",img_gray.shape) 
#gray no channel
print("img_gray.size = ",img_gray.size) 
print("img_gray.dtype = ", img_gray.dtype)
