# import LocVer3
from pylab import *
from PIL import Image
import cv2

img = array(Image.open('1.jpg').convert('L'))  # convert('L'))=>trang den
gray()
print('B1')
img = cv2.GaussianBlur(img, (3, 3), 1.0)
sigma = 0.5
medianG = np.median(img)
TH_low = int(max(0, (1.0 - sigma) * medianG))
TH_high = int(min(255, (1.0 + sigma) * medianG))
edged = cv2.Canny(img, TH_low, TH_high) 
title('OpenCV')
imshow(edged)
###############################
# noisyImg = img
x, y = img.shape
print('B2')
# figure()
# title('Goc')
# imshow(img)
# imgout = LocVer3.Loc(noisyImg, '1', 3)
prewittx = array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])
prewitty = array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
horFilter = cv2.filter2D(img, -1, prewittx)
verFilter = cv2.filter2D(img, -1, prewitty)
# figure()
# title('horFilter')
# imshow(horFilter)
# figure()
# title('verFilter')
# imshow(verFilter)
O = np.empty(horFilter.shape)
A = np.empty([x, y])
print('B3-B4')
for i in range(x):
    for j in range(y):
        if horFilter[i, j] != 0:
            O[i, j] = (arctan(verFilter[i, j] / horFilter[i, j]) * 180) / pi
        else:
            O[i, j] = 90
        if 315 + 22.5 <= O[i, j] or O[i, j] < 22.5 or 135 + 22.5 <= O[i, j] < 225 - 22.5:
            O[i, j] = 0
        elif 22.5 <= O[i, j] < 45 + 22.5 or 225 - 22.5 <= O[i, j] < 225 + 22.5:
            O[i, j] = 45
        elif 90 - 22.5 <= O[i, j] < 90 + 22.5 or 270 - 22.5 <= O[i, j] < 270 + 22.5:
            O[i, j] = 90
        elif 135 - 22.5 <= O[i, j] < 135 - 22.5 or 315 - 22.5 <= O[i, j] < 315 + 22.5:
            O[i, j] = 135    
        A[i, j] = sqrt((int(horFilter[i, j]) * int(horFilter[i, j])) + (int(verFilter[i, j]) * int(verFilter[i, j])))
print('B5')
for i in range(1, x-1):
    for j in range(1, y-1):
        if O[i, j] == 0:
            if A[i+1, j] > A[i, j] or A[i-1, j] > A[i, j]:
                A[i, j] = 0
        elif O[i, j] == 45:
            if A[i+1, j+1] > A[i, j] or A[i-1, j-1] > A[i, j]:
                A[i, j] = 0
        elif O[i, j] == 90:
            if A[i, j+1] > A[i, j] or A[i, j-1] > A[i, j]:
                A[i, j] = 0
        elif O[i, j] == 135:
            if A[i-1, j+1] > A[i, j] or A[i+1, j-1] > A[i, j]:
                A[i, j] = 0
print('B6')     

sigma = 0.33
# medianG = np.median(img)
medianG = A.mean()
TH_low = int(max(0, (1.0 - sigma) * medianG))# max(x,y)
TH_high = int(min(255, (1.0 + sigma) * medianG))
print (TH_low, TH_high, medianG)
a = 1
for i in range(1,x-1):
    for j in range(1,y-1):
        if A[i, j] > TH_high:
            A[i, j] = 255
        elif A[i, j] < TH_low:
            A[i, j] = 0
while a:
    a=0
    for i in range(1,x-1):
        for j in range(1,y-1):
            if TH_high > A[i, j] > TH_low:
                if A[i-1, j-1] > TH_high or A[i+1, j+1] > TH_high or A[i-1, j] > TH_high or A[i+1, j] > TH_high or A[i-1, j+1] > TH_high or A[i+1, j-1] > TH_high or  A[i, j-1] > TH_high or A[i, j+1] > TH_high :
                    A[i, j] = 255
                else:
                    A[i, j] = 0
                a = 1

figure()
title('Canny')
imshow(A)
show()
