import RPi.GPIO as GPIO
from nrf24 import NRF24

def get_nrf24_status():
    # Setup GPIO
    GPIO.setmode(GPIO.BCM)
    
    # Specify Raspberry Pi SPI interface (0 or 1) and CE pin
    radio = NRF24(0, 22)

    # Initialize the radio with CSN=0 and channel 76
    radio.begin(22,0,76)

    # Retrieve and print the status
    status = radio.get_status()
    print(f"NRF24L01 Status: 0x{status:02X}")

    # Cleanup GPIO
    GPIO.cleanup()

if __name__ == "__main__":
    get_nrf24_status()
