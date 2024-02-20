from pyrf24 import RF24, RF24_250KBPS


radio = RF24(22,0)
radio.setDataRate(RF24_250KBPS)
radio.print_details()
