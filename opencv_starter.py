import cv2 as cv
import numpy as np
import time

def threshold(img,thresh):
    for x in range(0, img.shape[0]):
        for y in range(0, img.shape[1]):
            if img[x,y] > thresh:
                img[x,y] = 255
            else:
                img[x,y] = 0
    return img


#read in an image into memory
for imgList in range(1,16):
    img = cv.imread('C:/Users/shane/TUD/Computer Vision/images/Oring' + str(imgList) + '.jpg',0)
    thresh = 100
    bw = threshold(img,thresh)
    cv.imshow('image',bw)
    cv.waitKey(0)
    cv.destroyAllWindows()
