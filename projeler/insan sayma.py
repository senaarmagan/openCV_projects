import cv2

backsub = cv2.createBackgroundSubtractorMOG2()
kamera = cv2.VideoCapture("img/humanVideo.mp4")
i = 0
minArea=5000
while True:
    ret, frame = kamera.read()

    fgmask = backsub.apply(frame, None, 0.05)
    erode=cv2.erode(fgmask,None,iterations=4)
    moments=cv2.moments(erode,True)
    area=moments['m00']
     
    if moments['m00'] >=minArea:
        x=int(moments['m10']/moments['m00'])
        print("mom :" + str(moments['m00']) + "x :" + str(x))
        if x>350:
            i=i+1

        cv2.putText(frame,'Human ID: %r' %i, (200,50), cv2.FONT_HERSHEY_COMPLEX,2, (255, 255, 255), 3)
        cv2.imshow("frame", frame)
        cv2.imshow("fgmask", fgmask)

    key = cv2.waitKey(25)
    if key == ord('q'):
            break

kamera.release()
cv2.destroyAllWindows()
