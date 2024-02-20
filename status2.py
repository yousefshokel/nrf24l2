from pyrf24 import RF24


radio = RF24()
radio.begin(22,0)
radio.print_details()
