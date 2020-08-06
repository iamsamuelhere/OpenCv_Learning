from cv2 import cv2
import matplotlib.pyplot as plt
dhoni=cv2.imread('dhoni.jpg')
ball=cv2.imread('ball.jpg')
dhoni_bgr=cv2.cvtColor(dhoni,cv2.COLOR_RGB2BGR)
ball_bgr=cv2.cvtColor(ball,cv2.COLOR_RGB2BGR)
font=cv2.FONT_HERSHEY_COMPLEX
cv2.putText(dhoni_bgr,'Dhoni',(403,95),font,1,(255,255,255))

names=['dhoni','ball']
images=[dhoni_bgr,ball_bgr]
for i in range(2):
    plt.subplot(1,2,i+1)
    plt.imshow(images[i])
    plt.title(names[i])

    # plt.xticks([])
    # plt.yticks([])
plt.show()