from pyrf24 import RF24


radio = RF24(22,0)
radio.setDataRate(RF24_250KBPS)
radio.print_details()
