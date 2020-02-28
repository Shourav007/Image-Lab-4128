# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 01:43:27 2020

@author: Shourav Paul
"""

import numpy as np
import math
import cv2
from matplotlib import pyplot as plt

img1= cv2.imread("lena.png", 0)
img2= cv2.imread("lena.png", 0)
img3= cv2.imread("lena.png", 0)
img4= cv2.imread("lena.png", 0)
cv2.imshow('input', img1)
print(img1)
hist = cv2.calcHist([img1],[0],None,[256],[0,256])
plt.hist(img1.ravel(),256,[0,256])
plt.show()

d = img1.max()
c = img1.min()
print(c)
print(d)

kernel1 = np.array([[0,1,0],[1,-4,1],[0,1,0]])      
kernel2 = np.array([[1,1,1],[1,-8,1],[1,1,1]])
kernel3 = np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])  
kernel4 = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]) 
k1 = int(3/2)
k2 = int(3/2)       
m=3
n=3  
print(kernel1)
summ = sum(sum(kernel1))
print("summ ",summ)
height = img1.shape[0]
width = img1.shape[1]
image_arr = np.zeros((height+m-1, width+n-1), dtype=float)
image_arr[k1:height+k1, k2:width+k2] = img1
print(image_arr)
ab1 = np.zeros((height, width), dtype=float)
ab2 = np.zeros((height, width), dtype=float)
ab3 = np.zeros((height, width), dtype=float)
ab4 = np.zeros((height, width), dtype=float)
for i in range(k1,height):
    for j in range(k2,width):
        image_value1 = []
        image_value2 = []
        image_value3 = []
        image_value4 = []
        for u in range(-k1,k1+1):
            for v in range(-k2,k2+1):
                image_value1.append(image_arr[i-u][j-v]*kernel1[u+k1][v+k2])
                image_value2.append(image_arr[i-u][j-v]*kernel2[u+k1][v+k2])
                image_value3.append(image_arr[i-u][j-v]*kernel3[u+k1][v+k2])
                image_value4.append(image_arr[i-u][j-v]*kernel4[u+k1][v+k2])
        ab1[i-k1][j-k2] = float(sum(image_value1))
        ab2[i-k1][j-k2] = float(sum(image_value2))
        ab3[i-k1][j-k2] = float(sum(image_value3))
        ab4[i-k1][j-k2] = float(sum(image_value4))

mx = ab1.max()-1
mn = ab1.min()-1
for i in range(height):
    for j in range(width):
        r = ab1[i][j]
        img1[i][j] = ((r-mn)/(mx-mn))*255

cv2.imshow('laplacian_output 1', img1)

mx = ab2.max()-1
mn = ab2.min()-1
for i in range(height):
    for j in range(width):
        r = ab2[i][j]
        img2[i][j] = ((r-mn)/(mx-mn))*255

cv2.imshow('laplacian_output 2', img2)

mx = ab3.max()-1
mn = ab3.min()-1
for i in range(height):
    for j in range(width):
        r = ab3[i][j]
        img3[i][j] = ((r-mn)/(mx-mn))*255

cv2.imshow('laplacian_output 3', img3)

mx = ab4.max()-1
mn = ab4.min()-1
for i in range(height):
    for j in range(width):
        r = ab4[i][j]
        img4[i][j] = ((r-mn)/(mx-mn))*255

cv2.imshow('laplacian_output 4', img4)

hist = cv2.calcHist([img1],[0],None,[256],[0,256])
plt.hist(img1.ravel(),256,[0,256])
plt.show()
plt.hist(img2.ravel(),256,[0,256])
plt.show()
plt.hist(img3.ravel(),256,[0,256])
plt.show()
plt.hist(img4.ravel(),256,[0,256])
plt.show()

     
cv2.waitKey(0)
cv2.destroyAllWindows()
