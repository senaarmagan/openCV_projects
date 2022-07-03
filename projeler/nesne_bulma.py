import cv2
import numpy as np


img=cv2.imread('img/bilgisayar.jpg')
griton=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#istenilen resmin verilmesi
nesne=cv2.imread('img/istenilen.jpg',0)

x,y=nesne.shape[::-1]
#görüntünün şablon görüntüsüyle eşleşen kısımlarını bulmak için kullanılır(matchTemplate).
resim=cv2.matchTemplate(griton,nesne,cv2.TM_CCOEFF_NORMED)
threshold=0.8 #görüntü eşikleme

loc=np.where(resim > threshold)

#resmi boyutlarına göre ayarlayıp dikdörtgen içine alma
for n in zip(*loc[::-1]):
    cv2.rectangle(img,n,(n[0]+x,n[1]+y),(0,255,255),2)

cv2.imshow('bulunan nesne',img)
cv2.waitKey()
cv2.destroyAllWindows()    

