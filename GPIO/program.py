import RPi.GPIO as GPIO
import time
import random
import sys

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
time.sleep(10)
while True:
	x = random.randint(1,3)
	if x == 1:
		GPIO.output(led, 1)
		GPIO.output(led2, 0)
		GPIO.output(led3, 0)
	elif x == 2:
		GPIO.output(led, 0)
		GPIO.output(led2, 1)
		GPIO.output(led3, 0) 
	elif x == 3:
		GPIO.output(led, 0)
		GPIO.output(led2, 0)
		GPIO.output(led3, 1)	
	time.sleep(0.2)	
GPIO.cleanup()
