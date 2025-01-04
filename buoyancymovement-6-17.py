#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import smbus
import ms5837
import sys
import cgi
import cgitb
import ms5837
import smbus
import time
import datetime
import webbrowser
import threading
import collect_data
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
from gpiozero import MCP3008
#import psutil

def startup_sensor():
	print("prep to init")
	sensor.init()
	time.sleep(1)
	print("prep to read")
	sensor.read(ms5837.OSR_256)
	print("prep to set density")
	sensor.setFluidDensity(ms5837.DENSITY_FRESHWATER)

def collect_pressure():
	global timer_sec
	while True:
		try:
			sensor.read(ms5837.OSR_256)
		except:
			#print("failed reading")
			continue #goes back to the try. it's stubborn like that
		readings = sensor.pressure(ms5837.UNITS_kPa)
		now = datetime.datetime.now()
		#print(now)
		seconds = int(now.strftime("%S"))
		#print(seconds)
		if seconds % 5 == 0 and seconds != timer_sec: 
		#and seconds == timer_sec:
			print(str(readings) + "   " + now.strftime("%H:%M:%S"))
			timer_sec = seconds
			#print(timer_sec)
		#f = open("/home/robotics/pressure_test.txt", 'w')
		#print(str(now.strftime("%H:%M:%S") + " : " + (str(readings)) + " kPa"), file=f)
		break

def plunger_up():
	global counter
	print("plunger going up")
	while GPIO.input(switch) == True:
		while GPIO.input(switch) == True:
			GPIO.output(motorup, GPIO.HIGH)
		GPIO.output(motorup, GPIO.LOW)
		time.sleep(0.5)

def plunger_down():
	print("plunger going down")
	if GPIO.input(switch) == False: #check if it's true by software protection
		GPIO.output(motordown, GPIO.HIGH)
		#collect_pressure()
		time.sleep(plunger_time)
		GPIO.output(motordown, GPIO.LOW)
	time.sleep(0.5)
	if GPIO.input(switch) == False: #check if it's true by software protection
		GPIO.output(motordown, GPIO.HIGH)
		#collect_pressure()
		time.sleep(plunger_time)
		GPIO.output(motordown, GPIO.LOW)

def calibration():
    print("calibration\n")
    plunger_up()
    time.sleep(2)
    print("plunger going down")
    plunger_down()

def be_down():
	plunger_up()
    #not inclusive of the last second
#	global counter
	#for descend_time in range(time_to_bottom):
		#print ("counter" + str(counter))
		#if counter % 5 == 0:
		#collect_pressure()
		#counter = counter + 1
		#time.sleep(1)


def be_up():
	plunger_down()
	#time.sleep(time_to_bottom)
	#for rising_time in range(time_to_bottom):
	#	collect_pressure()

def be_main():
     calibration()

def be_dive():
     print("be dive")
     be_down()
     time.sleep(time_to_bottom)
     be_up()
     #webbrowser.open('192.168.42.10/index.html')

def get_battery():
#	battery_status = psutil.sensors_battery()
#	print(battery_status)
#	print("Percentage of battery: %s %" % (battery_status.percent,))
#	print("Is power plugged: %s" % (battery_status.power_plugged,))
	pot = MCP3008(0)
	new_val = pot.value*6.6
	print(new_val)
	k = open("battery_check.txt", 'w')
	print((new_val), file=k)
	print("test")

#running main function
#be_main()
print("Content-type:text/html\r\n\r\n")
print("")
print("Hello everyone")
print("""<p><a href="http://192.168.42.10/index.php">Go_Back_to_Data</a></p>""")



#initializing the sensors
sensor = ms5837.MS5837_02BA(1)
DEBUG = 1

time.sleep(2)

motordown = 5
motorup = 6
switch = 21
plunger_time = 70 #was ~60 seconds to bottom of syinge
time_to_bottom = 1
counter = 140 #number of seconds for the whole cycle
timer_sec = 0

#set the modes for the pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#pin setups
GPIO.setup(motordown, GPIO.OUT)
GPIO.setup(motorup, GPIO.OUT)
GPIO.setup(switch, GPIO.IN)

#initial them all to low
GPIO.output(motorup, GPIO.LOW)
GPIO.output(motordown, GPIO.LOW)

form = cgi.FieldStorage()

'''#startup sensor
startup_success = 0
while startup_success == 0:
	try:
		startup_sensor()
	except:
		print("                 ***FAILED STARTUP***")
		pass
	else:
		startup_success = 1
		time.sleep(0.5)
'''
#if sys.argv[1] == "calibrate": calibration()
#if sys.argv[1] == "up": plunger_up()
#if sys.argv[1] == "down": plunger_down()
#if sys.argv[1] == "dive": be_dive()

#while True:
#	get_battery() 
if "dive" in form: 
	print("diving")
	dataCode = threading.Thread(target=collect_data.main, args = (counter,))
	dataCode.start()
	be_dive()

if "sample" in form: 
	print("sampling")
	dataCode = threading.Thread(target=collect_data.main, args = (4,))
	dataCode.start()
	#be_dive()

if "calibrate" in form: 
	#print("Calibrating")
	calibration()

if "battery" in form:
	get_battery()
