# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 11:37:37 2020

@author: Shourav Paul
"""

import numpy as np
import math
import cv2
from matplotlib import pyplot as plt

img= cv2.imread("lena.png", 0)
img1 = cv2.imread("lena.png", 0)
cv2.imshow('input', img)
print(img)
hist = cv2.calcHist([img],[0],None,[256],[0,256])
plt.hist(img.ravel(),256,[0,256])
plt.show()

d = img.max()
c = img.min()
print(c)
print(d)

kernel1 = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])  
kernel2 = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])     

k1 = int(3/2)
k2 = int(3/2)       
m=3
n=3  
print(kernel1)
summ = sum(sum(kernel1))
print("summ ",summ)
height = img.shape[0]
width = img.shape[1]
image_arr = np.zeros((height+m-1, width+n-1), dtype=float)
image_arr[k1:height+k1, k2:width+k2] = img
print(image_arr)
ab1 = np.zeros((height, width), dtype=float)
ab2 = np.zeros((height, width), dtype=float)

for i in range(k1,height):
    for j in range(k2,width):
        image_value1 = []
        image_value2 = []
        for u in range(-k1,k1+1):
            for v in range(-k2,k2+1):
                image_value1.append(image_arr[i-u][j-v]*kernel1[u+k1][v+k2])
                image_value2.append(image_arr[i-u][j-v]*kernel2[u+k1][v+k2])
        ab1[i-k1][j-k2] = float(sum(image_value1))
        ab2[i-k1][j-k2] = float(sum(image_value2))

mx = ab1.max()-1
mn = ab1.min()-1
for i in range(height):
    for j in range(width):
        r = ab1[i][j]
        img[i][j] = ((r-mn)/(mx-mn))*255

mx = ab2.max()-1
mn = ab2.min()-1
for i in range(height):
    for j in range(width):
        r = ab2[i][j]
        img1[i][j] = ((r-mn)/(mx-mn))*255

cv2.imshow('sobel_output', img)
cv2.imshow('sobel_output no 2', img1)


hist = cv2.calcHist([img],[0],None,[256],[0,256])
plt.hist(img.ravel(),256,[0,256])
plt.show()
print(img)
     
cv2.waitKey(0)
cv2.destroyAllWindows()

