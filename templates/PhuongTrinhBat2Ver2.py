import math#PIL matplotlib numpy scipy opencv
while 1:
    try:
        a = int(input('Nhap a: '))
        b = int(input('Nhap b: '))
        c = int(input('Nhap c: '))
    except Exception:
        print('Vui Long Nhap So')
        continue
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
    i = input('Ban co muon tiep tuc:\n\tYes\n\tNo\n\t')
    if(i == 'No' or i != 'Yes'):
        break