from nrf24 import NRF24

def get_nrf24_status():
    # Create an NRF24 object
    radio = NRF24()

    # Initialize the radio with CE=0, CSN=0, and channel 76
    radio.begin(22, 8, 76)

    # Retrieve and print the status
    status = radio.get_status()
    print(f"NRF24L01 Status: 0x{status:02X}")

if __name__ == "__main__":
    get_nrf24_status()
