from cv2 import cv2
face_classifier=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam=cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('outputvideo.avi', fourcc,20.0,(640,480))
while(1):
    ret,frame=cam.read()


    grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face=face_classifier.detectMultiScale(grey,1.1,4)
    print(face)
    for (x,y,w,h) in face:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
    out.write(frame)
    cv2.imshow('out',frame)

    k=cv2.waitKey(1)
    if(k==ord('q')):
        break
cam.release()