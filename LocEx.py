import cv2
from PIL import Image
from pylab import *

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

def main():
    img = array(
        Image.open("/home/caohuy/Python/20190304_103428.jpg").convert('L'))  # convert('L'))=>trang den
    gray()
    title('Anh Goc')
    imshow(img)
    x, y = img.shape
    gauss = np.random.normal(0, 20, img.shape)
    noisyImg = np.around(img + gauss)
    # Make sure pixel value is between 0-255
    noisyImg = (noisyImg - noisyImg.min()) * 255 / (noisyImg.max() - noisyImg.min())
    noisyImg = noisyImg.astype(uint8)
    figure()
    title('noisyImg')
    imshow(noisyImg)
    print(str(x) + 'x' + str(y))
    # Loc Median
    for i in range(x):
        for j in range(y):
            imgout = tinhmedian(noisyImg, i, j)

    figure()
    title('Loc Median tu lam')
    imshow(imgout)

    maskSize = 3  # so cac phan tu xung quanh de lay trung binh: (5x5)
    imgOut1 = cv2.medianBlur(noisyImg, 3)
    figure()
    title('Loc Median')
    imshow(imgOut1)
    show()
main()