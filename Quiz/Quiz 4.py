# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 17:19:42 2018

@author: HuangXuankun
"""

def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    
    def max_sum(L, seqLen):
        numResult = len(L) - seqLen +1
        resultMax = 0
        for i in range(numResult):
            resultTemp = sum(L[i:i+seqLen])
            if resultTemp > resultMax:
                resultMax = resultTemp
            resultTemp = 0
        return resultMax
    
    resultMax = 0
    for i in range(1,len(L)+1):
        resultTemp = max_sum(L,i)
        if resultTemp > resultMax:
            resultMax = max_sum(L,i)
            
    return resultMax
        

print(max_contig_sum([1,-2,9,3,5,-9,-6]))