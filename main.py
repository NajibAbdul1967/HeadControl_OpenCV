import speech_recognition as sr
import pyautogui
import cv2
import numpy as np

#Init audio 

#Init clicks and cursor

#Init face detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
#


def move_cursor(mX,mY):
    pass

def listen_for_command():
    pass


def detect_face():
    pass
    




while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        #Middle of rectangle?
        mX = (x+w)/2
        mY = (y+h)/2
        print(mX,mY)
        # Move screen
        #move_mouse(mX,mY)

    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

    
cap.release()
cv2.destroyAllWindows()



    

