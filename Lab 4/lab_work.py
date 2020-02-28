# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 11:24:07 2020

@author: csere
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 16:03:21 2020

@author: csere
"""

import numpy as np
import cv2
import math
import matplotlib.pyplot as plt
from tqdm import tqdm

input_img = cv2.imread('einstein.jpg',cv2.IMREAD_GRAYSCALE)
input_img = cv2.resize(input_img, (200,200), interpolation = cv2.INTER_AREA) 

cv2.imshow('input_image',input_img)

input_hist = plt.hist(input_img.ravel(),256,[0,256])[0]

#print(input_hist)

#print(input_hist)
'''
eq_img = cv2.equalizeHist(input_img)

plt.hist(eq_img.ravel(),256,[0,256])
plt.show()
'''

normalized_input_hist = input_hist/(len(input_img)*len(input_img[0]))
plt.hist(normalized_input_hist,256,[0,256])
plt.figure()

cdf_input = []
sum = 0
for i in range(0,256):
    sum = sum+normalized_input_hist[i]
    cdf_input.append(sum)

print(cdf_input)
plt.hist(cdf_input,256,[0,256])[0]
plt.figure()

output_img = input_img.copy()

for i in range(len(input_img)):
    for j in range(len(input_img[0])):
        s = 255*(cdf_input[ input_img[i][j] ])
        output_img[i][j] = s 
        
print(output_img)

output_hist = plt.hist(output_img.ravel(),256,[0,256])[0]
print(output_hist)
normalized_output_hist = output_hist/(len(output_img)*len(output_img[0]))
plt.hist(normalized_output_hist,256,[0,256])
plt.figure()

cdf_output = []
sum = 0
for i in range(0,256):
    sum = sum+normalized_output_hist[i]
    cdf_output.append(sum)

print(cdf_output)
plt.hist(cdf_output,256,[0,256])
plt.figure()
plt.show()


cv2.imshow("output_img",output_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
