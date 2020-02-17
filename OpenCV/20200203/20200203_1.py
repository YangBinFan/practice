# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 10:23:36 2020

@author: bck10
"""
import cv2

img=cv2.imread(r"C:\Users\bck10\Desktop\OpenCV\material\Lena512.jpg",0)
#cv2.namedWindow("image1")
#cv2.namedWindow("image2")
cv2.imshow("image",img)
cv2.imshow("image2",img)
cv2.waitKey()

cv2.imwrite(r"C:\Users\bck10\Desktop\OpenCV\Lena512.jpg",img)
cv2.destroyAllWindows()
