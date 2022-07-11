import os
import cv2 as cv

def readImages(dirPath):
    '''
    Read all images within a given directory.
    Arguments:
    - dirPath: string of directory path
    Output:
    - images: array of cv2 image objects
    - names: array of strings corresponding to filenames of images
    '''
    # variables
    images = []
    names = []
    directory = os.listdir(dirPath)
    # iterating trough folder
    for file in directory:
        # omitting hidden folders
        if file[0] == '.':
            continue
        # reading values
        path = f'{dirPath}/{file}'
        name = os.path.splitext(file)[0]
        img = cv.imread(path)
        # storing values
        images.append(img)
        names.append(name)
    # finished
    print(f'Read {len(images)} images succesfully.')
    return images, names