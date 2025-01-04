import ms5837
import smbus
import time
import datetime

sensor = ms5837.MS5837_02BA()
DEBUG = 1

time.sleep(2)

def startup():
#	print("prep to init")
	sensor.init()
	time.sleep(1)
#	print("prep to read")
	sensor.read(ms5837.OSR_256)
#	print("prep to set density")
	sensor.setFluidDensity(ms5837.DENSITY_FRESHWATER)


def main():
	print("starting")
	counter = 15
	startup_success = 0
	second_time = 0
	while startup_success == 0:
		try:
			startup()
		except:
			print("                 ***FAILED STARTUP***")
			pass
		else:
			startup_success = 1
			time.sleep(0.5)

	print("opening file")
	try:
		f = open("collect_all_data2.txt", 'w')
		print("file opened")
	except:
		print("not opened.................................")

	while second_time <= counter:
		try:
			print("reading sensor")
			sensor.read(ms5837.OSR_256)
			print("sensor read")

		except:
			print("                 ***FAILED READING***")
			continue
		readings = sensor.pressure(ms5837.UNITS_kPa)
		readings = round(readings, 2)
		#print pressure readings
		print("readings: " + str(readings))

		depth = sensor.depth()
		depth = round(depth + 0.13, 2)
		#print the first depth readings
		print("first depth: " + str(depth))
	#	second_time = second_time + 3
		time.sleep(3)

		try:
			print("reading sensor")
			sensor.read(ms5837.OSR_256)
			temp1 = sensor.read(ms5837.OSR_256)
			print("sensor read: " + str(temp1))

		except:
			print("                 ***FAILED READING***")
			continue

		depth2 = sensor.depth() + 0.13
		print(str(depth2))

		now = datetime.datetime.now()
		if abs(depth2 - depth) > 0.35: #was 0.2
			continue

		if depth >= 5 or depth <-0.35: #was 0.2
 			continue

		print("RN10" + " : " + (str(second_time)) + " : " + (str(readings)) + " : " + (str(depth)), file=f)

	#	print(str(now.strftime("%H:%M:%S") + " : " + str(readings) + " kPa") + " : ")
#		print(str(now.strftime("%H:%M:%S")))
		second_time = second_time + 5
		#f.close()
		#time.sleep(5)


main()
