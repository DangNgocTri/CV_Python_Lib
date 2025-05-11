import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import os

def readAndwriteSiglePixel():
    root = os.getcwd()
    imgPath = os.path.join(root, 'Photos\Dog.jpg')
    img = cv.imread(imgPath)
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    plt.figure()
    plt.imshow(imgRGB)
    plt.show()
    # imgRGB[100:,:200,0] = 255
    # imgRGB[150:,:150,1] = 100
    # plt.figure()
    # plt.imshow(imgRGB)
    # plt.show()
    eyeRegion = imgRGB[55:70, 90:106].copy()
    eyeRegion[:, :, 0] = 50  # R
    dx = 70-55
    dy = 106-90

    StartY = 119
    StartX = 44

    # row y, col x
    
    imgRGB[ StartX : StartX + dx, StartY : StartY + dy ] = eyeRegion
    plt.figure()
    plt.imshow(imgRGB)
    plt.show()

if __name__ == '__main__':
    readAndwriteSiglePixel()