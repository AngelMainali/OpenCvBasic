import cv2 as cv
import numpy as np

img=cv.imread(r'C:\Users\Dell\Downloads\open.jpg')

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#laplacian method 
lap=cv.Laplacian(gray,cv.CV_64F)   #second derivative => either positive or negative
lap=np.uint8(np.absolute(lap))     #unsigned integer
cv.imshow('Laplacian',lap)

#sobel method
sobelx=cv.Sobel(gray, cv.CV_64F, 1,0) #for x-axis so: x=1,y=0
sobely=cv.Sobel(gray,cv.CV_64F,0,1) #for y-axis so: x=0,y=1
combined_sobel= cv.bitwise_or(sobelx,sobely)
combined_sobel=np.uint8(np.absolute(combined_sobel))

cv.imshow('sobel combined',combined_sobel)
#cv.imshow('sobelx',sobelx)
#cv.imshow('sobely',sobely)

#Canny method
canny=cv.Canny(gray,150,175)  #threshold1,threshold2
cv.imshow('canny',canny)


cv.waitKey(0)
