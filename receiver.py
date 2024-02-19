# Import the RF24 module
from pyRF24 import RF24

# Create an instance of the RF24 class
radio = RF24()

# Setup the radio module
radio.begin()

ce_pin = 25  # Replace with your GPIO pin
csn_pin = 8   # Replace with your GPIO pin

radio.setCEPin(ce_pin)
radio.setCSNPin(csn_pin)

# Set the radio channel and payload size
radio.setChannel(0x76)
radio.setPayloadSize(32)

# Set the address for communication (both on transmitter and receiver)
address = [0xAB, 0xCD, 0xEF, 0x01, 0x23]
radio.openWritingPipe(address)
radio.openReadingPipe(1, address)

# Start listening for incoming data
radio.startListening()

while True:
    # Check if there is data available to read
    if radio.available():
        # Read the data
        data = radio.read(32)
        print("Received data:", data.decode('utf-8'))

# Cleanup when the script ends
radio.end()






