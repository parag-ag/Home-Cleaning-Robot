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

def autonomy():
    tf = 0.030
    x = random.randrange(0,4)

    if x == 0 :
        for y in range(30) :
            check_front()
            forward(tf)
    elif x == 1 :
        for y in range(30) :
            check_front()
            backward(tf)
    elif x == 2 :
        for y in range(30) :
            check_front()
            turn_left(tf)
    elif x == 3 :
        for y in range(30) :
            check_front()
            turn_right(tf)
            
def start_auto_clean(robot) :
    for z in range(10) :
        autonomy()



