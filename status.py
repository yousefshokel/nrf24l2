import time
from pyrf24 import RF24, RF24_PA_LOW, RF24_250KBPS

# Set up NRF24L01 radio
radio = RF24(22,0)

def setup_radio():
    radio.begin()
    radio.printDetails()

def get_status():
    status = radio.get_status()
    print(f"NRF24L01 Status: {status}")

if __name__ == "__main__":
    try:
        setup_radio()
        get_status()
    except KeyboardInterrupt:
        print("Program terminated by user.")
    finally:
        radio.powerDown()
