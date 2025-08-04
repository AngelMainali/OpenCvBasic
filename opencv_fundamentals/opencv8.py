import cv2 as cv  

img=cv.imread(r"C:\Users\Dell\Desktop\opencv\image_sample\cat.jpg")
resize=cv.resize(img,(500,500))


gray=cv.cvtColor(resize,cv.COLOR_BGR2GRAY)

blur_img=cv.GaussianBlur(gray,(1,1),2)

canny=cv.Canny(blur_img,50,100)

canny_countour,_ =cv.findContours(canny,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
count1=len(canny_countour)
print(count1)

thresh_val,thresh_img=cv.threshold(blur_img,120,255,cv.THRESH_BINARY)

thresh_countour,_ =cv.findContours(thresh_img,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
count2=len(thresh_countour)
print(count2)

cv.imshow("resize",resize)
cv.imshow("gray",gray)
cv.imshow("blur",blur_img)
cv.imshow("canny",canny)


#draw countours
img_thresh=resize.copy()
img_canny=resize.copy()


cv.drawContours(img_thresh,thresh_countour,-1,(0,255,0),2)
cv.drawContours(img_canny,canny_countour,-1,(0,0,255),2)

cv.imshow("img_thresh",img_thresh)
cv.imshow("img_canny",img_canny)


cv.waitKey(0)