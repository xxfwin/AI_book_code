#Load data:
from numpy import *
def loadDataSet(fileName):
    dataSet = []
    f = open(fileName)
    for line in f.readlines():
        curLine = line.strip().split('\t')
        fltLine = map(float, curLine)
        dataSet.append(fltLine)
    return mat(dataSet)

#The code of the whole algorithm:
# using Euclidean Distance as distance measure and random centroid as the function of create centroids
def KMeans(dataSet, k):
    m = shape(dataSet)[0] 
    clusterAssment = mat(zeros((m, 2)))
    centroids = createCent(dataSet, k)
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        for i in range(m):
            minDist = inf;minIndex = -1
            for j in range(k): 
                distJI = distMeas(centroids[j, :], dataSet[i, :])
                if distJI < minDist:
                    minDist = distJI; minIndex = j
            if clusterAssment[i, 0] != minIndex:
                clusterChanged = True
            clusterAssment[i, :] = minIndex, minDist**2 
        print centroids
        for cent in range(k): 
            ptsInClust = dataSet[nonzero(clusterAssment[:,0].A==cent)[0]]
            centroids[cent,:] = mean(ptsInClust, axis=0) 
    return centroids, clusterAssment

#Data visualization:
import matplotlib.pyplot as plt
def showCluster(dataSet, k, clusterAssment, centroids):
    fig = plt.figure()
    plt.title("K-means")
    ax = fig.add_subplot(111)
    data = []
    for cent in range(k): 
        ptsInClust = dataSet[nonzero(clusterAssment[:,0].A==cent)[0]] 
        data.append(ptsInClust)
    for cent, c, marker in zip( range(k), ['r', 'g', 'b', 'y'], ['^', 'o', '*', 's'] ):
        ax.scatter(data[cent][:, 0], data[cent][:, 1], s=80, c=c, marker=marker)
    ax.scatter(centroids[:, 0], centroids[:, 1], s=1000, c='black', marker='+', alpha=1) 
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    plt.show()

