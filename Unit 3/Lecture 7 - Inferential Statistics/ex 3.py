# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 12:55:05 2018

@author: HuangXuankun
"""

def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if len(L) == 0:
        return float('NaN')
    sumL = 0
    for string in L:
        sumL += len(string)
    mean = sumL / len(L)
    
    diffSqr_sum = 0 
    for string in L:
        diffSqr_sum += (len(string) - mean) ** 2
    return round((diffSqr_sum / len(L))**0.5,4)

#A = ['a', 'z', 'p']
#print(stdDevOfLengths(A))
#L = ['apples', 'oranges', 'kiwis', 'pineapples']
#print(stdDevOfLengths(L))

def coeVar(L):
    sumL = sum(L)
    mean = sumL/len(L)
    diffSqr_sum = 0 
    for i in L:
        diffSqr_sum += (i - mean) ** 2
    std = (diffSqr_sum / len(L))**0.5
    result = std/mean
    print(result)

coeVar([10, 4, 12, 15, 20, 5])

        