# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 22:13:33 2018

@author: HuangXuankun
"""

def solveit(test):
    """ test, a function that takes an int parameter and returns a Boolean
        Assumes there exists an int, x, such that test(x) is True
        Returns an int, x, with the smallest absolute value such that test(x) is True 
        In case of ties, return any one of them. 
    """
    testNo = 0
    while True:
        if test(testNo):
            break
        testNo += 1
    return testNo

#### This test case prints 49 ####
def f(x):
    return (x+15)**0.5 + x**0.5 == 15
print(solveit(f))

def f(x):
    return x == 0
print(solveit(f))