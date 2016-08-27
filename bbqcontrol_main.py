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

import requests
import json
from PIDCtrl.python_pid_controller import pid_controller
import time
import csv
#import Adafruit_GPIO.SPI as SPI #Comment out for testing without target
#import MAX6675.MAX6675 as MAX6675 #Comment out for testing without target
#import servocontrol.servocontrol as servo

#Main function for temperature control with PID
def main(targettemp):

    #Raspberry Pi hardware SPI configuration.
    SPI_PORT   = 0
    SPI_DEVICE = 0

    #Read actualtemp of sensor
    #Comment out for testing without target the following lines
    #sensor = MAX6675.MAX6675(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))
    #actualTemp = sensor.readTempC()
    actualtemp = 200 # Only for testing

    #Berechnen der PID-Controller Parameter
    #Sampling Time alle 5 Sekunden
    samplingtime = 5
    #Koeffizienten
    Ti = 50
    Td = 0.1
    Kp = 1.8

    y, yc, h = actualtemp, targettemp, samplingtime
    correctionvalue = pid_controller(y, yc, h, Ti, Td, Kp)
    while 1:
        correctionvalue = pid_controller(y, yc, h, Ti, Td, Kp)
        headers = {'Content-Type': 'application/json',}
        data = {}
        data['actualtemp'] = actualtemp
        data['correctionvalue'] = next(correctionvalue)
        data['targettemp'] = targettemp
        data = json.dumps(data)
        requests.post('http://geissi18.pythonanywhere.com/bbqcontrol/bbqvalues', headers=headers, data=data)
        jsonDataAsPythonValue = json.loads(data)
        outputFile = open('data.txt', 'a')
        outputFile.write('%f\n' % jsonDataAsPythonValue['actualtemp'])

        #Einstellen des Servos
        servo(50)
        time.sleep(h)
