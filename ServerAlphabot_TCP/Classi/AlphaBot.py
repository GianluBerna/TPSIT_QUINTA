import time
import turtle

class AlphaBot(object):

    def __init__(self):
        self.turtle = turtle.Turtle()

    def forward(self, potenza):
        self.turtle.fd(potenza)

    """def stop(self):
        self.turtle.fd(potenza)"""

    def backward(self, potenza):
        self.turtle.bk(potenza)

    def left(self, potenza):
        self.turtle.lt(potenza)

    def right(self, potenza):
        self.turtle.right(potenza)

    def setPWMA(self, value):
        self.PWMA.ChangeDutyCycle(value)

    """
    def setPWMB(self,value):
        self.PWMB.ChangeDutyCycle(value)    
        
    def setMotor(self, left, right):
        if((right >= 0) and (right <= 100)):
            GPIO.output(self.IN1,GPIO.HIGH)
            GPIO.output(self.IN2,GPIO.LOW)
            self.PWMA.ChangeDutyCycle(right)
        elif((right < 0) and (right >= -100)):
            GPIO.output(self.IN1,GPIO.LOW)
            GPIO.output(self.IN2,GPIO.HIGH)
            self.PWMA.ChangeDutyCycle(0 - right)
        if((left >= 0) and (left <= 100)):
            GPIO.output(self.IN3,GPIO.HIGH)
            GPIO.output(self.IN4,GPIO.LOW)
            self.PWMB.ChangeDutyCycle(left)
        elif((left < 0) and (left >= -100)):
            GPIO.output(self.IN3,GPIO.LOW)
            GPIO.output(self.IN4,GPIO.HIGH)
            self.PWMB.ChangeDutyCycle(0 - left)"""

    """
    def istruction(istr, t):
    istr = istr.decode()
    command = istr.split("_")[0]
    number = int(istr.split("_")[1])
    switcher = {
        "forward": forward,
        "f": forward,
        "backward": backward,
        "b": backward,
        "right": right,
        "r": right,
        "left": left,
        "l":left
    }
    switcher[command](t, number)
        

def forward(t, number):
    t.fd(number)

def backward(t, number):
    t.bk(number)

def right(t, number):
    t.right(number)

def left(t, number):
    t.left(number)
    """
