# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 00:42:50 2020

@author: Dell
"""
import numpy as np
import cv2
import math
c=.2
gamma=1.5
img = cv2.imread("Lenna.png", cv2.IMREAD_GRAYSCALE)
cv2.imshow("input", img)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        a = img.item(i,j)
        img.itemset((i,j), c*(a**gamma))
cv2.imshow('output image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()