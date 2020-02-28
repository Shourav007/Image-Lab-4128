# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 10:28:03 2020

@author: Dell
"""

import cv2
import numpy as np
import math

v1 = [0,0,0,0,0,0,0]
v2 = [0,0,0,0,0,0,0]


sigma = 3.25

for i in range(7):
    v1[i] = (1/(2*3.1416*sigma))*(math.exp(-((math.pow(i-3, 2))+(math.pow(i-3, 2)))/(2*sigma)))
    
print(v)
c = [0,0,0,0,0,0,0]
for i in range(7):
    c[i] = round(v1[i]/v1[0])
    
    
print(c)

from scipy.linalg import toeplitz
v1 = toeplitz(c)
print(v1)
