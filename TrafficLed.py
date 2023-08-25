from gpiozero import LED
from time import sleep

red = LED(17)
yellow = LED(26)
green = LED(5)

time = 2

def redOn():
    red.on()
    sleep(time)
    red.Off()
    
def yellowOn():
    yellow.on()
    sleep(time)
    yellow.Off()


def grreenOn():
    green.on()
    sleep(time)
    green.Off()
    
while True:
    redOn()
    yellowOn()
    grreenOn()