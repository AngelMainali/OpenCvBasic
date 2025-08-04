import cv2 as cv
import numpy as np

img= cv.imread(r'C:\Users\Dell\Downloads\open.jpg')

############################################################################

#resize image
resized=cv.resize(img,(500,500), interpolation=cv.INTER_AREA)
#cv.imshow('Image',resized)

##############################################################################

#flip image
flip= cv.flip(img, -1) #flip in both direction
#cv.imshow('Image1',flip)

flip1= cv.flip(img, 1) #horizontal flip and 0 for vertical flip
#cv.imshow('Image2',flip1)

###############################################################################

#crop image
cropped =img[100:500, 200:500]
#cv.imshow('img',cropped)

################################################################################

#translation

def translate(img,x,y):
    trans_mat = np.float32([[1,0,x],[0,1,y]])
    dimension = (img.shape[1], img.shape[0]) #(width,height)
    return cv.warpAffine(img, trans_mat, dimension)

#translated = translate(img,-200,-100)
#cv.imshow('translated', translated)
#cv.imshow('original_img',img)

################################################################################

#rotation

def rotate(img, angle, rotate_point = None):
    (height,width)= img.shape[:2] #0=height, 1=width

    if rotate_point is None:
        rotate_point = (width // 2, height // 2)

    rot_mat= cv.getRotationMatrix2D(rotate_point, angle, 1) #scale=1
    dimension = (width,height)

    return cv.warpAffine(img, rot_mat, dimension)    

rotated= rotate(img, -45, (200,100))
cv.imshow("original image",img)
cv.imshow("rotated img",rotated)



cv.waitKey(0)
cv.destroyAllWindows()

