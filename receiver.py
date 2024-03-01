import time
from pyrf24 import RF24, RF24_PA_LOW, RF24_250KBPS, RF24_1MBPS, RF24_2MBPS
import RPi.GPIO as GPIO
from datetime import datetime

GPIO.setmode(GPIO.BCM)

radio = RF24(22, 0)

pipe = 1
address = [0xF0F0F0F0E1]

radio.begin()
radio.openReadingPipe(pipe, address[0])
radio.setDataRate(RF24_1MBPS)
radio.startListening()

print("Receiver is ready to receive messages...")

N = 0
latency = 0

try:
    while True:
        
        if radio.available():
            payload_size = radio.getDynamicPayloadSize()
            data = radio.read(payload_size)
            N = N+1
            print("Received:", data.decode('utf-8'),N, time.time() - latency)
            latency = time.time()
            
        elif time.time() - latency > 5:
            print("Warning: No response from the transmitter...")
            while not radio.available():
                pass
                
            
            
            
except KeyboardInterrupt:
    pass
finally:
    
    radio.stopListening()
    radio.end()






