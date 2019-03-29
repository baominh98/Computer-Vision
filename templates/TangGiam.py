n= int(input('Nhap So Luong Phan Tu:'))
a = []
for i in range(n):
    a.append(float(input('Phan Tu Thu %d: '%(i+1))))
b='1'
while(b!='4'):
    b = input('Tuy Chon:\n 1:Nhap\n 2:Xep Tang\n 3:Xep Giam\n 4:Thoat\n ')
    if(b == '1'):
        n= int(input('Nhap So Luong Phan Tu:'))
        a = []
        for i in range(n):
            a.append(float(input('Phan Tu Thu %d: '%(i+1))))
    if(b == '2'):
        print('Tang Dan:')
        for i in range(0,n):
            for j in range(i,n):
                if(a[j]<a[i]):
                    a[j] = a[j]+a[i]
                    a[i] = a[j]-a[i]
                    a[j] = a[j]-a[i]
        print(a)
    if(b == '3'):
        print('Giam Dan:')
        for i in range(0,n):
            for j in range(i,n):
                if(a[j]>a[i]):
                    m = a[j]
                    a[j]=a[i]
                    a[i]=m
        print(a)