# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 18:59:48 2018

@author: HuangXuankun
"""
import pylab, random

#def flipCoin(numFlips):
#    '''
#    Returns the result of numFlips coin flips of a biased coin.
#
#    numFlips (int): the number of times to flip the coin.
#
#    returns: a list of length numFlips, where values are either 1 or 0,
#    with 1 indicating Heads and 0 indicating Tails.
#    '''
#    with open('coin_flips.txt','r') as f:
#        all_flips = f.read()
#    flips = random.sample(all_flips, numFlips)
#    return [int(flip == 'H') for flip in flips]


#def getMeanAndStd(X):
#    mean = sum(X)/float(len(X))
#    tot = 0.0
#    for x in X:
#        tot += (x - mean)**2
#    std = (tot/len(X))**0.5
#    return mean, std
#
#meanOfMeans, stdOfMeans = [], []
#sampleSizes = range(10, 500, 50)
#
#def clt():
#    for sampleSize in sampleSizes:
#        sampleMeans = []
#        for t in range(20):
#            sample = flipCoin(sampleSize)## FILL THIS IN
#            sampleMeans.append(getMeanAndStd(sample)[0])
#            print(sample,sampleMeans)
#        meanOfMeans.append(sum(sampleMeans)/20)
#        stdOfMeans.append(getMeanAndStd(sampleMeans)[1])

#
#clt()
#pylab.figure(1)
#pylab.errorbar(sampleSizes, meanOfMeans,
#               yerr = 1.96*pylab.array(stdOfMeans),
#               label = 'Est. mean and 95% confidence interval')
#pylab.xlim(0, max(sampleSizes) + 50)
#pylab.axhline(0.65, linestyle = '--',
#              label = 'True probability of Heads')
#pylab.title('Estimates of Probability of Heads')
#pylab.xlabel('Sample Size')
#pylab.ylabel('Fraction of Heads (minutes)')
#pylab.legend(loc = 'best')
#pylab.show()

def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

def drawCard(numDraws):
    '''
    Return the result of num of five star cards being drew.
    
    numDraws = the number of times to draw a card continueously

    returns: a list of cards drew, where values are either 1 or 0,
    with 1 indicating 5 stars card being draw.
    '''
    cards = []
    for n in range(numDraws):
        cardDrew = random.randint(1,100)
        cards.append(cardDrew)
    return [int(card == 1) for card in cards]

meanOfMeans, stdOfMeans = [], []
drawNumSizes = range(10,1000,10)

def clt():
    for drawNum in drawNumSizes:
        fiveStarsMeans = []
        for t in range(20):
            fiveStarsDrew = drawCard(drawNum)
            fiveStarsMeans.append(getMeanAndStd(fiveStarsDrew)[0])
        meanOfMeans.append(getMeanAndStd(fiveStarsMeans)[0])
        stdOfMeans.append(getMeanAndStd(fiveStarsMeans)[1])

clt()
pylab.figure(1)
pylab.errorbar(drawNumSizes, meanOfMeans,
               yerr = 1.96*pylab.array(stdOfMeans),
               label = 'Est. mean and 95% confidence interval')
pylab.xlim(0, max(drawNumSizes) + 50)
pylab.axhline(0.01, linestyle = '--',
              label = 'True probability of 5StarsDraw')
pylab.title('Estimates of Probability of 5StarsDraw')
pylab.xlabel('Number of draws')
pylab.ylabel('Probability of 5Stars being drew')
pylab.legend(loc = 'best')
pylab.show()

