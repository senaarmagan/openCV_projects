import cv2
from pyzbar.pyzbar import decode

#decode fonksiyonu Decoded sınıfında bir dizi nesne döndürür.
#Dizinin her öğesi algılanan bir barkodu veya Qr kodu temsil eder.

video = cv2.VideoCapture(0)

while(True):
    ret, resim = video.read()
    Barkod = decode(resim)
    for barkod in Barkod:
        (x, y, w, h) = barkod.rect
        #barkod veya qr kısmı dikdörtgen alan ile belirler
        cv2.rectangle(resim, (x, y), (x + w, y + h), (255, 255, 255), 8)
        #barcod kodun veya qr kodun numarasını veya yazısını yazdırır
        cv2.putText(resim, "Barkod/Qr Data: " + str(barkod.data), (0, resim.shape[0] - 12),
                    cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
      
    cv2.imshow('Goruntu', resim)
    if cv2.waitKey(13) & 0xFF == ord('q'):
        break
    
video.release()
#oluşturulan pencereleri kapatır
cv2.destroyAllWindows()

