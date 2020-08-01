from cv2 import cv2

cam = cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('output.avi', fourcc,20.0,(640,480))



print(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))


while(cam.isOpened()):
    ret,frame=cam.read()
    out.write(frame)
    grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cv2.imshow('Black and white',grey)
    cv2.imshow('Color',frame)
   
    k=cv2.waitKey(1)
    if(k==ord('q')):
        break
    
cam.release()
out.release()





