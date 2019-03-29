from PIL import Image
from pylab import *
from scipy import signal

def matrantrungbinh_median(a, x, y):
    b = np.ones(9)
    temb = 0
    for i in range(0, 3):
        for j in range(0, 3):
            b[temb] = a[x - i, y - j]
            temb = temb + 1
    b = np.sort(b)
    return b


def tinhmedian(a, x, y):
    ma_tran_trung_binh = matrantrungbinh_median(a, x, y)  # type:
    tb = 0
    c = a
    # print(len(a)%2)
    if len(ma_tran_trung_binh) / 2 == 0:
        tb = ma_tran_trung_binh[int(((ma_tran_trung_binh[len(ma_tran_trung_binh) / 2] + ma_tran_trung_binh[len(ma_tran_trung_binh) / 2 + 1]) / 2) - 1)]
    else:
        tb = ma_tran_trung_binh[int(len(ma_tran_trung_binh) / 2)]
    # print(str(x) + 'x' + str(y))
    c[x - 1, y - 1] = tb
    return c

def MaTranTrungBinh(img2, x, y):
    b = np.ones(9)/9
    temb = 0
    for i in range(0, 3):
        for j in range(0, 3):
            b[temb] = img2[x - i, y - j]
            temb = temb + 1
    b = np.sort(b)
    return b


def tinhTrungBinh(img1, x, y):
    ma_tran_trung_binh = MaTranTrungBinh(img1, x, y)  # type:
    imgOut = img1
    Tong = 0
    for i in range(9):
        Tong = Tong + ma_tran_trung_binh[i]
    tb = float(Tong / 9)
    imgOut[x - 1, y - 1] = tb
    return imgOut

def main():
        img = array(Image.open("/home/caohuy/Python/20190304_103428.jpg").convert('L'))  # convert('L'))=>trang den
        gray()
# Lam Nhieu Anh
        gauss = np.random.normal(0, 30, img.shape)
        noisyImg = np.around(img + gauss)
        # Make sure pixel value is between 0-255
        noisyImg = (noisyImg - noisyImg.min()) * 255 / (noisyImg.max() - noisyImg.min())
        noisyImg = noisyImg.astype(uint8)
# ==============
        x, y = noisyImg.shape
        print('Kich Thuoc Anh:' + str(x) + 'x' + str(y))
        while(1):
                title('Anh Goc')
                imshow(noisyImg)
                CheDoLoc = input('\t1: Median\n\t2:TrungBinh\n\t3:Thoat\n')
                if CheDoLoc == '1':
                        for i in range(x):
                                for j in range(y):
                                        imgout = tinhmedian(noisyImg, i, j)
                        figure()
                        title('Loc Median')
                        imshow(imgout)
                if CheDoLoc == '2':
                        for i in range(x):
                                for j in range(y):
                                        imgout = tinhTrungBinh(noisyImg, i, j)
                        figure()
                        title('Loc Trung Binh')
                        imshow(imgout)
                if CheDoLoc == '3':
                        break
                show()
main()