import cv2 as cv

img = cv.imread(r' ') #enter image path


resized = cv.resize(img, (800, 600))
flipped = cv.flip(resized, 0)
gray=cv.cvtColor(resized, cv.COLOR_BGR2GRAY)




#cv.rectangle(gray, (200, 200), (400, 400), (120,20,200), 7)

#cv.imshow("Image", gray)


#cv.imshow("img",img)

edges=cv.Canny(resized,threshold1=10,threshold2=400)
#edges=cv.Canny(resized,
cv.imshow("Canny",edges)


# Wait until a key is pressed
cv.waitKey(0)

# Close the window
cv.destroyAllWindows()
