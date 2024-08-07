import cv2

"""
cap=cv2.VideoCapture(0) # default (0) : kamera

while True:
    ret, frame = cap.read() # ret : True/False , frame goruntu
    frame = cv2.flip(frame,1)
    cv2.imshow("webcab",frame) # kamera açılıyor

    cv2.waitKey(30) # 30 milisaniye boyunca
    if cv2.waitKey(1) & 0xFF == ord("q") :
        break

cap.release()

cv2.destroyAllWaindows()
"""

# **********************

"""
cap=cv2.VideoCapture("video.mp4") # suanlık video yok , videodan goruntu alır

while True:
    ret, frame = cap.read() 
    if ret==0:
        break
    frame = cv2.flip(frame,1)
    cv2.imshow("webcab",frame)
    if cv2.waitKey(1) & 0xFF == ord("q") :
        break

cap.release()
cv2.destroyAllWaindows()
"""

# ********************************

import cv2

cap = cv2.VideoCapture(0)

# Genişlik ve Yükseklik Değerlerini Ayarla
cap.set(3, 640)  # Genişlik
cap.set(4, 480)  # Yükseklik

dosyaadi = "/Users/enesbal/Desktop/video/1.avi"
codec = cv2.VideoWriter_fourcc("W", "M", "V", "2")
framerate = 30
resolution = (640, 480)

output = cv2.VideoWriter(dosyaadi, codec, framerate, resolution)

while cap.isOpened():
    ret, frame = cap.read()
    
    if not ret:
        print("Kamera başlatılamadı veya video sona erdi.")
        break

    frame = cv2.flip(frame, 1)
    output.write(frame)

    cv2.imshow("webcam", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    cv2.waitKey(30)

output.release()
cap.release()
cv2.destroyAllWindows()

