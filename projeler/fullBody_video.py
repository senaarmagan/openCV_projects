import cv2

kamera=cv2.VideoCapture('img/video.mp4')
bodyCascade=cv2.CascadeClassifier('xml/haarcascade_fullbody.xml')

while True:
    ret,frame=kamera.read()
    griton=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    insan=bodyCascade.detectMultiScale(griton,scaleFactor=1.2,minNeighbors=3)
    
    #bulunan insanları dikdörtgen içine alma 
    for (x,y,w,h) in insan:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,180,0),2)
     
        #çıkış işlemi q ile
    cv2.imshow('insan',frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

kamera.release()
cv2.destroyAllWindows()    
