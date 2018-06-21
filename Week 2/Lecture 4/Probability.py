# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 10:08:08 2018

@author: HuangXuankun
"""

import random

def rollDie():
    '''returns a random int between 1 and 6 '''
    return random.choice([1,2,3,4,5,6])

def testRoll(n = 10):
    result = ''
    for i in range(n):
        result += str(rollDie())
    print(result)
    
testRoll(5)