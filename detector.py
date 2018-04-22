import cv2, os
import numpy as np
from PIL import Image
import pickle
import sqlite3

recognizer = cv2.createLBPHFaceRecognizer()
recognizer.load('trainner/trainner.yml')
cascadePath = "Classifier/face.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
path = 'dataSet'



def getProfile(Id):
    conn = sqlite3.connect("FaceBase.db")
    cmd = 'SELECT * FROM Pessoas WHERE ID= ' + str(id)
    cursor = conn.execute(cmd)
    profile = None
    for row in cursor:
        profile = row
    conn.close()
    return profile


camera = cv2.VideoCapture(1)
font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 1, 1)

while True:
    ret, im = camera.read()
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(100, 100),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    for (x, y, w, h) in faces:
        id, conf = recognizer.predict(gray[y:y + h, x:x + w])
        cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)
    profile = getProfile(id)
    if profile != None:
        cv2.cv.PutText(cv2.cv.fromarray(im), str(profile[1]), (x, y + h + 30), font, 255)
        cv2.cv.PutText(cv2.cv.fromarray(im), str(profile[2]), (x, y + h + 60), font, 255)
        cv2.cv.PutText(cv2.cv.fromarray(im), str(profile[3]), (x, y + h + 90), font, 255)
        cv2.cv.PutText(cv2.cv.fromarray(im), str(profile[4]), (x, y + h + 120), font, 255)

    cv2.imshow('AO VIVO', im)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    camera.release()
    cv2.destroyAllWindows()
