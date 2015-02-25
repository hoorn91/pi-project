import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led = 4
led2 = 14
led3 = 15
button = 18
GPIO.setup(led, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)
GPIO.setup(button, GPIO.IN, GPIO.PUD_UP)
GPIO.output(led, 0)
GPIO.output(led2, 0)
GPIO.output(led3, 0)

while True:
	if GPIO.input(button) == False:
            print("button pressed")
            break
GPIO.cleanup()