import struct
import time
from pyrf24 import RF24, RF24_PA_LOW, RF24_250KBPS, RF24_1MBPS, RF24_2MBPS
import RPi.GPIO as GPIO
from datetime import datetime

GPIO.setmode(GPIO.BCM)


radio = RF24(22, 0)
radio.begin()

pipe = 1
address = [0xF0F0F0F0E1]
radio.setDataRate(RF24_1MBPS)
radio.setPALevel(RF24_PA_LOW)
radio.openReadingPipe(pipe, address[0])
radio.openWritingPipe(address[0])
radio.startListening()
print("Receiver is ready to receive messages...")

N = 0
latency = 0
Time = time.time()

try:
    while True:
        radio.startListening()
        if radio.available():
            payload_size = struct.calcsize('fff')
            data = radio.read(payload_size)
            N = N+1
            if len(data) == payload_size:
                unpacked_data= struct.unpack('fff', data)
                sensor_value = unpacked_data[0]
                PacketNumber = unpacked_data[1]
                MachineId = unpacked_data[2]
                print(f"Sensor Value: {sensor_value}")
                print(f"Machine Number: {MachineId}")
                print(f"Packet Number: {PacketNumber}")
                print(f"Number of packets received: {N}")
                #print(f"Packet received: {N/PacketNumber*100}%")
                print(f"Timestamp: {datetime.now()}")
                print("")
                latency = time.time()
                
        #elif time.time() - latency > 5:
            #print("Warning: No response from the transmitter...")
            #while not radio.available():
               # pass
                
        if time.time() - Time > 3:
            A = time.time()
            while  Time - A < 0.5:
                message =  "HIGH"
                radio.stopListening()
                radio.write(message.encode('utf-8'))
                print("Transmitted number: {}".format(message))
                Time = time.time()
            
        
except KeyboardInterrupt:
    pass
finally:
    
    radio.stopListening()
    radio.end()
                

