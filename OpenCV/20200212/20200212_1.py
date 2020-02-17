# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 10:45:04 2020

@author: bck10
"""

import cv2 as cv 
import matplotlib.pyplot as plt 
img = cv.imread(r'C:\Users\bck10\Desktop\OpenCV\material\lena_01.jpg',0) 
ret,thresh1 = cv.threshold(img, 127,255,cv.THRESH_BINARY)
ret,thresh2 = cv.threshold(img, 127,255,cv.THRESH_BINARY_INV) 
ret,thresh3 = cv.threshold(img, 127,255,cv.THRESH_TRUNC) 
ret,thresh4 = cv.threshold(img, 127,255,cv.THRESH_TOZERO) 
ret,thresh5 = cv.threshold(img, 127,255,cv.THRESH_TOZERO_INV) 
titles = ['origin','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV'] 
images = [img,thresh1,thresh2, thresh3, thresh4, thresh5] 
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray') 
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([]) 
    
plt.show()
