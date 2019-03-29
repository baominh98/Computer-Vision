import math#PIL matplotlib numpy scipy opencv
def check(a):
    for i in range(0,len(a)):
        if(a[i] != '-'):
            if(ord(a[i]) <48 or ord(a[i])>57):
                return False
    if(a ==''):
        return False
    return True

while 1:
    a = input('Nhap a: ')
    b = input('Nhap b: ')
    c = input('Nhap c: ')
    if(check(a)!= True):
        print('sai dinh dang a')
        continue
    if(check(b)!= True):
        print('sai dinh dang b')
        continue
    if(check(c)!= True):
        print('sai dinh dang c')
        continue
    a = int(a)
    b = int(b)
    c = int(c)
    if (a == 0):
        print('Phuong Trinh la phuong trinh bat nhat\nx=',-c/b)
        continue
    delta = b*b - 4*a*c
    print('Delta:',delta)
    if(delta>0):
        print('Phuong trinh co 2 nghiem:')
        x1 = (-b-math.sqrt(delta))/(2*a)
        x2 = (-b+math.sqrt(delta))/(2*a)
        print('x1:',x1,'\nx2:',x2)
    elif(delta == 0):
        x=-b/2*a
        print('Phuong trinh co 1 nghiem duy nhat:\nx=',x)
    else:
        print('Phuong trinh vo nghiem')
    i = input('Ban co muon tiep tuc:')
    if(i == 'no' or i == 'No' or i == ''):
        break