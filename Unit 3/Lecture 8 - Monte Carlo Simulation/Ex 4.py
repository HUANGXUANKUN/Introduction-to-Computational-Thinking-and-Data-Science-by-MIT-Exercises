# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 22:37:42 2018

@author: HuangXuankun
"""
import random
def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    ballsList = [1,1,1,2,2,2]
    numSameColor = 0
    for trail in range(numTrials):
        balls = drawBalls(ballsList,3)
        if ifSameColor(balls):
            numSameColor += 1
#            print('+1!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    return numSameColor/numTrials

def drawBalls(ballsList,numDraw):
    ballsListA = ballsList.copy()
#    print(ballsListA)
    balls = []
    for draw in range(numDraw):
        pick = random.choice(ballsListA)
        balls.append(pick)
        ballsListA.remove(pick)
#        print(pick,ballsListA)
#    print(balls)
    return balls

def ifSameColor(balls):
    if balls[0] == balls[1] and balls[0] == balls[2]:
        return True
    return False

result = noReplacementSimulation(5000)
print(result)