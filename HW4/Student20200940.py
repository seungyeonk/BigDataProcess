#!/usr/bin/python3
import numpy as np
from os import listdir
import operator
import sys
trainingfile = sys.argv[1]
testfile = sys.argv[2]
def autoNorm(dataSet):
    min_Vals = dataSet.min(0)
    max_Vals = dataSet.max(0)
    ranges = max_Vals - min_Vals
    normDataSet = np.zeros(np.shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - np.tile(min_Vals, (m, 1))
    normDataSet = normDataSet / np.tile(ranges, (m, 1))
    return normDataSet, ranges, min_Vals

def classify0(inX, dataSet, labels, k):
    dataSize = dataSet.shape[0]
    diffMat = np.tile(inX, (dataSize, 1))-dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


def makevector(filename) :
    returnVect = np.zeros((1, 1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0, 32*i+j] = int(lineStr[j])
    return returnVect


def test(k):
    labels = []
    trainingFileList = listdir(trainingfile)
    m = len(trainingFileList)
    trainingMat = np.zeros((m, 1024))
    for i in range(m):
        fullfileName = trainingFileList[i]
        fileName = fullfileName.split('.')[0]
        classNum = int(fileName.split('_')[0])
        labels.append(classNum)
        trainingMat[i, :] = makevector('%s/%s' % (trainingfile, fullfileName))
    testFileList = listdir(testfile)
    errCount = 0
    nTest = len(testFileList)
    for i in range(nTest):
        fullfileName = testFileList[i]
        fileName = fullfileName.split('.')[0]
        classNum = int(fileName.split('_')[0])
        vectorUnderTest = makevector('%s/%s' % (testfile, fullfileName))
        classifierResult = classify0(vectorUnderTest, trainingMat, labels, k)
        if (classifierResult != classNum) :
            errCount += 1
    print(int(errCount / nTest * 100))

if __name__ == "__main__":
	for i in range(1, 21):
    		test(i)

