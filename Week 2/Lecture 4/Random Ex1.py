# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 17:16:38 2018

@author: HuangXuankun
"""

import random
from collections import OrderedDict
def genEven():
    '''
    Returns a random even number x, where 0 <= x < 100
    '''
    result = random.randint(0,99)
    if result % 2 != 0:
        result = genEven()
    
    return result

#print(genEven())

def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    for num in range(9+1,21):
        if num % 2 == 0:
            return num
        
def stochasticNumber():
    '''
    Stochastically generates and returns a uniformly distributed even number between 9 and 21
    '''
    while True:
        result = random.randint(9+1,21-1)
        if result % 2 == 0:
            return result
        
#print(stochasticNumber())
def dist3():
    return int(random.random() * 10)

def dist4():
    return random.randrange(0, 10)

def dist1():
    return random.random() * 2 - 1

def dist2():
    if random.random() > 0.5:
        return random.random()
    else:
        return random.random() - 1 

def testDist():
    dist3Dict = {}
    for i in range(10):
        resultA = dist1()
        if resultA not in dist3Dict:
            dist3Dict[resultA] = 1
        else:
            dist3Dict[resultA] += 1
    
    dist4Dict = {}
    for i in range(10):
        resultA = dist2()
        if resultA not in dist4Dict:
            dist4Dict[resultA] = 1
        else:
            dist4Dict[resultA] += 1
    dist3Dict = OrderedDict(sorted(dist3Dict.items()))
    dist4Dict = OrderedDict(sorted(dist4Dict.items()))
    print(dist3Dict)
    print(dist4Dict)
            
testDist()

            
    
    