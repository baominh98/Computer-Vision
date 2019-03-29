from PIL import Image
from pylab import *
from scipy import signal

def matran_median(a, x_vitri, y_vitri, x, y, size):
    b = np.ones(size*size)
    temb = 0
    for i in range(-int(size/2), int(size/2)+1):
        for j in range(-int(size/2), int(size/2)+1):
            if x_vitri-i<0 or y_vitri-j<0 or x_vitri-i>=x or y_vitri-j>=y:
                    continue
            b[temb] = a[x_vitri - i, y_vitri - j]
            temb = temb + 1
    b = np.sort(b)
    return b

def tinhmedian(a,x,y,size):
    for x_vitri in range(x):
        for y_vitri in range(y):
            ma_tran = matran_median(a, x_vitri, y_vitri,x,y,size)
            c = a
            tb = ma_tran[int(len(ma_tran) / 2)]
            c[x_vitri - 1, y_vitri - 1] = tb
    return c

def matrantrungbinh(img1, x_vitri, y_vitri, x, y, size):
    b = np.ones(size*size)/(size*size)
    temb = 0
    for i in range(-int(size/2), int(size/2)+1):
        for j in range(-int(size/2), int(size/2)+1):
            if x_vitri-i<0 or y_vitri-j<0 or x_vitri-i>=x or y_vitri-j>=y:
                continue
            b[temb] = img1[x_vitri - i, y_vitri - j]
            temb = temb + 1
    return b

def tinhTrungBinh(img1,x,y,size):
    for x_vitri in range(x):
        for y_vitri in range(y):
            ma_tran_trung_binh = matrantrungbinh(img1, x_vitri, y_vitri,x,y,size)
            imgOut = img1
            Tong = 0
            for i in range(9):
                Tong = Tong + ma_tran_trung_binh[i]
            tb = float(Tong / (size*size))
            imgOut[x_vitri - 1, y_vitri - 1] = tb
    return imgOut

def Loc(img, CheDoLoc, size):
        # while(1):
        # img = array(Image.open("/home/caohuy/Python/1.jpg").convert('L'))  # convert('L'))=>trang den
        # gray()
# # Lam Nhieu Anh
#         gauss = np.random.normal(0, 30, img.shape)
#         noisyImg = np.around(img + gauss)
#         # Make sure pixel value is between 0-255
#         noisyImg = (noisyImg - noisyImg.min()) * 255 / (noisyImg.max() - noisyImg.min())
#         noisyImg = noisyImg.astype(uint8)
# ==============
        x, y = img.shape
        print('Kich Thuoc Anh:' + str(x) + 'x' + str(y))
        if CheDoLoc == '1':
                imgout = tinhmedian(img,x,y,size)
                figure()
                title('Loc Median')
                imshow(imgout)
                return imgout
        if CheDoLoc == '2':
                imgout = tinhTrungBinh(img,x,y,size)
                figure()
                title('Loc Trung Binh')
                imshow(imgout)
                return imgout