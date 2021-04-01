import RPi.GPIO as GPIO          
from time import sleep

class rhode():
    current_dir = 1             # To store current location

    def __init__(left1, left2, right1, right2, en):
        '''
        Initializing the robot
        '''
        self.left1 = left1
        self.left2 = left2
        self.right1 = right1
        self.right2 = right2
        self.en = en

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.left1,GPIO.OUT)
        GPIO.setup(self.left2,GPIO.OUT)
        GPIO.setup(self.en,GPIO.OUT)
        GPIO.output(self.left1,GPIO.LOW)
        GPIO.output(self.left2,GPIO.LOW)
        GPIO.setup(self.left1,GPIO.OUT)
        GPIO.setup(self.left2,GPIO.OUT)
        GPIO.output(self.right1,GPIO.LOW)
        GPIO.output(self.right2,GPIO.LOW)
        p=GPIO.PWM(self.en,1000)
        p.start(25)
        print("\n")
        print("The default speed & direction of motor is LOW & Forward.....")
        print("r-right(90) s-stop f-forward b-backward l-left(90) e-exit")
        print("\n")    

    def forward():
        print("forward")
        GPIO.output(left1,GPIO.HIGH)
        GPIO.output(left2,GPIO.LOW)
        GPIO.output(right1,GPIO.HIGH)
        GPIO.output(right2,GPIO.LOW)
        current_dir = 1
    
    def stop():
        print("stop")
        GPIO.output(left1,GPIO.LOW)
        GPIO.output(left2,GPIO.LOW)
        GPIO.output(right1,GPIO.LOW)
        GPIO.output(right2,GPIO.LOW)

    def turn_right():
        print("turning right")
        GPIO.output(left1,GPIO.HIGH)
        GPIO.output(left2,GPIO.LOW)
        GPIO.output(right1,GPIO.LOW)
        GPIO.output(right2,GPIO.HIGH)
        sleep(1)
        self.stop()

    def turn_left():
        print("turning left")
        GPIO.output(left1,GPIO.LOW)
        GPIO.output(left2,GPIO.HIGH)
        GPIO.output(right1,GPIO.HIGH)
        GPIO.output(right2,GPIO.LOW)
        sleep(1)
        self.stop()

    def backward():
        print("backward")
        GPIO.output(left1,GPIO.LOW)
        GPIO.output(left2,GPIO.HIGH)
        GPIO.output(right1,GPIO.LOW)
        GPIO.output(right2,GPIO.HIGH)
        current_dir = 0


if __name__ == '__main__':
    print("Hello world")
    left1 = 24
    left2 = 23
    right1 = 22
    right2 = 27
    en = 25

    robot1 = rhode(left1, left2, right1, right2, en)
    while 1:
        ins = input()
        if ins == 'f':
            robot1.forward()
        elif ins == 'b':
            robot1.backward()
        elif ins == 's':
            robot1.stop()
        elif ins == 'r':
            robot1.turn_right()
        elif ins == 'l':
            robot1.turn_left()
        elif ins == 'e':
            break
        else:
            print('Invalid Instruction Given!!') 

