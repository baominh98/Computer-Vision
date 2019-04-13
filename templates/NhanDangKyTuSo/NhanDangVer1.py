import numpy
import HOG
import RutVector
import File

def GetSquareEuclideanDist(x,y):
    return numpy.sum((x-y)**2)
def EuclideanClassifier(file):
    testFeature = HOG.HOG_funtion(file)
    distanceTo = numpy.empty(10)
    FeatureMean = numpy.empty([10,1764])
    FeatureMean = File.LayVector_file('VectorTB.txt')
    # FeatureMean0 = RutVector.feature(0)
    # FeatureMean1 = RutVector.feature(1)
    # FeatureMean2 = RutVector.feature(2)
    # FeatureMean3 = RutVector.feature(3)
    # FeatureMean4 = RutVector.feature(4)
    # FeatureMean5 = RutVector.feature(5)
    # FeatureMean6 = RutVector.feature(6)
    # FeatureMean7 = RutVector.feature(7)
    # FeatureMean8 = RutVector.feature(8)
    # FeatureMean9 = RutVector.feature(9)
    # distanceTo[0] = GetSquareEuclideanDist(testFeature , FeatureMean0)
    # distanceTo[1] = GetSquareEuclideanDist(testFeature , FeatureMean1)
    # distanceTo[2] = GetSquareEuclideanDist(testFeature , FeatureMean2)
    # distanceTo[3] = GetSquareEuclideanDist(testFeature , FeatureMean3)
    # distanceTo[4] = GetSquareEuclideanDist(testFeature , FeatureMean4)
    # distanceTo[5] = GetSquareEuclideanDist(testFeature , FeatureMean5)
    # distanceTo[6] = GetSquareEuclideanDist(testFeature , FeatureMean6)
    # distanceTo[7] = GetSquareEuclideanDist(testFeature , FeatureMean7)
    # distanceTo[8] = GetSquareEuclideanDist(testFeature , FeatureMean8)
    # distanceTo[9] = GetSquareEuclideanDist(testFeature , FeatureMean9)
    for i in range(10):
        distanceTo[i] = GetSquareEuclideanDist(testFeature , FeatureMean[i])
    a = distanceTo[0]
    x=0
    for i in range(10):
        if a> distanceTo[i]:
            a=distanceTo[i]
            x = i
    print(x)
def TestEuclideanClassifier(file):
    EuclideanClassifier(file)
for i in range(10):
    print('Anh So : '+ str(i))
    TestEuclideanClassifier('200anh/'+str(i)+'-4.png')