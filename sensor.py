import RPi.GPIO as gpio         
from time import sleep

def distance(measure='cm'):
    gpio.setmode(gpio.BCM)
    gpio.setup(12,gpio.OUT)
    gpio.setup(16,gpio.IN)

    gpio.output(12,True)
    try:
        while gpio.input(16) == 0 :
            nosig = time.time()

        while gpio.input(16) == 1 :
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