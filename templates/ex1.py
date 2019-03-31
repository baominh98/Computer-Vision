from pylab import *
from PIL import Image
import cv2

img = array(Image.open('static/chess.jpg').convert('L'))  # convert('L'))=>trang den
img1 = Image.open('static/chess.jpg')
img1 = array(img1)
gray()
print('B1')
# img = cv2.GaussianBlur(img, (3, 3), 1.0)
title('IMG')
imshow(img)


print('B2')
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
# horFilter = np.empty([5,5])
# verFilter = np.empty([5,5])
# horFilter = ([5,5,5,0,1],[0,0,0,0,0],[5,5,10,5,5],[0,0,10,10,10],[30,30,30,0,0])
# verFilter = ([5,0,0,10,30],[5,0,0,10,0],[5,0,15,10,20],[10,0,15,10,10],[10,0,15,10,0])
s = np.zeros([2,2])
_s = np.zeros([2,2])
x, y = img.shape
A = np.zeros([x,y])
D = 1
Wmn = 1
s11 = 0
s12 = 0
s22 = 0
for i in range(x):
    for j in range(y):
        for m in range(i-D, i+D+1):
            for n in range(j-D, j+D+1):
                if m>x-1 or n >y-1:
                    _s = np.zeros([2,2])
                else:
                    s11 = int(horFilter[m,n])*int(horFilter[m,n])
                    s12 = int(horFilter[m,n])*int(verFilter[m,n])
                    s22 = int(verFilter[m,n])*int(verFilter[m,n])
                    _s[0,0] = s11
                    _s[0,1] = s12
                    _s[1,0] = s12
                    _s[1,1] = s22
                s = s+_s*Wmn
        
        A[i,j] = np.linalg.det(s) - (s[0,0]+s[1,1])*0.04
        if A[i,j]<0:
            A[i,j] = 0
        s = np.zeros([2,2])
print('B4')
for i in range(x):
    for j in range(y):
        if i-1<0 or i+1>x-1 or j-1<0 or j+1>y-1:
            continue
        if A[i+1, j] < A[i, j] or A[i-1, j] < A[i, j]:
            continue
        if A[i+1, j+1] < A[i, j] or A[i-1, j-1] < A[i, j]:
            continue
        if A[i, j+1] < A[i, j] or A[i, j-1] < A[i, j]:
            continue
        if A[i-1, j+1] < A[i, j] or A[i+1, j-1] < A[i, j]:
            continue
        A[i, j] = 0

print(A)
figure()
imshow(A)
img1[A>0.01*A.max()]=[0,0,255]
figure()
imshow(img1)
show()
