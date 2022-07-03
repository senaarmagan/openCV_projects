import cv2

#İstenilen sınıflandırıcıların xml dosyaları
yuzCascade=cv2.CascadeClassifier('xml/haarcascade_frontalface_default.xml')
gozCascade=cv2.CascadeClassifier('xml/haarcascade_eye.xml')

#Bilgisayar kamerasını açma
kamera=cv2.VideoCapture(0)

while True:
    ret,frame=kamera.read()
    griton=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    yuzler=yuzCascade.detectMultiScale(griton,1.2,5)
    for (x,y,w,h) in yuzler:
        #bulunan yüzü dikdörtgen içine alma
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,110,50),2)
        griton=griton[y:y+h,x:x+w]
        renkli=frame[y:y+h,x:x+w]
        gozler=gozCascade.detectMultiScale(griton)
        #yüz içerisinde bulunan gözleri dikdörtgen içine alma 
        for(ex,ey,ew,eh) in gozler:
            cv2.rectangle(renkli,(ex,ey),(ex+ew,ey+eh),(0,70,150),1)
             
    #çıkış işlemi q ile    
    cv2.imshow('görüntü',frame)
    if cv2.waitKey(13) & 0xFF == ord('q'):
        break
        
kamera.release()
cv2.destroyAllWindows()        