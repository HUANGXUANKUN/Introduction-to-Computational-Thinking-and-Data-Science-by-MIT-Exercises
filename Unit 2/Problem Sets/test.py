# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 11:48:38 2018

@author: HuangXuankun
"""
import math
import random

import ps2_visualize
import pylab

##################
## Comment/uncomment the relevant lines, depending on which version of Python you have
##################

# For Python 3.5:
#from ps2_verify_movement35 import testRobotMovement
# If you get a "Bad magic number" ImportError, you are not using Python 3.5 

# For Python 3.6:
from ps2_verify_movement36 import testRobotMovement
# If you get a "Bad magic number" ImportError, you are not using Python 3.6


# === Provided class Position
class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: number representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        angle = float(angle)
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

    def __str__(self):  
        return "(%0.2f, %0.2f)" % (self.x, self.y)


class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        self.width = width
        self.height = height
        self.tileStatus = {}
        
    
    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        intX = int(pos.getX())
        intY = int(pos.getY())
        
        self.tileStatus[(intX, intY)] = True        
        

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        pos = (m, n)
        if pos in self.tileStatus:
            if self.tileStatus[pos] == True:
                return True
        
        return False
            
            
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        tileNumber = self.width * self.height
        return tileNumber
    
    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        tilesCleaned = 0
        for tile in self.tileStatus:
            if tile:
                tilesCleaned += 1
                
        return tilesCleaned

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        ranX = random.randrange(0, self.width)
        ranY = random.randrange(0, self.height)
        
        return (Position(ranX, ranY))

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        posX = pos.getX()
        posY = pos.getY()
        if posX >= 0 and posX < self.width:
            if posY >= 0 and posY < self.height:
                return True
            
        return False

# ----> We tried to clean tile at position (0.6, 0.3), which should have resulted in the number of clean tiles increasing.
# === Problem 2
class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.room = room
        self.speed = speed
        self.position = room.getRandomPosition()
        self.direction = random.randint(0,359)
        self.room.cleanTileAtPosition(self.position)
        
    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.position
    
    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.direction

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        self.position = position
        return self.position

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.direction = direction
        return self.direction

    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
#        self.position = self.position.getNewPosition(self.direction, self.speed)
#        self.room.cleanTileAtPosition(self.position)       
        raise NotImplementedError

# === Problem 3
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current
    direction; when it would hit a wall, it *instead* chooses a new direction
    randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        
        newPos = self.position.getNewPosition(self.direction, self.speed)
        if (newPos.getX() > 0 and newPos.getX() < self.room.width) and (newPos.getY() > 0 and newPos.getY() < self.room.height):
                self.position = newPos
                self.room.cleanTileAtPosition(self.position)
        else:
            self.direction = random.randint(0,359)
            self.updatePositionAndClean()

def runSimulation(speed, width, height,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. StandardRobot or
                RandomWalkRobot)
    """

    room = RectangularRoom(width,height)
    roomSize = room.getNumTiles()
    robot = robot_type(room,speed)
    i = 0
    while i <= 5:
        robot.updatePositionAndClean()
        i+=1
    print('robot room has',robot.room.getNumCleanedTiles(),'clean tiles ')
    print('Room has',room.getNumCleanedTiles(),'clean tiles ')
    
#runSimulation(1.0, 8, 8, StandardRobot)
class objecta(object):
    def __init__(self,a):
        self.a = a
    def aPlus1(self):
        self.a += 1

class A(object):
    def __init__(self,a,b):
        self.A = a
        self.b = b
    def aPlus1(self):
        self.A.aPlus1()
    def bPlus1(self):
        self.b += 1
        
a = objecta(3)
b = 4
sample = A(a,b)
sample.aPlus1()
sample.bPlus1()
print(a,sample.A)
print(b,sample.b)
