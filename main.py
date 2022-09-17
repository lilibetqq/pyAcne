import cv2
from time import sleep


casc_path = 'data/haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(casc_path)


def checkVideo():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print('Unable to load camera.')
        sleep(5)
        pass

    while True:
        _, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4, 0,  [130, 130])
        print(faces)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
       
        cv2.imshow('img', img)
        k = cv2.waitKey(30) & 0xff
        if k==27:
            break
            
    cap.release()

def checkPhoto():
    img = cv2.imread('samples/pasha.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('img', img)
    cv2.waitKey()

checkVideo()
#checkVideo()