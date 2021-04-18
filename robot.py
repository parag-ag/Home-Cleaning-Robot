import RPi.GPIO as GPIO          
from time import sleep

class rhode():
    current_dir = 1             # To store current location

    def __init__(self, left1, left2, right1, right2, en, clean_pin):
        '''
        Initializing the robot
        '''
        self.left1 = left1
        self.left2 = left2
        self.right1 = right1
        self.right2 = right2
        self.en = en
        self.clean_pin = clean_pin

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(in1,GPIO.OUT)
        GPIO.output(in1, GPIO.LOW)

        GPIO.setup(self.left1,GPIO.OUT)
        GPIO.setup(self.left2,GPIO.OUT)
        GPIO.setup(self.en,GPIO.OUT)
        GPIO.output(self.left1,GPIO.LOW)
        GPIO.output(self.left2,GPIO.LOW)
        GPIO.setup(self.right1,GPIO.OUT)
        GPIO.setup(self.right2,GPIO.OUT)
        GPIO.output(self.right1,GPIO.LOW)
        GPIO.output(self.right2,GPIO.LOW)
        p=GPIO.PWM(self.en,1000)
        p.start(25)
        print("\n")
        print("The default speed & direction of motor is LOW & Forward.....")
        print("r-right(90) s-stop f-forward b-backward l-left(90) e-exit")
        print("\n")    

    def forward(self, sleep_time = 1):
        print("forward")
        GPIO.output(self.left1,GPIO.HIGH)
        GPIO.output(self.left2,GPIO.LOW)
        GPIO.output(self.right1,GPIO.HIGH)
        GPIO.output(self.right2,GPIO.LOW)
        sleep(sleep_time)
    
    def stop(self):
        print("stop")
        GPIO.output(self.left1,GPIO.LOW)
        GPIO.output(self.left2,GPIO.LOW)
        GPIO.output(self.right1,GPIO.LOW)
        GPIO.output(self.right2,GPIO.LOW)

    def turn_right(self, sleep_time = 1):
        print("turning right")
        GPIO.output(self.left1,GPIO.HIGH)
        GPIO.output(self.left2,GPIO.LOW)
        GPIO.output(self.right1,GPIO.LOW)
        GPIO.output(self.right2,GPIO.HIGH)
        sleep(sleep_time)
        self.stop()

    def turn_left(self, sleep_time = 1):
        print("turning left")
        GPIO.output(self.left1,GPIO.LOW)
        GPIO.output(self.left2,GPIO.HIGH)
        GPIO.output(self.right1,GPIO.HIGH)
        GPIO.output(self.right2,GPIO.LOW)
        sleep(sleep_time)
        self.stop()

    def backward(self, sleep_time = 1):
        print("backward")
        GPIO.output(self.left1,GPIO.LOW)
        GPIO.output(self.left2,GPIO.HIGH)
        GPIO.output(self.right1,GPIO.LOW)
        GPIO.output(self.right2,GPIO.HIGH)
        sleep(sleep_time)