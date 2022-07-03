import cv2
import numpy as np

kamera=cv2.VideoCapture(0)

while (1):
    ret,frame=kamera.read()
    
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    """
    kırmızı=[150,30,30],[190,255,255]
    beyaz=[0,0,40],[256,60,256]
    sarı=[5,100,100],[40,255,256]
    """
    
    dusuk_mavi=np.array([100,60,60])
    yuksek_mavi=np.array([140,255,255])
    
    mask=cv2.inRange(hsv,dusuk_mavi,yuksek_mavi)
    son_resim=cv2.bitwise_and(frame,frame,mask=mask)
    
    cv2.imshow('orjinal',frame)
    cv2.imshow('son resim',son_resim)
    cv2.imshow('mask',mask)
    
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()

    
