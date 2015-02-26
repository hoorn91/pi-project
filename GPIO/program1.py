import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pir = 4

GPIO.setup(pir, GPIO.IN)
time.sleep(2)

while True:
	if GPIO.input(pir):
            print("MOTION DETECTED!!!!!")
	time.sleep(1)
GPIO.cleanup()