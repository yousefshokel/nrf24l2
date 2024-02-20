from pyrf24 import RF24


radio = RF24()
radio.begin(24,25)
radio.print_details()
