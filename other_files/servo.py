import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
pwm=GPIO.PWM(3, 50)
pwm.start(0)
def SetAngle(angle):
	print("function started")
	duty = angle / 18 + 2  
	print(duty)
	GPIO.output(3, True)
	pwm.ChangeDutyCycle(duty)
	sleep(5)
	GPIO.output(3, False)
	pwm.ChangeDutyCycle(0)
	print("end")
print("start")
SetAngle(90) 
pwm.stop()
GPIO.cleanup()

