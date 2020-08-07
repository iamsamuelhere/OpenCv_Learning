from cv2 import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread('dhoni.jpg')
img=cv2.cvtColor(img,cv2.COLOR_RGB2BGR)

#Lapsian Gradient
lap_img=cv2.Laplacian(img,cv2.CV_64F)#ksize is optional
lap_img=np.uint8(np.absolute(lap_img))
cv2.imwrite('lap.png',lap_img)

#Sobel Gradient
sobx=cv2.Sobel(img,cv2.CV_64F,1,0)
sobx=np.uint8(np.absolute(sobx))
cv2.imwrite('sob.png',sobx)

soby=cv2.Sobel(img,cv2.CV_64F,0,1)
soby=np.uint8(np.absolute(soby))
cv2.imwrite('soby.png',soby)

sobelCombinex_y=cv2.bitwise_or(sobx,soby)
cv2.imwrite('sobcomb.png',sobelCombinex_y)


#Canny
cannyimg=cv2.Canny(img,100,200)
cv2.imwrite('canny.png',cannyimg)

images=[img,lap_img,sobx,soby,sobelCombinex_y,cannyimg]
titles=['original','lapsian gradient','SobelX','Sobely','sobelcombine_x&y','Canny']



for i in range(6):
    plt.subplot(3,2,i+1)
    plt.tight_layout()

    plt.imshow(images[i])
    plt.title(titles[i])

plt.show()

cv2.waitKey()