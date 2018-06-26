# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 16:31:05 2018

@author: HuangXuankun
"""

def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for 
        the largest value in L then for the second largest, and so on to 
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does 
                not yield a set of multipliers such that the equation sums to 's'
    """
    if len(L) == 0:
        return 'no solution'
    
    sum_mutipliers = 0
    quotient = s // L[0]
    remainder = s % L[0]

    if remainder == 0:
        sum_mutipliers += quotient
        return sum_mutipliers
            
    else:
        result = greedySum(L[1:], remainder)
        if type(result) == int:    
            return quotient + result
        else: 
            return result
    
print(greedySum([4,2],8))
print(greedySum([4,2],9))
print(greedySum([4,2,1],9))
