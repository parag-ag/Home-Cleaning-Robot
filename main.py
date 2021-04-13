# from robot import rhode
from time import sleep
from autonomous_mode import start_auto_clean
from manual_mode import start_manual_mode
import sys
import cgi


# form = cgi.FieldStorage()
# searchterm =  form.getvalue('searchbox')            # 'searchbox' is input-name
# if "start_bot" in form

left1 = 24
left2 = 23
right1 = 22
right2 = 27
en = 25

print("Home Cleaning Robot")
print("Press enter to start the robot...")
input()

print("\nBooting up Rhodes...")
# robot1 = rhode(left1, left2, right1, right2, en)
sleep(1)
print("\nBoot Complete. Select mode of cleaning:")
print("1. Automatic Cleaning")
print("2. Manual Cleaning")
while(1):
    n = int(input())
    if n == 1:
        print("Starting automatic cleaning. Press CTRL+C to stop...")
        start_auto_clean()
        break
    elif n == 2:
        print("Manual mode selected:")
        start_manual_mode()
        break
    else:
        print("Wrong choice given. Re-enter your choice: ")
