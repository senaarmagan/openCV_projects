import cv2

yuzCascade=cv2.CascadeClassifier('xml/haarcascade_frontalface_default.xml')
smileCascade=cv2.CascadeClassifier('xml/haarcascade_smile.xml')

kamera=cv2.VideoCapture(0)

while True:
    ret,frame=kamera.read()
    griton=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    yuzler=yuzCascade.detectMultiScale(griton,1.3,5)
    for (x,y,w,h) in yuzler:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,110,50),2)
        griton=griton[y:y+h,x:x+w]
        renkli=frame[y:y+h,x:x+w]
        agiz=smileCascade.detectMultiScale(griton)
        for(ax,ay,aw,ah) in agiz:
            cv2.rectangle(renkli,(ax,ay),(ax+aw,ay+ah),(0,70,150),2)  
        cv2.imshow('görüntü',frame)
         
    key = cv2.waitKey(25)
    if key == ord('q'):
        break
           
kamera.release()
cv2.destroyAllWindows()        
