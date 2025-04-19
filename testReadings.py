import ms5837
import smbus
import time
import datetime
import threading
import os

sensor = ms5837.MS5837_02BA(1)
DEBUG = 1
global second_time
time.sleep(2)
counter=0
f = open("collect_data.txt", 'w')
os.chmod("collect_data.txt", 0o777)
second_time = 0

def startup():
	#print("prep to init")
	sensor.init()
	time.sleep(1)
	#print("prep to read")
	sensor.read(ms5837.OSR_256)
	#print("prep to set density")
	sensor.setFluidDensity(ms5837.DENSITY_FRESHWATER)

def main(counter):
	global second_time
	startup_success = 0
#	second_time = 0
	while startup_success == 0:
		try:
			startup()
		except:
			print("                 ***FAILED STARTUP***")
			pass
		else:
			startup_success = 1
			time.sleep(0.5)

	#os.chmod("collect_data.txt", 0o777)

	while second_time >= counter:
		try:
			sensor.read(ms5837.OSR_256)

		except:
			print("                 ***FAILED READING***")
			continue
		readings = sensor.pressure(ms5837.UNITS_kPa)
		readings = round(readings, 2)

		depth = sensor.depth()
		depth = round(depth + 0.43, 2)

		try:
			sensor.read(ms5837.OSR_256)

		except:
			print("                 ***FAILED READING***")
			continue
		depth2 = sensor.depth() + 0.43

		now = datetime.datetime.now()
		if abs(depth2 - depth) > 0.35:
			continue

		if depth >= 5 or depth <-0.35:
 			continue
#		print("first: " + depth)
		depth =  depth * -1
#		print("second: " + depth)
#		print(str(now.strftime("%H:%M:%S") + " : " + str(readings) + " kPa") + " : ")
#		print("Depth: ", str(depth))
#		print(str(now.strftime("%H:%M:%S")))
#		print("first time: ", second_time)
		second_time = second_time + 5
		print("RN08" + " : " + (str(second_time)) + " : " + (str(readings)) + " : " + (str(depth)), file=f)
		print("RN08" + " : " + (str(second_time)) + " : " + (str(readings)) + " : " + (str(depth)))
#		print("second time: ", second_time)
		#f.close()
		time.sleep(5)


#if "__name__" == "__main__":

#	startup()
#	while True:
#		main(counter)
#	startup()

#for i in range(counter):
#	counter = 5
#	main(5)

while True:
	main(counter)
