import cv2 as cv 
import numpy as np 

#create two blank images
img1=np.zeros((300,300), dtype="uint8")
img2=np.zeros((300,300), dtype="uint8")

#draw a white rectangle in img1
cv.rectangle(img1,(50,50),(250,250),255,-1)

#draw a white circle in img2
cv.circle(img2, (150,150),120,255,-1)

#cv.imshow('rectangle',img1)
#cv.imshow('circle',img2)

#AND operation
bit_and =cv.bitwise_and(img1,img2)
#cv.imshow("AND",bit_and)

#OR operation
bit_or =cv.bitwise_or(img1,img2)
#cv.imshow("OR",bit_or)

#X-OR operation
bit_XOR=cv.bitwise_xor(img1,img2)
#cv.imshow("XOR",bit_XOR)

#NOT operation
bit_not=cv.bitwise_not(img1)
#cv.imshow("NOT",bit_not)


#Masking
img=cv.imread(r'C:\Users\Dell\Downloads\cat.jpg')
resized=cv.resize(img,(600,600))


#creating a mask
img_mask=np.zeros(resized.shape[:2], dtype="uint8")

#creating white circle in mask
cv.circle(img_mask,(300,300),200,255,-1)


masked=cv.bitwise_and(resized,resized,mask=img_mask)

# cv.imshow("priginal image",img)
# cv.imshow("resized",resized)
# cv.imshow("mask",img_mask)
# cv.imshow("masked",masked)

##############################################################################################################             

#splitting the channels

B,G,R=cv.split(resized)
# cv.imshow("original_img",resized)
# cv.imshow("blue",B)
# cv.imshow("green",G)
# cv.imshow("red",R)               

merge=cv.merge([B,G,R])
# cv.imshow("merge",merge)

zeros= np.zeros_like(B)
blue_visual= cv.merge([B,zeros,zeros])
green_visual= cv.merge([zeros,G,zeros])
red_visual= cv.merge([zeros,zeros,R])

cv.imshow("original_img",resized)
cv.imshow("blue_visual",blue_visual)
cv.imshow("green_visual",green_visual)
cv.imshow("red_visual",red_visual)
                
               
    
cv.waitKey(0)
cv.destroyAllWindows()
