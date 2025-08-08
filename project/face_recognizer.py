import cv2 as cv 
import numpy as np 
import os

face_cascade= cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

recognizer= cv.face.LBPHFaceRecognizer_create()

dataset_path='training_images'

faces=[]
labels=[]

lables_to_name={}
current_label=0

for person_name in os.listdir(dataset_path):
     person_folder =os.path.join(dataset_path,person_name)

     lables_to_name[current_label]=person_name

     for image_name in os.listdir(person_folder):
        image_path=os.path.join(person_folder,image_name)

        image= cv.imread(image_path, cv.IMREAD_GRAYSCALE)

        face_rect= face_cascade.detectMultiScale(image,scaleFactor=1.1,minNeighbors=5)

        for (x,y,w,h) in face_rect:
            face_roi= image[y:y+h,x:x+w]
            face_resize= cv.resize(face_roi,(200,200))

            faces.append(face_resize)
            labels.append(current_label)
    
     current_label+=1 


faces = np.array(faces)
labels = np.array(labels)

recognizer.train(faces,labels)
print("Training completed...")

test_img=cv.imread(r'training_images\Elon_Musk\EM11.jpg')
test_gray=cv.cvtColor(test_img,cv.COLOR_BGR2GRAY)
faces_rectangle=face_cascade.detectMultiScale(test_gray,scaleFactor=1.1,minNeighbors=5)
for (x,y,w,h) in faces_rectangle:
    face_roi=test_gray[y:y+h,x:x+w]
    face_resize= cv.resize(face_roi,(200,200))
    label,confidence=recognizer.predict(face_resize)
    person_name = lables_to_name[label]
    
    text=f"{person_name}  confidence=({round(confidence,2)})"

    cv.rectangle(test_img,(x,y),(x+w,y+h),(0,255,0),2)
    cv.putText(test_img,text,(x,y-10),cv.FONT_HERSHEY_SIMPLEX,0.9,(255,0,0),3)

result=cv.resize(test_img,(1000,700))
cv.imshow("RESULT",result)
cv.waitKey(0)
cv.destroyAllWindows()