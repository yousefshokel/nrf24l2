from pyrf24 import RF24


radio = RF24(0,22)
radio.begin()
radio.print_details()
