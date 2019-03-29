from pylab import *
from PIL import Image
# LBP 8bit
def SimpleLBPExtract(img):
    row, col = img.shape
    imgOut = np.empty((row-2, col-2))
    binArray = 2**np.arange(12)
    for i in range(1,row-1):
        for j in range(1,col-1):
            pixelArray = img[i-1:i+2, j-1:j+2].flatten()
            a = np.empty(12)
            a = pixelArray[[0,1,1,2,3,3,5,5,6,7,7,8]] >= pixelArray[4]   #  So sanh pixel giua voi xung quanh
            imgOut[i-2,j-2] = a.dot(binArray)# nhan pixelArray voi chuoi he so binArray(2^1,2^2,2^3...
    return imgOut
img = array(Image.open('/home/caohuy/Python/1.jpg').convert('L'))  # convert('L'))=>trang den
gray()
imshow(img)
imgLBP = SimpleLBPExtract(img)
figure()
imshow(imgLBP)
show()