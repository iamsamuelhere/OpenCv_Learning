from cv2 import cv2
pedas_class=cv2.CascadeClassifier('haarcascade_fullbody.xml')

cam=cv2.VideoCapture('pedestrians.avi')

while(cam.isOpened()):
    ret,frame=cam.read()
    grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    people=pedas_class.detectMultiScale(grey,1.1,3)

    for (x,y,w,h) in people:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)

    cv2.imshow('output',frame)
    k=cv2.waitKey(1)
    if(k==27):
        break
cam.release()
cv2.destroyAllWindows()