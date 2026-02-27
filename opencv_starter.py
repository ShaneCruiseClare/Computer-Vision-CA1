import cv2 as cv
import matplotlib.pyplot as plt
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

#create histogram
#find threshold of histogram of image *example set back 50 pixels from peak
def histogram(img):
    hist = np.zeros(256)
    for x in range(0, img.shape[0]):
        for y in range(0, img.shape[1]):
            hist[img[x,y]] += 1

    return hist

#create a label function that prints text pass or fail 

#read in an image into memory
for imgList in range(1,16):
    img = cv.imread('C:/Users/shane/TUD/Computer Vision/images/Oring' + str(imgList) + '.jpg',0)
    thresh = 100
    hist = histogram(img)
    plt.plot(hist)
    plt.show()
    bw = threshold(img,thresh)
    cv.imshow('image',bw)
    cv.waitKey(0)
    cv.destroyAllWindows()
