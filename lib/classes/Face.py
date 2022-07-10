import cv2 as cv
import face_recognition as fr

class Face:
    def __init__(   self,
                    name,
                    img,
                    ncoded) -> object:

        self.name = name
        self.img = img
        self.ncoded = ncoded
        pass

    