import RPi.GPIO as gpio         
from time import sleep

def distance(measure='cm'):
    gpio.setmode(gpio.BCM)
    gpio.setup(32,gpio.OUT)
    gpio.setup(36,gpio.IN)

    gpio.output(32,False)
    try:
        while gpio.input(36) == 0 :
            nosig = time.time()

        while gpio.input(36) == 1 :
            sig = time.time()

        tl = sig - nosig

        if measure == 'cm':
            distance = tl / 0.000058
        elif measure == 'in':
            distance = tl / 0.000148 
        else:
            print('improper choice of measurement : in or cm')
            distance = None
        
        #gpio.cleanup()
        return distance

    except:
        distance = 100
        #gpio.cleanup()
        return distance