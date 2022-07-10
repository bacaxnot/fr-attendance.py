# EXTERNAL LIBRARIES
import cv2 as cv
import numpy as np
import face_recognition as fr

# INTERTNAL LIBRARIES
from lib import *

# VARIABLES DECLARATION
imagesPath = 'people/images'
encodingsPath = 'people/encodings'
attendancePath = 'attendance'

# IMAGE TREATMENT
images, names = readImages(imagesPath)
knownFaceEncodes = encodeImages(images)

# VIDEO CAPTURING
cam = cv.VideoCapture(0)

while True:
    success, img = cam.read()
    imgS = cv.resize(img, (0,0), None, 0.25, 0.25)
    imgS = cv.cvtColor(imgS, cv.COLOR_BGR2RGB)
    
    faceLocations = fr.face_locations(imgS)
    faceEncodes = fr.face_encodings(imgS, faceLocations)

    for encode, location in zip(faceEncodes, faceLocations):
        matches = fr.compare_faces(knownFaceEncodes, encode)
        distances = fr.face_distance(knownFaceEncodes, encode)
        matchIndex = np.argmin(distances)

        if matches[matchIndex]:
            name = names[matchIndex].upper()
            top, right, bottom, left = [coord * 4 for coord in location]
            
            cv.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2) 
            cv.rectangle(img, (left, bottom-35), (right, bottom), (0, 255, 0), cv.FILLED) 
            cv.putText(img, name, (left+6, bottom-6), cv.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            
            saved = saveRegister(name, attendancePath)
            if saved:
                print(f'{name} succesfully registered.')
            
    cv.imshow('FR_3000', img)
    cv.waitKey(1)