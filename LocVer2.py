from PIL import Image
from pylab import *
from scipy import signal

def matrantrungbinh_median(a, x_vitri, y_vitri, x, y, size):
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

def tinhmedian(a, x_vitri, y_vitri,x,y,size):
    ma_tran_trung_binh = matrantrungbinh_median(a, x_vitri, y_vitri,x,y,size)
    c = a
    tb = ma_tran_trung_binh[int(len(ma_tran_trung_binh) / 2)]
    c[x_vitri - 1, y_vitri - 1] = tb
    return c

def tim_Ma_Tran_Chap1(a, x_vitri, y_vitri, x, y, size):
    b = np.ones(size*size)/(size*size)
    temb = 0
    for i in range(-int(size/2), int(size/2)+1):
        for j in range(-int(size/2), int(size/2)+1):
            if x_vitri-i<0 or y_vitri-j<0 or x_vitri-i>=x or y_vitri-j>=y:
                    continue
            b[temb] = a[x_vitri - i, y_vitri - j]
            temb = temb + 1
    return b

def tinh_Ma_Tran_Chap(img1, x_vitri, y_vitri,x,y,size):
    ma_tran_trung_binh = tim_Ma_Tran_Chap1(img1, x_vitri, y_vitri,x,y,size)
    imgOut = img1
    Tong = 0
    for i in range(9):
        Tong = Tong + ma_tran_trung_binh[i]
    tb = float(Tong / (size*size))
    imgOut[x_vitri - 1, y_vitri - 1] = tb
    return imgOut

def main():
        while(1):
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
                title('Anh Goc')
                imshow(noisyImg)
                CheDoLoc = input('\t1: Median\n\t2:TrungBinh\n\t3:Thoat\n')
                if CheDoLoc == '3':
                        break
                size =int(input('Size: '))
                if CheDoLoc == '1':
                        for i in range(x):
                                for j in range(y):
                                        imgout = tinhmedian(noisyImg, i, j,x,y,size)
                        figure()
                        title('Loc Median')
                        imshow(imgout)
                if CheDoLoc == '2':
                        for i in range(x):
                                for j in range(y):
                                        imgout = tinh_Ma_Tran_Chap(noisyImg, i, j,x,y,size)
                        figure()
                        title('Loc Trung Binh')
                        imshow(imgout)
                show()
main()