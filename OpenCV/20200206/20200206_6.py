# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 13:51:00 2020

@author: bck10
"""
import cv2
events = [i for i in dir(cv2) if 'EVENT' in i]
print (events)
