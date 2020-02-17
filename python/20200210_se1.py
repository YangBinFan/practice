# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 12:05:07 2020

@author: bck10
"""

from selenium import webdriver
import time


li=[]
#num=int(input())
driver = webdriver.Chrome(r'C:\Users\bck10\Anaconda3\share\jupyter\kernels\python3\chromedriver.exe')
driver.get("https://www.ptt.cc/bbs/Gossiping/index.html")
time.sleep(1)



#driver.find_element_by_name('UHSearchBox').send_keys('ptt Gossiping')
#time.sleep(1)
driver.find_element_by_name('yes').click()
time.sleep(1)                                    

first_page=driver.find_elements_by_css_selector('.title a')
for i in first_page[-6::-1]:
    li.append(i.text)
    li.append(i.get_attribute('href'))
    
while len(li)<20:
    driver.find_element_by_css_selector('.wide:nth-child(2)').click()
   # time.sleep(1)
    last_page=driver.find_elements_by_css_selector('.title a')
    for i in last_page[-1::-1]:
        li.append(i.text)
        li.append(i.get_attribute('href'))
        if len(li)==20:break
    
driver.close()
for i in li:
    print(i)
    
    
    


#driver.get()
#driver.close()
#driver.quit()
#driver.back()
#driver.foward()
#driver.refresh()