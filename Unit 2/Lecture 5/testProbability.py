# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 10:08:08 2018

@author: HuangXuankun
"""

import random
random.seed(0)

def rollDie():
    '''returns a random int between 1 and 6 '''
    return random.choice([1,2,3,4,5,6])

def testRoll(n = 10):
    result = ''
    for i in range(n):
        result += str(rollDie())
#    print(result)
    
testRoll(5) 

def runSim(goal, numTrials):
    total = 0
    for i in range(numTrials):
        result = ''
        for i in range (len(goal)):
            result += str(rollDie())
        if result == goal:
            total += 1
    estProbability = round(total/numTrials, 8)        
    print('Actual probability =', round(1/(6**len(goal)), 8))
    print('Estimated probability =', estProbability)

runSim('11111', 1000000)