from pyrf24 import RF24


radio = RF24()
radio.begin(0,22)
radio.print_details()
