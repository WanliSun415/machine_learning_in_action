from numpy import *


def loadDataSet(fileName):
    numFeat = len(open(fileName).readline().split('\t')) - 1
    dataMat = []; labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = []
        curLine = line.strip().split('\t')
        for i in range(numFeat):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelMat.append(float(curLine[-1]))
    return dataMat, labelMat


def standRegres(xArr, yArr):
    xMat = mat(xArr); yMat = mat(yArr).T
    xTx = xMat.T * xMat
    if linalg.det(xTx) == 0.0:
        print("This matrix is singular, cannot do inverse")
        return
    ws = xTx.I * xMat.T * yMat
    return ws


def lwlr(testPoint, xArr, yArr, k=1.0):
    xMat = mat(xArr); yMat = mat(yArr).T
    m = shape(xMat)[0]
    weights = mat(eye(m))
    for j in range(m):
        diffMat = testPoint - xMat[j, :]
        weights[j, j] = exp(diffMat * diffMat.T / (-2 * k**2))
    xTx = xMat.T * weights * xMat
    if linalg.det(xTx) == 0.0:
        print("This matrix is singular, cnanot do inverse")
        return
    ws = xTx.I * xMat.T * weights * yMat
    return testPoint * ws


def lwlrTest(testArr, xArr, yArr, k=1.0):
    m = shape(testArr)[0]
    yHat = zeros(m)
    for i in range(m):
        yHat[i] = lwlr(testArr[i], xArr, yArr, k)
    return yHat


def rssError(yArr, yHatArr):
    return ((yArr-yHatArr) ** 2).sum()

if __name__ == '__main__':
    # xArr, yArr = loadDataSet('ex0.txt')
    # ws = standRegres(xArr, yArr)
    # xMat = mat(xArr); yMat = mat(yArr)
    # import matplotlib.pyplot as plt
    # fig = plt.figure()
    # ax = fig.add_subplot(111)
    # ax.scatter(xMat[:, 1].flatten().A[0], yMat.T[:, 0].flatten().A[0])
    # xCopy = xMat.copy()
    # xCopy.sort(0)
    # yHat = xCopy*ws
    # ax.plot(xCopy[:, 1], yHat)
    # plt.show()

    # xArr, yArr = loadDataSet('ex0.txt')
    # yHat = lwlrTest(xArr, xArr, yArr, 0.03)
    # xMat = mat(xArr); yMat = mat(yArr)
    # srtInd = xMat[:, 1].argsort(0)
    # xSort = xMat[srtInd][:, 0, :]
    # import matplotlib.pyplot as plt
    # fig = plt.figure()
    # ax = fig.add_subplot(111)
    # ax.plot(xSort[:, 1], yHat[srtInd])
    # ax.scatter(xMat[:, 1].flatten().A[0], yMat.T.flatten().A[0], s=2, c='red')
    # plt.show()

    abX, abY = loadDataSet('abalone.txt')
    yHat01 = lwlrTest(abX[0: 99], abX[0: 99], abY[0: 99], 0.1)
    yHat1 = lwlrTest(abX[0: 99], abX[0: 99], abY[0: 99], 1)
    yHat10 = lwlrTest(abX[0: 99], abX[0: 99], abY[0: 99], 10)
    print(rssError(abY[0: 99], yHat01.T))
    print(rssError(abY[0: 99], yHat1.T))
    print(rssError(abY[0: 99], yHat10.T))
    yHat01 = lwlrTest(abX[100: 199], abX[0: 99], abY[0: 99], 0.1)
    yHat1 = lwlrTest(abX[100: 199], abX[0: 99], abY[0: 99], 1)
    yHat10 = lwlrTest(abX[100: 199], abX[0: 99], abY[0: 99], 10)
    print(rssError(abY[100: 199], yHat01.T))
    print(rssError(abY[100: 199], yHat1.T))
    print(rssError(abY[100: 199], yHat10.T))
