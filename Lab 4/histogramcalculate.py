# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 11:19:11 2020

@author: Dell
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('lena.png', cv2.IMREAD_GRAYSCALE)
img1 = cv2.imread('lena.png', cv2.IMREAD_GRAYSCALE)
img2 = np.zeros((img.shape[0], img.shape[1]), dtype="uint8")
cv2.imshow('input image',img)

plt.hist(img.ravel(),256,[0,255])
plt.show()

n = np.zeros((256), dtype=float)
p = np.zeros((256), dtype=float)
s = np.zeros((256), dtype=int)
cum = np.zeros((256), dtype=float)
z = img.shape[0]*img.shape[1]
x = 0

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        n[img[i][j]]=n[img[i][j]]+1
'''        
print("pixel count")        
for i in range(256):
    print('pixel ',i,'= value',n[i])
'''    
for i in range(0,256):
    p[i]=n[i]/(z)
    x = x+p[i]
    cum[i]=p[i]
    s[i]=round(255*x) #(L-1)=255

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        val = img[i][j]
        img.itemset((i,j),s[val])


plt.hist(list(range(255)),p)
plt.hist(img.ravel(),255,[0,255])
plt.show()     
cv2.imshow('output image', img)
print(img)
print(img1)
cv2.waitKey(0)
cv2.destroyAllWindows()