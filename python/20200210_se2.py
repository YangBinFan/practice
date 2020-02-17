# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 15:38:40 2020

@author: bck10
"""

from selenium import webdriver
import time

driver = webdriver.Chrome(r'C:\Users\bck10\Anaconda3\share\jupyter\kernels\python3\chromedriver.exe')
driver.get("https://www.ptt.cc/ask/over18?from=%2Fbbs%2FGossiping%2Findex.html")
time.sleep(1)

driver.find_element_by_name('yes').click()


js='window.open("https://www.ptt.cc/bbs/Gossiping/M.1581322900.A.683.html");'                                    
driver.execute_script(js)

