from cv2 import cv2
#On press-n-->mountian,,, esc---destroy all 

img=cv2.imread('apple.jfif')
cv2.imshow('output',img)
k=cv2.waitKey()
if(k==ord('m')):
    img2=cv2.imread('mac.jpg')
    cv2.imshow('ouput2',img2)
    cv2.waitKey()
    cv2.destroyAllWindows()
    cv2.imwrite('imgwrite.jpg',img2)
elif(k==27):
    img=cv2.imread('apple.jfif')
    cv2.imshow('output',img)
    cv2.waitKey()
    cv2.destroyAllWindows()
    cv2.imwrite('applecopy.jfif',img)


