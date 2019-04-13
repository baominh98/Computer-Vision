# Nhan dang Ky tu so tu hinh anh
# input: hinh co so
# output: So o dang string
# 1: tao 20 hinh cho moi so (tong cong 200 hinh) de lam tap mau (kich thuc 64x64); 200 hinh rieng biet
# 2: tim feature vector cua tam hinh tu hinh mau: Dung thuat Toan HOG
#   sao khi lam HOG se ra dc 20 feature vector
#   Moi so se co tuong ung 20 feature vector
#   Tim vector trung binh cua moi so bang cach tinh trung binh 20 hinh cua tung so-> tim dc 10 feature vector trung binh cua moi so
# //3: So sanh khoang cach giua cac vector trung binh voi hinh input
# 3:  luu vector trung binh cua tap mau vao file text
# 4: Tao project moi doc vector trung bih tu file txt va so sanh voi vector trung binh cua input
#       feature vector cua input gan voi vector trung binh nao nhat thi do chinh la ky tu do
import HOG
import File
import numpy
def feature(j):
    V1 = numpy.empty(1764)
    V = numpy.zeros(1764)
    # for j in range(0,10):
    for i in range(1,21):
        hogVector = HOG.HOG_funtion('200anh/'+str(j)+'-'+str(i)+'.png')
        for i in range(len(hogVector)):
            V1[i] = hogVector[i]/len(hogVector)
        V = V1 + V
    return V
        # add_file = input('Nhap Duong Dan: ')
        # add_file = 'VectorTB.txt'
        # file = File.Mode_Ghi_Them(add_file)
        # File.Ghi_Vector_Vao_file(file,hogVector)
        # file.close()
