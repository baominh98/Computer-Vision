from pylab import *
import numpy
from PIL import Image
import cv2

def HOG_funtion(ImgInput = '3.png'):
    W = (64,64)
    Sw = (8,8)
    Sb = (16,16)
    binStep = 20
    binSize = int(180/binStep)
    imgColor = Image.open(ImgInput)
    img = array(imgColor.convert('L'))
    img = cv2.resize(img,W)
    imshow(img)
    gray()
    #Find gradient magnitude and orientation
    gx = cv2.Sobel(img, cv2.CV_32F , 1, 0, ksize=1)
    gy = cv2.Sobel(img, cv2.CV_32F , 0, 1, ksize=1)
    mag, angle = cv2.cartToPolar(gx, gy, angleInDegrees=True)
    angle = numpy.abs(angle - 180)
    #Find gradient histogram
    histArray = numpy.zeros((int(W[0]/Sw[0]), int(W[1]/Sw[1]), binSize))
    i = 0
    for row in range(0, W[0], Sw[0]):
        j = 0
        for col in range(0, W[1], Sw[1]):
            angleCell = angle[row:row+Sw[0], col:col+Sw[1]]/binStep
            angleCellDown = numpy.floor(angleCell).astype(int)
            angleCellUp = numpy.ceil(angleCell).astype(int)
            percentDown = 1 - (angleCell - angleCellDown)
            percentUp = 1 - percentDown
            angleCellDown[angleCellDown >= binSize] = 0
            angleCellUp[angleCellUp >= binSize] = 0
            magCell = mag[row:row+Sw[0], col:col+Sw[1]]
            histArray[i,j,angleCellDown] = magCell*percentDown
            histArray[i,j,angleCellUp] = histArray[i,j,angleCellUp] + magCell*percentUp
            j += 1
        i += 1
    row,col,b = histArray.shape
    sBVectors = numpy.zeros(((row - 1)*(col-1), binSize*4))
    index = 0
    for i in range(0, row-1):
        for j in range(0, col-1):
            sBVectors[index,:binSize] = histArray[i,j,:]
            sBVectors[index,binSize:binSize*2] = histArray[i+1,j,:]
            sBVectors[index,binSize*2:binSize*3] = histArray[i,j+1,:]
            sBVectors[index,binSize*3:binSize*4] = histArray[i+1,j+1,:]
            vectorLength = numpy.linalg.norm(sBVectors[index,:])
            # print(sBVectors.min(), sBVectors.max())
            if(vectorLength > 0):
                sBVectors[index,:] = sBVectors[index,:]/vectorLength
            index = index + 1
    hogVector = sBVectors.flatten()
    # print(hogVector.min(), hogVector.max())
    return hogVector