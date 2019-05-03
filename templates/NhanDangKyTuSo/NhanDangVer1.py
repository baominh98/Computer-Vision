import numpy
import HOG
import File
from random import randint

def GetSquareEuclideanDist(x,y):
    return numpy.sum((x-y)**2)
def EuclideanClassifier(file):
    testFeature = HOG.HOG_funtion(file)
    distanceTo = numpy.empty(10)
    FeatureMean = numpy.empty([10,1764])
    FeatureMean = File.LayVector_file('VectorTB.txt')
    for i in range(10):
        distanceTo[i] = GetSquareEuclideanDist(testFeature , FeatureMean[i])
    a = distanceTo[0]
    x=0
    for i in range(10):
        if a> distanceTo[i]:
            a=distanceTo[i]
            x = i
    return x
def TestEuclideanClassifier(file):
    return EuclideanClassifier(file)
while(1):
    random_so = randint(0, 9)
    random_thutu = randint(1, 20)
    print('Anh So : '+ str(random_so))
    result = TestEuclideanClassifier('200anh/'+str(random_so)+'-'+str(random_thutu)+'.png')
    print(random_so, result)
    if result == random_so:
        print('Dung')
    else:
        print('sai')
        break