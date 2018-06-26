# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 17:48:24 2018

@author: HuangXuankun
"""

def max_sum(L, seqLen):
    numResult = len(L) - seqLen +1
    resultMax = 0
    for i in range(numResult):
        resultTemp = sum(L[i:i+seqLen])
        if resultTemp > resultMax:
            resultMax = resultTemp
        resultTemp = 0
    return resultMax

a = [1,2,3,4,5]
print(max_sum(a,2))