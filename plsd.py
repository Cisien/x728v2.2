#!/bin/python3
import RPi.GPIO as GPIO
import time
import os

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.IN)
GPIO.setup(26, GPIO.OUT)

def my_callback(channel):
    time.sleep(30) # 30 second delay to see if it's still a 1 (short power cycle)
    if GPIO.input(6):     # if port 6 == 1
        print ("---AC Power Loss OR Power Adapter Failure---")
        print ("Shutdown in 5 seconds")
        time.sleep(5)
        GPIO.output(26, GPIO.HIGH)
        time.sleep(3)
        GPIO.output(26, GPIO.LOW)
        #os.system('shutdown -h now')

    else:                  # if port 6 != 1
        print ("---AC Power OK,Power Adapter OK---")

GPIO.add_event_detect(6, GPIO.BOTH, callback=my_callback)
my_callback('')
while True:
  time.sleep(1)
