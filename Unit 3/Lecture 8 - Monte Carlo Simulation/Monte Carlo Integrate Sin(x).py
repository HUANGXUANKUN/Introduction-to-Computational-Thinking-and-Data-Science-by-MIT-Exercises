# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 23:46:44 2018

@author: HuangXuankun
"""

import random,math,numpy,scipy


def testNeedleInSin(x,y):
    y1 = math.sin(x)
    if y <= y1:
        return True
    return False

def throwNeedles(numNeedles):
    numNeedlesInShape = 0
    for needle in range(numNeedles):
        xRan = random.uniform(0.0,math.pi)
        yRan = random.random()
        if testNeedleInSin(xRan,yRan):
            numNeedlesInShape += 1
    return float(numNeedlesInShape /numNeedles)

def calArea(ratio,shapeSize):
    return float(ratio * shapeSize)

def getEst(numNeedles,numTrials):
    estResults = []
    for trial in range(numTrials):
        areaRatio = throwNeedles(numNeedles)
        estResult = calArea(areaRatio,math.pi)
        estResults.append(estResult)
    estAreaMean = sum(estResults)/len(estResults)
    estStd = numpy.std(estResults)
    print('estArea =',estAreaMean,'estStd =',estStd,'num of needles =',numNeedles)
    return estAreaMean,estStd

def estArea(precision,numTrials):
    numNeedles = 1000
    estStd = getEst(numNeedles,numTrials)[1]
    while estStd*1.96 > precision:
        numNeedles *= 2
        estStd = getEst(numNeedles,numTrials)[1]
        
estArea(0.05,1000)

        
    
    
            
        
        
   
