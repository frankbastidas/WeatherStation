import RPi.GPIO as GPIO

class PIthing(object):
    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)                

    def outpin(self,pin_out):
        GPIO.setup(pin_out,GPIO.OUT)

    def inpin(self,pin_in):
        GPIO.setup(pin_in,GPIO.IN,GPIO.PUD_UP)

    def readpin(self,pin_read):
        return GPIO.input(pin_read)

    def writepin(self,pin_write,value):
        GPIO.output(pin_write,value)

    def gpioend(self):
        GPIO.cleanup()
