import cv2
import numpy as np

img=cv2.imread('resim.jpg')

#gri tonlama
griton=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#bulanıklaştırma
blur = cv2.medianBlur(griton,5)

#kenar vurgulama
kenar=cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,9)

#filtreleme
renkli=cv2.bilateralFilter(img,9,300,300)

#karikatür efekti
karikatur=cv2.bitwise_and(renkli,renkli,mask=kenar)

cv2.imshow('Orjinal img',img)
cv2.imshow('GRİTON',griton)
cv2.imshow('bulanık resim',blur)
cv2.imshow('kenar vurgulama',kenar)
cv2.imshow('filtreli resim',renkli)
cv2.imshow('Karikatür',karikatur)

cv2.waitKey()
cv2.destroyAllWindows() 

