#!/usr/bin/python
import sys
import signal
import RPi.GPIO as GPIO
import time
from simple_pid import PID
import ms5837
import smbus
import datetime
import threading

global target_position
global position

TOP_SWITCH = 21
ROTATE_SWITCH = 6
SERVO_OFF = 150
SERVO_UP = 200
SERVO_DOWN = 100

SYRINGE_NEUTRAL = 19	 #was 25 #was 16
SYRINGE_MAX = 37 #was 44 #was 30

SEC_PER_CLICK = 2.384615

SERVO_CHANNEL = 0

start_depth = 0

p = -0.001 #was -0.02
i = 0 #was -0.00015
d = 0

GPIO.setmode(GPIO.BCM)
#GPIO.setup(12, GPIO.OUT)
GPIO.setup(ROTATE_SWITCH, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(TOP_SWITCH, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#p = GPIO.PWM(12, 50) # channel 12, 50Hz
#p.start(SERVO_OFF) #motor_off

sensor = ms5837.MS5837_02BA(1)

# Stop Servo
#p.start(SERVO_OFF)
time.sleep(1)
file = open("pidDepth.txt", "w")
file2 = open("Depth.txt", "w")

def handle_signal(signum, frame):
    Set_Servo(SERVO_CHANNEL, SERVO_OFF)
    print("bye")
    sys.exit(0)

# Register the handler for common termination signals
signal.signal(signal.SIGTERM, handle_signal)  # kill
signal.signal(signal.SIGINT, handle_signal)   # Ctrl+C


# Turn on servo with servoblaster
def Set_Servo(channel, pulse_width):
    with open('/dev/servoblaster', 'w') as f:
        f.write(f"{channel}={pulse_width}\n")

def startup():
	Set_Servo(SERVO_CHANNEL, SERVO_OFF) 
	sensor.init()
	time.sleep(1)
	sensor.read(ms5837.OSR_256)
	sensor.setFluidDensity(ms5837.DENSITY_FRESHWATER)


def move(move_amount):
#code to turn on servo and fill syringe w water and stop it when switch (pin 20) is activated
        print("moving ", move_amount)
        if move_amount > 0:
                Set_Servo(SERVO_CHANNEL, SERVO_DOWN) 
                pos_part=move_amount
                if (pos_part != 0):
                     print("pos_part, = ", pos_part)
                     time_part = pos_part * SEC_PER_CLICK
                     Set_Servo(SERVO_CHANNEL, SERVO_DOWN)
                     time.sleep(time_part)
                     Set_Servo(SERVO_CHANNEL, SERVO_OFF)

        if move_amount < 0:
                pos_part=move_amount
                if (pos_part != 0):
                   print("pos_part, = ", pos_part)
                   Set_Servo(SERVO_CHANNEL, SERVO_UP)
                   time.sleep(abs(pos_part * SEC_PER_CLICK))
                   Set_Servo(SERVO_CHANNEL, SERVO_OFF)
        print("moved")
        return

def init_html():

        #ORIGINAL CODE FROM 2023-24 below
        print("Content-type:text/html\r\n\r\n")
        print("")
        print("Hello everyone")
        print("""<p><a href="http://192.168.42.10/index.php">Go_Back_to_Data</a></p>""")

def find_neutral():
	global syr_position
	global SYRINGE_NEUTRAL
	global position
	global start_depth

	sensor.read(ms5837.OSR_256)
	start_depth = sensor.depth() * 100

	depth = sensor.depth() * 100
	while((depth - start_depth) < 2):
		if (GPIO.input(TOP_SWITCH) == 0):
			Set_Servo(SERVO_CHANNEL, SERVO_OFF)
			return

		print("Finding neutral from ", position)
		Set_Servo(SERVO_CHANNEL, SERVO_UP) 
		time.sleep(.25 * SEC_PER_CLICK)
		position+=0.25
		Set_Servo(SERVO_CHANNEL, SERVO_OFF) 
		time.sleep(0.5)
		sensor.read(ms5837.OSR_256)
		depth = sensor.depth() * 100
		print("Finding Neutral - ", depth, "cm")
	SYRINGE_NEUTRAL = position + 0.25
	Go_To_Pos(SYRING_NEUTRAL)
	print("Neutal syringe is ", position)
	print("Neutral syringe is: ", position, file=file2)
	#syr_position = SYRINGE_NEUTRAL

if __name__ == "__main__":
	init_html()
	startup()
	#Go_To_Top()
	#Go_To_Pos(SYRINGE_MAX)
	inp = float(input("How much to move?"))
	#find_neutral()
	move(inp)
	GPIO.cleanup()

