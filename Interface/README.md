# Interface

The Interface class provides multiple interfaces used for devices that will be attached to the Raspberry Pi.

## Features

Following features are provided

- UART interface to communicate with the AIS Base Station by USB <-> RS232
- I2C Interface to comminicate with I2C-supported embedded devices
- Socket (Ethernet) Interface to communicate with devices in the Local Area Network
- SPI Interface to communicate with SPI-supported embedded devices

## Requirements

### Libraries

- [PySerial](https://pypi.org/project/pyserial/)
- [smbus2](https://pypi.org/project/smbus2/) 
- [socket](https://docs.python.org/3/library/socket.html)
- [spidev](https://pypi.org/project/spidev/)


## To Do

- Better Parent-Child relationship between the Inferface class and the interfaces (UART, I2C, ect..)
