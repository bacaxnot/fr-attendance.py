import cv2 as cv
import face_recognition as fr

def encodeImages(images):
    '''
    Encode images given an array of images.
    Arguments:
    - images: array of cv2 image objects
    Output:
    - encodedImgs: array of encoded images
    '''
    # variables
    encodedImgs = []
    # iterating through images
    for img in images:
        # encoding image
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        encoded = fr.face_encodings(img)[0]
        # storing value
        encodedImgs.append(encoded)
    # finished
    print(f'Encoded {len(encodedImgs)} images succesfully.')
    return encodedImgs