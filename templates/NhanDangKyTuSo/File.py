import numpy
def Mode_open(add_file):
    return open(add_file)
def Mode_Doc_Ghi(add_file):
    return open(add_file,'r+')
def Mode_Ghi_Moi(add_file):
    return open(add_file,'w')
def Mode_Doc_Ghi_Moi(add_file):
    return open(add_file,'w+')
def Mode_Ghi_Them(add_file):
    return open(add_file,'a')
def Mode_Doc_Ghi_Them(add_file):
    return open(add_file,'a+')
def Ghi_Vector_Vao_file(file,hogVector):
    x = len(hogVector)
    file.write('')
    for i in range(x):
        file.write(str(hogVector[i]) + ' ')
    file.write('\n')
def LayVector_file(add_file):
    # Vector = numpy.empty(10)
    file = Mode_open(add_file)
    a = file.readline()
    b= numpy.zeros([10,1764])
    x=0
    y=0
    c=''
    while(a):
        for i in range(len(a)):
            if a[i]!= ' ':
                if a[i]!= '\n':
                    c = c + a[i]
            else:
                b[x,y] = float(c)
                y=y+1
                c =''
        a = file.readline()
        x=x+1
        y=0
    file.close()
    return b
