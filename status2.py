from pyrf24 import RF24
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
#GPIO.setup()


radio = RF24(22,0)
radio.begin()
radio.print_details()
GPIO.cleanup()
