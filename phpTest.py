#!/usr/bin/env python3
print("Content-Type: text/html\n\n")
import sys
import smbus
import threading
import cgi
import cgitb
import webbrowser
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
#import collect_data
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
from gpiozero import MCP3008
import testPHPfile
form = cgi.FieldStorage()

'''
def kitty():
	print("where the f the function")

#def gohuskies():
if "huskies" in form:
	kitty()
if "sample" in form:
        print("sampling")
        dataCode = threading.Thread(target=testPHPfile.main, args = (4,))
        dataCode.start()
'''
#if __name__ == "__main__":
#	gohuskies()
