# import LocVer3
from pylab import *
from PIL import Image
import cv2

img = array(Image.open('1.jpg').convert('L'))  # convert('L'))=>trang den
gray()
img = cv2.GaussianBlur(img, (3, 3), 1.0)
# sigma = 0.33
# medianG = np.median(img)
# TH_low = int(max(0, (1.0 - sigma) * medianG))
# TH_high = int(min(255, (1.0 + sigma) * medianG))
# edged = cv2.Canny(img, TH_low, TH_high) 
# title('OpenCV')
# imshow(edged)
###############################
# noisyImg = img
x, y = img.shape

# figure()
title('Goc')
imshow(img)
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
Gradient = np.empty(horFilter.shape)
Alpha = np.empty([x, y])

for i in range(x):
    for j in range(y):
        if horFilter[i, j] != 0:
            Gradient[i, j] = (arctan(verFilter[i, j] / horFilter[i, j]) * 180) / pi
        else:
            Gradient[i, j] = 90
        if 315 + 22.5 <= Gradient[i, j] or Gradient[i, j] < 22.5 or 135 + 22.5 <= Gradient[i, j] < 225 - 22.5:
            Gradient[i, j] = 0
        elif 22.5 <= Gradient[i, j] < 45 + 22.5 or 225 - 22.5 <= Gradient[i, j] < 225 + 22.5:
            Gradient[i, j] = 45
        elif 90 - 22.5 <= Gradient[i, j] < 90 + 22.5 or 270 - 22.5 <= Gradient[i, j] < 270 + 22.5:
            Gradient[i, j] = 90
        elif 135 - 22.5 <= Gradient[i, j] < 135 - 22.5 or 315 - 22.5 <= Gradient[i, j] < 315 + 22.5:
            Gradient[i, j] = 135    
        Alpha[i, j] = sqrt((int(horFilter[i, j]) * int(horFilter[i, j])) + (int(verFilter[i, j]) * int(verFilter[i, j])))
        if i>0 and j>0 and i<x-1 and j<y-1:
            if Gradient[i, j] == 0:
                if Alpha[i+1, j] > Alpha[i, j] or Alpha[i-1, j] > Alpha[i, j]:
                    Alpha[i, j] = 0
            elif Gradient[i, j] == 45:
                if Alpha[i+1, j+1] > Alpha[i, j] or Alpha[i-1, j-1] > Alpha[i, j]:
                    Alpha[i, j] = 0
            elif Gradient[i, j] == 90:
                if Alpha[i, j+1] > Alpha[i, j] or Alpha[i, j-1] > Alpha[i, j]:
                    Alpha[i, j] = 0
            elif Gradient[i, j] == 135:
                if Alpha[i-1, j+1] > Alpha[i, j] or Alpha[i+1, j-1] > Alpha[i, j]:
                    Alpha[i, j] = 0

# for i in range(1, x-1):
#     for j in range(1, y-1):
#         if Gradient[i, j] == 0:
#             if Alpha[i+1, j] > Alpha[i, j] or Alpha[i-1, j] > Alpha[i, j]:
#                 Alpha[i, j] = 0
#         elif Gradient[i, j] == 45:
#             if Alpha[i+1, j+1] > Alpha[i, j] or Alpha[i-1, j-1] > Alpha[i, j]:
#                 Alpha[i, j] = 0
#         elif Gradient[i, j] == 90:
#             if Alpha[i, j+1] > Alpha[i, j] or Alpha[i, j-1] > Alpha[i, j]:
#                 Alpha[i, j] = 0
#         elif Gradient[i, j] == 135:
#             if Alpha[i-1, j+1] > Alpha[i, j] or Alpha[i+1, j-1] > Alpha[i, j]:
#                 Alpha[i, j] = 0
                
sigma = 0.66
medianG = np.median(img)
TH_low = int(max(0, (1.0 - sigma) * medianG))# max(x,y)
TH_high = int(min(255, (1.0 + sigma) * medianG))
print (TH_low, TH_high, medianG)
a = 1
while a:
    for i in range(x):
        for j in range(y):
            if Alpha[i, j] > TH_high:
                Alpha[i, j] = 255
            elif Alpha[i, j] < TH_low:
                Alpha[i, j] = 0
            elif Alpha[i, j] > TH_low:
                Alpha[i, j] = 255
            else:
                a = 0

figure()
title('Canny')
imshow(Alpha)
show()
