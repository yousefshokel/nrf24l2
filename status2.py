from pyrf24 import RF24
#import RPi.GPIO as GPIO

#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(22, GPIO.OUT)


radio = RF24(18,0)
radio.begin()
radio.print_details()
#GPIO.cleanup()
