import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

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
#get img and analysis the peaks of the pixels using otsu's method
def auto_threshold(img):

    #hist = histogram(img)
    hist = np.zeros(256)
    for x in range(0, img.shape[0]):
        for y in range(0, img.shape[1]):
            hist[img[x,y]] += 1

    #get the total number of pixels
    total = img.shape[0] * img.shape[1]
    sum = 0

    for t in range(256):
        sum += t * hist[t]

    sumB = 0
    wB = 0
    wF = 0
    varMax = 0
    threshold = 3

    for t in range(256):
        wB += hist[t]
        #Weight background
        if (wB == 0):
            continue
        #Weight forground
        wF = total - wB
        if (wF == 0):
            break
        sumB += t * hist[t]
        #Mean background
        mB = sumB / wB
        #Mean foreground
        mF = (sum - sumB) / wF

        # calculate the betwwen class variance 
        varBetween = wB * wF * (mB - mF) * (mB - mF)

        #check if new max has been found 
        if varBetween > varMax:
            varMax = varBetween
            threshold = t

        return threshold
        
#create a label function that prints text pass or fail 
#def labelPassOrFails():
    #passLabel     

#needs two elements, using an array to be able to show 
def binaryMorp():
    #need to get the img and use the array to fill in the different gaps on the orings
    rows, cols = (8, 8)
    
    arr = [[0 for i in range(cols)] for j in range(rows)]

    arr[0][0] = 1
    for row in arr:
        print(row)

#read in an image into memory
for imgList in range(1,16):
    img = cv.imread('C:/Users/shane/TUD/Computer Vision/images/Oring' + str(imgList) + '.jpg',0)
    thresh = auto_threshold(img)
    hist = histogram(img)
    bM = binaryMorp()
    plt.plot(hist)
    plt.show()
    bw = threshold(img,thresh)
    cv.imshow('image',bw)
    cv.waitKey(0)
    cv.destroyAllWindows()
