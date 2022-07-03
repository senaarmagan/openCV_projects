import cv2

backsub = cv2.createBackgroundSubtractorMOG2()
kamera = cv2.VideoCapture("img/video.avi")
i = 0
minArea=2600

while True:
    ret, frame = kamera.read()
    fgmask = backsub.apply(frame, None, 0.02)
    erode=cv2.erode(fgmask,None,iterations=4)
    moments=cv2.moments(erode,True)
    area=moments['m00']

    if moments['m00'] >=minArea:
        x=int(moments['m10']/moments['m00'])
        y=int (moments['m01']/moments['m00'])
        print("mom :" + str(moments['m00']) + "x :" + str(x) + " y : " + str(y))
        if x>40 and x<55 and y>50 and y<65:
            i=i+1

            print("ust"+str(i))
        elif x>102 and x<110 and y>105 and y<130:
            i=i+1
            print("alt"+str(i))

        cv2.putText(frame,'Arac: %r' %i, (200,30), cv2.FONT_HERSHEY_COMPLEX,1, (255, 255, 255), 2)
        cv2.imshow("frame", frame)
        cv2.imshow("fgmask", fgmask)

    key = cv2.waitKey(25)
    if key == ord('q'):
            break
kamera.release()
cv2.destroyAllWindows()

