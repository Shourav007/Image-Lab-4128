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
cv2.imshow('input', img)
print(img)
hist = cv2.calcHist([img],[0],None,[256],[0,256])
plt.hist(img.ravel(),256,[0,256])
plt.show()

d = img.max()
c = img.min()
print(c)
print(d)

n = int(input("Enter kernel size x: "))
m = int(input("Enter kernel size y: "))


kernel = np.zeros((m, n), dtype=float)        
sigma = float(input("Enter sigma value: ")) 
sigma = math.pow(sigma, 2)
k1 = int(m/2)
k2 = int(n/2)       
  
for a in range(m):
    for b in range(n):
        kernel[a][b] = (1/(2*3.1416*sigma))*(math.exp(-((math.pow(a-k1, 2))+(math.pow(b-k2, 2)))/(2*sigma)))

print(kernel)
summ = sum(sum(kernel))
print("summ ",summ)
height = img.shape[0]
width = img.shape[1]
image_arr = np.zeros((height+m-1, width+n-1), dtype=float)
image_arr[k1:height+k1, k2:width+k2] = img
print(image_arr)
ab = []

for i in range(k1,height):
    for j in range(k2,width):
        image_value = []
        for u in range(-k1,k1+1):
            for v in range(-k2,k2+1):
                image_value.append(image_arr[i-u][j-v]*kernel[u+k1][v+k2])
                
        s = sum(image_value)
        img[i-k1][j-k2] = float(s/summ)
        


cv2.imshow('Gaussian_output', img)
#cv2.imshow('Gaussian_output no 2', image_arr)


hist = cv2.calcHist([img],[0],None,[256],[0,256])
plt.hist(img.ravel(),256,[0,256])
plt.show()
print(img)
     
cv2.waitKey(0)
cv2.destroyAllWindows()

