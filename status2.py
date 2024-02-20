from pyrf24 import RF24


radio = RF24(22,0)
radio.begin(0, 0, "P8_23", "P8_24")
radio.print_details()
