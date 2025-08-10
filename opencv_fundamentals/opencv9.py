import cv2 as cv 
import numpy as np

#load the image
img_path=r'project\training_images\Elon_Musk\EM1.jpg'
img=cv.imread(img_path)
img=cv.resize(img, (400,400))

#convert the image to hsv
hsv_img=cv.cvtColor(img, cv.COLOR_BGR2HSV)

#define the skin color
lower_skin=np.array([0,20,70], dtype=np.uint8)    #Hue,saturation,value
upper_skin=np.array([20,255,255], dtype=np.uint8)

#define the mask
img_mask=cv.inRange(hsv_img, lower_skin, upper_skin)

#apply the mask
detected_skin=cv.bitwise_and(img,img,mask=img_mask)

cv.imshow('Elon Musk',img)
cv.imshow('mask',img_mask)
cv.imshow('detected skin',detected_skin)

cv.waitKey(0)
cv.destroyAllWindows()