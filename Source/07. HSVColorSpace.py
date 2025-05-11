import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import os

def hsvColorSegmentation():
    root = os.getcwd()
    imgPath = os.path.join(root, 'Photos\\DNT.jpg')
    img = cv.imread(imgPath)
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    lowerBound = np.array([0, 0, 50])
    upperrBound = np.array([50, 150, 200])
    mask = cv.inRange(hsv, lowerBound, upperrBound)

    plt.figure()
    plt.imshow(imgRGB)
    plt.show()

    cv.imshow('mask',mask)
    cv.waitKey(0)

if __name__ == '__main__':
    hsvColorSegmentation()