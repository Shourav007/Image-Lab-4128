# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 11:06:02 2020

@author: paulShourav
"""

import numpy as np
import math
import cv2
from matplotlib import pyplot as plt

c=32
img= cv2.imread("gonjalez.jpg", 0)
cv2.imshow('input', img)
print(img)
hist = cv2.calcHist([img],[0],None,[256],[0,256])
plt.hist(img.ravel(),256,[0,256])
plt.show()

r1 = input("r1:  ")
r1=int(r1)
s1 = input("s1:  ")
s1=int(s1)
#r1 is the lowest value in the image that we can see form the img.min()
#and s1 is the value that we want to strech from so it can be 0
r2 = input("r2:  ")
r2=int(r1)
s2 = input("s2:  ")
s2=int(s1)
#r2 is the Largest value in the image that we can see form the img.max()
#and s2 is the value that we want to strech to so it can be 255
#r1=r2=m is the mean = 113 is the value that gives highest level of contrast 
#streching
d = img.max()
c = img.min()
print(c)
print(d)
s=0
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        r = img.item(i,j)
        if r<r1:
            s=(s1/r1)*r
            img.itemset((i,j),s)
        elif r>r1 and r<r2:
            s=((s2-s1)/(r2-r1))*(r-r1) + s1
            img.itemset((i,j),s)
        else:
            s=((255-s2)/(255-r2))*(r-r2) + s2
            img.itemset((i,j),s)
        
  

hist = cv2.calcHist([img],[0],None,[256],[0,256])
plt.hist(img.ravel(),256,[0,256])
plt.show() 
cv2.imshow('output', img)     
'''
x = math.log2(256)
print(x)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        r = img.item(i,j)+1
        s = c*(math.log2(r))
        img.itemset((i,j),s)

cv2.imshow('output', img)
'''
cv2.waitKey(0)
cv2.destroyAllWindows()