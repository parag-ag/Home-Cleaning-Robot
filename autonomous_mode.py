import RPi.GPIO as gpio         
from time import sleep
import random
from sensor import distance
import sys

def check_front() :
    dist = distance()

    if dist < 15 :
        print('too close!',dist)
        reverse(2)
        dist = distance()
        if dist < 15 :
            print('too close!',dist)
            turn_left(3)
            reverse(2)
            dist = distance()
            if dist < 15 :
                print('too close! giving up :(',dist)
                sys.exit()

def autonomy(robot):
    # tf = 3
    # x = random.randrange(0,4)

    # if x == 0 :
    #     for y in range(30) :
    #         check_front()
    #         robot.forward(tf)
    # elif x == 1 :
    #     for y in range(30) :
    #         check_front()
    #         robot.backward(tf)
    # elif x == 2 :
    #     for y in range(30) :
    #         check_front()
    #         robot.turn_left(tf)
    # elif x == 3 :
    #     for y in range(30) :
    #         check_front()
    #         robot.turn_right(tf)
    tf = 3
    x = random.randrange(0, 100) * 0.05
    dist = distance()
    print(dist)
    if dist > 15:
        robot.forward(tf)
    else:
        robot.turn_left(x)

            
def start_auto_clean(robot) :
    while True :
        try:
            autonomy(robot)
        except KeyboardInterrupt:
            pass



