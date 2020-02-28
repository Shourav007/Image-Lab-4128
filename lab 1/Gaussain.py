import cv2
import numpy
import math

n = int(input("Enter kernel size x: "))
m = int(input("Enter kernel size y: "))

kernel = numpy.zeros((m, n), dtype=float)
sigma = float(input("Enter sigma value: "))

sigma = math.pow(sigma, 2)
x = int(m/2)
y = int(n/2)

for a in range(m):
    for b in range(n):
        kernel[a][b] = input("Enter the values :")
summ=numpy.sum(kernel)
        
 
img = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow("Gaussian_original", img)       
       #kernel = (1/(2*3.1416*sigma))*(math.exp(-((math.pow(a-x, 2))+(math.pow(b-y, 2)))/(2*sigma)))

#summ = numpy.sum(kernel)
'''

height = img.shape[0]
width = img.shape[1]
image_arr = numpy.zeros((height+n-1, width+m-1), dtype=float)
image_arr[0:height, 0:width] = img

'''
cv2.imshow('Gaussian_output', img)
cv2.waitKey(0)
cv2.destroyAllWindows()





