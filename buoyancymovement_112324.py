#!/usr/bin/python
print("Content-Type: text/html\n\n")
import RPi.GPIO as GPIO
import time
import smbus
import ms5837
import sys
import cgi
import cgitb
#import smbus
#import time
import datetime
import webbrowser
import threading
import collect_data
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
from gpiozero import MCP3008
#import psutil

#global varialbles
pin_motordown = 5
pin_motorup = 6
pin_switch = 21
plunger_time = 70 #was ~60 seconds to bottom of syinge
time_to_bottom = 1
counter = 140 #number of seconds for the whole cycle
timer_sec = 0
print ("2.....")

#Function:startup_sensor
#Purpose:Sensors are initialized, read, and set density
def startup_sensor():
	sensor = ms5837.MS5837_02BA(1)
	print("prep to init")
	print("s1.......")
	sensor.init()
	print("s2........")
	time.sleep(1)
	print("prep to read")
	sensor.read(ms5837.OSR_256)
	print("prep to set density")
	sensor.setFluidDensity(ms5837.DENSITY_FRESHWATER)
	print("...startup_sensor() done")

#Function: collect_pressure
#Purpose: Reads the pressure sensors data, turns it into strings so it can be readable
def collect_pressure():
	global timer_sec
	while True:
		try:
			sensor.read(ms5837.OSR_256)
		except:
			print("failed reading")
			continue #goes back to the try. it's stubborn like that
		readings = sensor.pressure(ms5837.UNITS_kPa)
		now = datetime.datetime.now()
		#print(now)
		seconds = int(now.strftime("%S"))
		#print(seconds)
		if seconds % 5 == 0 and seconds != timer_sec:
		#and seconds == timer_sec:

		#converts readings to strings so they can be readable
			print(str(readings) + "   " + now.strftime("%H:%M:%S"))
			timer_sec = seconds
		#print(timer_sec)
		#f = open("/home/robotics/pressure_test.txt", 'w')
		#print(str(now.strftime("%H:%M:%S") + " : " + (str(readings)) + " kPa"), file=f)
		break

#Function: plunger_up
#Purpose: Shows the syringe is getting filled, hits the switch, BE dives down

def plunger_up():
	global counter
	print("plunger going up")
	

	GPIO.output(pin_motordown, GPIO.HIGH)
        time.sleep(3)
        GPIO.output(pin_motordown, GPIO.LOW)
        time.sleep(3)
        GPIO.output(pin_motorup, GPIO.HIGH)
        time.sleep(3)
        GPIO.output(pin_motorup, GPIO.LOW)
        time.sleep(3)
	
	'''
	while GPIO.input(pin_switch) == True:
		while GPIO.input(pin_switch) == True:
			GPIO.output(pin_motorup, GPIO.HIGH)
		GPIO.output(pin_motorup, GPIO.LOW)
		time.sleep(0.5)
	'''

#Function: plunger_down
#Purpose: Shows the syringe is empty, switch isn't hit, BE goes up

def plunger_down():
	print("plunger going down")

        GPIO.output(pin_motordown, GPIO.HIGH)
        time.sleep(3)
        GPIO.output(pin_motordown, GPIO.LOW)
        time.sleep(3)
        GPIO.output(pin_motorup, GPIO.HIGH)
        time.sleep(3)
        GPIO.output(pin_motorup, GPIO.LOW)
        time.sleep(3)
	
	'''
	if GPIO.input(pin_switch) == False: #check if it's true by software protection
		GPIO.output(pin_motordown, GPIO.HIGH)
		#collect_pressure()
		time.sleep(plunger_time)
		GPIO.output(pin_motordown, GPIO.LOW)
		time.sleep(0.5)
	if GPIO.input(switch) == False: #check if it's true by software protection
		GPIO.output(pin_motordown, GPIO.HIGH)
		#collect_pressure()
		time.sleep(plunger_time)
		GPIO.output(pin_motordown, GPIO.LOW)
	'''



#Function: calibration
#Purpose: 

def calibration():
    print("calibration\n")
    plunger_up()
    time.sleep(2)
    print("plunger going down")
    plunger_down()

#-------------------------------------------------------------
# Function: be_down
# Purpose : when syringe goes up, BE goes down!
# Note    : 
#-------------------------------------------------------------
def be_down():
	plunger_up()
    #not inclusive of the last second
	#global counter
	#for descend_time in range(time_to_bottom):
		#print ("counter" + str(counter))
		#if counter % 5 == 0:
		#collect_pressure()
		#counter = counter + 1
		#time.sleep(1)
#--------------------------------------------------------------
# Function: be_up
# Purpose:
# Note:
#--------------------------------------------------------------

def be_up():
	plunger_down()
	#time.sleep(time_to_bottom)
	#for rising_time in range(time_to_bottom):
	#collect_pressure()
#----------------------------------------------------------------
# Function: be_main
# Purpose: 
# Note:
#----------------------------------------------------------------
def be_main():
     calibration()
#----------------------------------------------------------------
# Function: be_dive
# Purpose:
# Note: 
#----------------------------------------------------------------
def be_dive():
     print("be dive")
     #be_down()
     print("test .... 123")
     time.sleep(2)

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


#new code from Angelyn  ... code starts here

def angelyn_hello_world():
	print("hello world .... 2024")


def init_html():        
        
	#ORIGINAL CODE FROM 2023-24 below
	#running main function
	#be_main()
	print("Content-type:text/html\r\n\r\n")
	print("")
	print("Hello everyone")
	print("""<p><a href="http://192.168.42.10/index.php">Go_Back_to_Data</a></p>""")


def init_pressure_suensor():
        #initializing the sensors
        sensor = ms5837.MS5837_02BA(1)
        time.sleep(2)

def init_rpi():


	#set the modes for the pins
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	#pin setups
	GPIO.setup(pin_motordown, GPIO.OUT)
	GPIO.setup(pin_motorup, GPIO.OUT)
	GPIO.setup(pin_switch, GPIO.IN)

	#initial them all to low
	GPIO.output(pin_motorup, GPIO.LOW)
	GPIO.output(pin_motordown, GPIO.LOW)
	print ("3.....")

def run_be():

       form = cgi.FieldStorage()
       print ("4......")
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
        #       get_battery()
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


def test_sensor():
	GPIO.output(pin_motordown, GPIO.HIGH)
	time.sleep(3)
	GPIO.output(pin_motordown, GPIO.LOW)
	time.sleep(3)
	GPIO.output(pin_motorup, GPIO.HIGH)
	time.sleep(3)
	GPIO.output(pin_motorup, GPIO.LOW)
	time.sleep(3)

if __name__ == "__main__":
	angelyn_hello_world()
	init_rpi()
	test_sensor()
	#init_sensor()  #having issues with ssensor code, maybe sensor is dead
	init_html()
	run_be()
