#hxvhjsgvjs

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
direction= input("What direction?") 

if direction == "up":
    print("LED on") 
    GPIO.output(22,GPIO.HIGH)
    time.sleep(2)
    print("LED off")
    GPIO.output(22,GPIO.LOW)
    time.sleep(2)

if direction == "sink":
    print("LED on") 
    GPIO.output(18,GPIO.HIGH)
    time.sleep(2)
    print("LED off")
    GPIO.output(18,GPIO.LOW)
    time.sleep(2)

constant = input("Is the pressure sensor constant?")
if constant == "false":
     print("ok.")
if constant == "true":
    print("!Pressure sensor is constant. Going down!")
    GPIO.output(18,GPIO.HIGH)
    time.sleep(5)
    print("At the bottom!!!")
    GPIO.output(18,GPIO.LOW)
   










