import time
from pyrf24 import RF24, RF24_PA_LOW, RF24_250KBPS

# Set up NRF24L01 radio
radio = RF24.RF24(RF24.RPI_V2_GPIO_P1_22, RF24.BCM2835_SPI_CS0, RF24.BCM2835_SPI_SPEED_8MHZ)

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
