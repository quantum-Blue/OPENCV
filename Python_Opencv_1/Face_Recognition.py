
import dlib
import cv2
import face_recognition
from datetime import datetime
import sqlite3

con = sqlite3.connect("yuztaninan.db")
cursor = con.cursor()


def tablo():
    cursor.execute("create table if not exists kisiler(ad Text, zaman DATETIME)")
    con.commit()

tablo()

def ekle(isim, tarih):
    cursor.execute("Insert into kisiler Values(?, ?)", (isim, tarih))
    con.commit()

detector = dlib.get_frontal_face_detector()
enes = face_recognition.load_image_file("enes.jpeg")
enes_enc = face_recognition.face_encodings(enes)[0]

zakir = face_recognition.load_image_file("zakir.jpeg")
zakir_enc = face_recognition.face_encodings(zakir)[0]

gorkem = face_recognition.load_image_file("gorkem.jpeg")
gorkem_enc = face_recognition.face_encodings(gorkem)[0]

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    face_loc = []
    faces = detector(frame)

    for face in faces:
        x = face.left()
        y = face.top()
        w = face.right()
        h = face.bottom()
        face_loc.append((y, w, h, x))

    i = 0

    face_encoding = face_recognition.face_encodings(frame, face_loc)

    for face in face_encoding:
        y, w, h, x = face_loc[i]
        sonuc = face_recognition.compare_faces([enes_enc], face)
        sonuc2 = face_recognition.compare_faces([zakir_enc], face)
        sonuc3 = face_recognition.compare_faces([gorkem_enc], face)

        if sonuc[0] == True:
            cv2.rectangle(frame, (x, y), (w, h), (255, 0, 0), 2)
            cv2.putText(frame, "enes", (x, h + 35), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
            ekle("Enes", datetime.now())

        elif sonuc2[0] == True:
            cv2.rectangle(frame, (x, y), (w, h), (255, 0, 0), 2)
            cv2.putText(frame, "zakir", (x, h + 35), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
            ekle("Zakir", datetime.now())

        elif sonuc3[0] == True:
            cv2.rectangle(frame, (x, y), (w, h), (255, 0, 0), 2)
            cv2.putText(frame, "gorkem", (x, h + 35), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
            ekle("Gorkem", datetime.now())

        else:
            cv2.rectangle(frame, (x, y), (w, h), (255, 0, 0), 2)
            cv2.putText(frame, "yabanci", (x, h + 35), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
            ekle("Bilinmeyen", datetime.now())

    cv2.imshow("1", frame)
    if cv2.waitKey(10) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
con.close()

















"""
import dlib
import cv2
import face_recognition
from datetime import datetime
import sqlite3

con=sqlite3.connect("yuztaninan.db")
cursor=con.cursor()

def tablo():
    cursor.execute("create table if not exist kisiler( ad Text,zaman DATETIME ) ")
    con.commit()

tablo()

def ekle(isim,tarih):
    cursor.execute("Insert into kisiler Values(?,?)",(isim,tarih))
    con.commit()



detector = dlib.get_frontal_face_detector()
enes=face_recognition.load_image_file("enes.jpeg")
enes_enc=face_recognition.face_encodings(enes)[0]

zakir=face_recognition.load_image_file("zakir.jpeg")
zakir_enc=face_recognition.face_encodings(zakir)[0]

gorkem=face_recognition.load_image_file("gorkem.jpeg")
gorkem_enc=face_recognition.face_encodings(gorkem)[0]

cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()

    face_loc=[]
    faces=detector(frame)

    for face in faces:
        x=face.left()
        y=face.top()
        w=face.right()
        h=face.bottom()
        face_loc.append((y,w,h,x))        



    i=0

    #face_loc=face_recognition.face_locations(frame)
    face_encoding=face_recognition.face_encodings(frame,face_loc)

    for face in face_encoding:
        
        y,w,h,x = face_loc[i]
        sonuc=face_recognition.compare_faces([enes_enc],face)
        #print(sonuc) # beni algılarsa True,algılamazsa False sonuç döndürür
        sonuc2=face_recognition.compare_faces([zakir_enc],face)
        sonuc3=face_recognition.compare_faces([gorkem_enc],face)

        if sonuc[0]==True:
            cv2.rectangle(frame,(x,y),(w,h),(255,0,0),2)
            cv2.putText(frame,"enes",(x,h+35),cv2.FONT_HERSHEY_PLAIN,2,(0,0,255),2)

            ekle("Enes",datetime.now())
        
        elif sonuc2[2]==True:

            cv2.rectangle(frame,(x,y),(w,h),(255,0,0),2)
            cv2.putText(frame,"zakir",(x,h+35),cv2.FONT_HERSHEY_PLAIN,2,(0,0,255),2)

            ekle("Zakir",datetime.now())

        elif sonuc3[2]==True:
            
            cv2.rectangle(frame,(x,y),(w,h),(255,0,0),2)
            cv2.putText(frame,"gorkem",(x,h+35),cv2.FONT_HERSHEY_PLAIN,2,(0,0,255),2)

            ekle("Gorkem",datetime.now())

        else:
            cv2.rectangle(frame,(x,y),(w,h),(255,0,0),2)
            cv2.putText(frame,"yabanci",(x,h+35),cv2.FONT_HERSHEY_PLAIN,2,(0,0,255),2)

            ekle("Bilinmeyen",datetime.now())



    cv2.imshow("1",frame)
    if cv2.waitKey(10) & 0xFF == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()


con.close()

"""