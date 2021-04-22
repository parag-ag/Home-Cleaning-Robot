from robot import rhode
from time import sleep
from autonomous_mode import start_auto_clean
from manual_mode import start_manual_mode
import sys
import cgi

left1 = 24
left2 = 23
right1 = 22
right2 = 27
en_left = 25
en_right = 26
clean_pin = 21

print("Home Cleaning Robot")
print("Press enter to start the robot...")
input()

print("\nBooting up Rhodes...")
robot = rhode(left1, left2, right1, right2, en_left, en_right, clean_pin)
sleep(1)
print("\nBoot Complete. Select mode of cleaning:")
print("1. Automatic Cleaning")
print("2. Manual Cleaning")
while(1):
    n = int(input())
    if n == 1:
        print("Starting automatic cleaning. Press CTRL+C to stop...")
        start_auto_clean(robot)
        break
    elif n == 2:
        print("Manual mode selected:")
        start_manual_mode(robot)
        break
    else:
        print("Wrong choice given. Re-enter your choice: ")
