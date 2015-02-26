import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pir = 4
buzz = 14
GPIO.setup(pir, GPIO.IN)
GPIO.setup(buzz, GPIO.OUT)
GPIO.output(buzz, 0)
time.sleep(2)
try:
	while True:
		if GPIO.input(pir):
				print("MOTION DETECTED!!!!!")
				GPIO.output(buzz, 1)
		time.sleep(1)
		GPIO.output(buzz, 0)

except KeyboardInterrupt:
	print "Program Shutdown"
	GPIO.cleanup()