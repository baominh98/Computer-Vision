from pylab import *


def Tong(N, Ak):
    T = 0
    for i in range(6):
        T = N[i] + Ak[i] + T
    return T


N = np.zeros(6)
Y = np.zeros(6)
for i in range(6):
    N[i] = input("Nhap So lan tung So " + str(i+1) + ": ")
Ak = np.ones(6)
T = Tong(N,Ak)
for i in range(6):
    Y[i] = (N[i] + Ak[i])/T
print(Y)