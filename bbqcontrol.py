#!/usr/bin/python
#Parts of the code are used from Adafruit

# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

import time

import Adafruit_GPIO.SPI as SPI
import MAX6675.MAX6675 as MAX6675

#Raspberry Pi hardware SPI configuration.
SPI_PORT   = 0
SPI_DEVICE = 0
sensor = MAX6675.MAX6675(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

# Loop printing measurements every second.
print 'Press Ctrl-C to quit.'
while True:
	temp = sensor.readTempC()
	print 'Thermocouple Temperature: {0:0.3F}°C'.format(temp)
time.sleep(1.0)