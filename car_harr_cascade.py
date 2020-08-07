from cv2 import cv2
cars_cascade=cv2.CascadeClassifier('cars.xml')

cap=cv2.VideoCapture('car.avi')
while(cap.isOpened()):
    ret,frame=cap.read()
    grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    car=cars_cascade.detectMultiScale(grey,1.1,4)

    for (x,y,w,h) in car:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),3)

    cv2.imshow('cars',frame)
    k=cv2.waitKey(1)
    if(k==27):
        break

cap.release()
cv2.destroyAllWindows()