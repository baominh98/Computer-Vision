from pylab import *
from PIL import Image
import cv2


def Harris1(img, Nguong, D = 1, Wmn = 1):
    title('IMG')
    imshow(img)
    prewittx = array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])
    prewitty = array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
    horFilter = cv2.filter2D(img, -1, prewittx)
    verFilter = cv2.filter2D(img, -1, prewitty)
    s = np.zeros([2,2])
    _s = np.zeros([2,2])
    x, y = img.shape
    A = np.zeros([x,y])
    for i in range(x):
        for j in range(y):
            s = np.zeros([2,2])
            for m in range(i-D, i+D+1):
                for n in range(j-D, j+D+1):
                    if m>x-1 or n >y-1:
                        _s = np.zeros([2,2])
                    else:
                        _s[0,0] = int(horFilter[m,n])*int(horFilter[m,n])
                        _s[0,1] = int(horFilter[m,n])*int(verFilter[m,n])
                        _s[1,0] = int(horFilter[m,n])*int(verFilter[m,n])
                        _s[1,1] = int(verFilter[m,n])*int(verFilter[m,n])
                    s = s+_s*Wmn
            
            A[i,j] = np.linalg.det(s) - (s[0,0]+s[1,1])*0.04

    for i in range(x):
        for j in range(y):
            if i-1<0 or i+1>x-1 or j-1<0 or j+1>y-1:
                continue
            if A[i+1, j] > A[i, j] or A[i-1, j] > A[i, j]:
                A[i, j] = 0
                continue
            if A[i+1, j+1] > A[i, j] or A[i-1, j-1] > A[i, j]:
                A[i, j] = 0
                continue
            if A[i, j+1] > A[i, j] or A[i, j-1] > A[i, j]:
                A[i, j] = 0
                continue
            if A[i-1, j+1] > A[i, j] or A[i+1, j-1] > A[i, j]:
                A[i, j] = 0
                continue
    # A = (A - A.min())*255/(A.max() - A.min())
    for i in range(x):
        for j in range(y):
            if A[i, j] > Nguong:
                A[i, j] = 255
            else: 
                A[i, j] = 0
    return A
def Harris2(img, Nguong, D = 1, Wmn = 1):
    prewittx = array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
    prewitty = array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
    horFilter = cv2.filter2D(img, -1, prewittx)
    verFilter = cv2.filter2D(img, -1, prewitty)

    s = np.zeros([2,2])
    _s = np.zeros([2,2])
    x, y = img.shape
    A = np.zeros([x,y])

    for i in range(x):
        for j in range(y):
            s = np.zeros([2,2])
            for m in range(i-D, i+D+1):
                for n in range(j-D, j+D+1):
                    if m>x-1 or n >y-1:
                        _s = np.zeros([2,2])
                    else:
                        _s[0,0] = int(horFilter[m,n])*int(horFilter[m,n])
                        _s[0,1] = int(horFilter[m,n])*int(verFilter[m,n])
                        _s[1,0] = int(horFilter[m,n])*int(verFilter[m,n])
                        _s[1,1] = int(verFilter[m,n])*int(verFilter[m,n])
                    s = s+_s*Wmn
            
            A[i,j] = np.linalg.det(s) - (s[0,0]+s[1,1])*0.04
    for i in range(x):
        for j in range(y):
            if i-1<0 or i+1>x-1 or j-1<0 or j+1>y-1:
                continue
            if A[i+1, j] > A[i, j] or A[i-1, j] > A[i, j]:
                A[i, j] = 0
                continue
            if A[i+1, j+1] > A[i, j] or A[i-1, j-1] > A[i, j]:
                A[i, j] = 0
                continue
            if A[i, j+1] > A[i, j] or A[i, j-1] > A[i, j]:
                A[i, j] = 0
                continue
            if A[i-1, j+1] > A[i, j] or A[i+1, j-1] > A[i, j]:
                A[i, j] = 0
                continue
    # A = (A - A.min())*255/(A.max() - A.min())
    for i in range(x):
        for j in range(y):
            if A[i, j] > Nguong:
                A[i, j] = 255
            else: 
                A[i, j] = 0
    return A
img = array(Image.open('static/chess.jpg').convert('L'))  # convert('L'))=>trang den
img1 = Image.open('static/chess.jpg')
img1 = array(img1)
gray()

while(1):
    try:
        Nguong = int(input('Nhap Gia Tri nguong: '))# 20
        break
    except Exception:
        print('Vui Long Nhap So')
# A2 = Harris2(img, Nguong)
A1 = Harris1(img, Nguong,1,1)
A = A1
# A[A2>0.01*A2.max()] = [255]
figure()
imshow(A)
img1[A>0.01*A.max()]=[255,0,0]
figure()
imshow(img1)
show()
