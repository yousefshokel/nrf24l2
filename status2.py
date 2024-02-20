from pyrf24 import RF24


radio = RF24(23,0)
radio.begin()
radio.print_details()
