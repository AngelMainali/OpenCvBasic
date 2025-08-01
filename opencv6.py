import cv2 as cv 
import numpy as np 

img=cv.imread(r'C:\Users\Dell\Downloads\open.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#cv.imshow('Image',gray)

########################################################################################################################################

#simple threshold
threshold, threshold_img=cv.threshold(gray, 135,255,cv.THRESH_BINARY) #for inverse: cv.THRESH_BINARY_INV :: if threshold>135 then 255 indicated the white color :: 135 is threshold value 
#cv.imshow('Threshold',threshold_img)

#Adaptive Threshold
adaptive_threshold=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,3) #cv.ADAPTIVE_THRESH_MEAN_C 
#cv.imshow('Adaptive_Threshold_img',adaptive_threshold)

#########################################################################################################################################

#color spaces

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
hsv=cv.cvtColor(img, cv.COLOR_BGR2HSV)
lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
hls=cv.cvtColor(img,cv.COLOR_BGR2HLS)
ycrcb=cv.cvtColor(img,cv.COLOR_BGR2YCrCb)
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)

#cv.imshow('HSV',hsv)
#cv.imshow('LAB',lab)
#cv.imshow('HLS',hls)
#cv.imshow('YCrCb',ycrcb)
cv.imshow('RGB',rgb)

###########################################################################################################################################

cv.waitKey(0)
cv.destroyAllWindows()
