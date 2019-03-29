from   PIL import Image
from pylab import *
def ConvertToGray(im):#Ham chuyen trang den
    return im[:,:,0]*0.2126+im[:,:,1]*0.7152+im[:,:,2]*0.0722
im = Image.open('/home/caohuy/Pictures/hinh-anh-anime-Miku-de-thuong.jpg')
# im = Image.open(a)
imarray = array(im) #chuyen anh ve dinh dang array
#print (im.mode)# hien Che Do mau truoc khi chuyen array
imshow(imarray)
title('Anh Mau')
show()

#figure() #chuyen mang thanh 1 chieu
gray()

if im.mode =='RGB':
    imConvert = ConvertToGray(imarray)
    imshow(imConvert)
else:
    print('Incorrect')
title('Anh Trang Den')
show()