import cv2 as cv
img=cv.imread(r' ') # enter image path

resized= cv.resize(img,(800,600))
cv.imshow("image",resized)

#average blur
avg_blur = cv.blur(resized,(5,5))
cv.imshow('average_blur',avg_blur)

#median blur
median_blur= cv.medianBlur(resized,7) #only odd value
cv.imshow('median_blur',median_blur)

#gaussian blur
gaussian_blur= cv.GaussianBlur(resized, (5,5)  ,9) # 9(any value)=standard deviation of x-axis
cv.imshow('gaussian_blur',gaussian_blur)

#bilateral filter
bilateral_filter=cv.bilateralFilter(resized,18,20,20) # window, sd color, sd space
cv.imshow('bilateral_filter',bilateral_filter)


cv.waitKey(0)