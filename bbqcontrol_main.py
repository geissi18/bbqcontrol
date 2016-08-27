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
#import Adafruit_GPIO.SPI as SPI #Comment out for testing without target
#import MAX6675.MAX6675 as MAX6675 #Comment out for testing without target

#Main function for temperature control with PID
def main(targettemp):
    #Raspberry Pi hardware SPI configuration.
    SPI_PORT   = 0
    SPI_DEVICE = 0

    #Auslesen der "settemp" vom Webserver
    #url = 'http://geissi18.pythonanywhere.com/bbqcontrol/settemp'
    #url = 'https://localhost/bbqcontrol/settemp'
    #response = requests.get(url)
    #json = response.json()
    #targettemp = json['temp']
    #print (json['temp'])
    print ('Targettemp = %d °C' % targettemp)

    #Read actualtemp of sensor
    #Comment out for testing without target the following lines
    #sensor = MAX6675.MAX6675(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))
    #actualTemp = sensor.readTempC()
    actualtemp = 200 # Only for testing
    
    print ('Actual Temperature: %f °C' % actualtemp)

    #Berechnen der PID-Controller Parameter
    #Sampling Time alle 5 Sekunden
    samplingtime = 5
    #Koeffizienten
    Ti = 5
    Td = 3
    Kp = 0.8

    y, yc, h = actualtemp, targettemp, samplingtime
    correctionvalue = pid_controller(y, yc, h, Ti, Td, Kp)
    while 1:
        print('Actual Temperature: %f C' % actualtemp)
        correctionvalue = pid_controller(y, yc, h, Ti, Td, Kp)
        #print (outputdata)
        #print(list(itertools.islice(outputdata, 1)))
        print('Correctionvalue: %f' % next(correctionvalue))
        #print('Correctionvalue: %f' % correctionvalue.next())
        time.sleep(h)
        #Curl der Variablen. Variablen auf Webserver vorbesetzt
        #bbqvalues = requests.get('http://geissi18.pythonanywhere.com/bbqcontrol/bbqvalues')
        #outputdata = pid_controller(y, yc, h, Ti, Td, Kp, u0, e0)
        #Curl Post outputdata
        #headers = {'Content-Type': 'application/json',}
        #data = '{"actualtemp":"", "u":"", "ui_prev":"", "e_prev":""}'
        #requests.post('http://geissi18.pythonanywhere.com/bbqcontrol/bbqvalues', headers=headers, data=data)

        #print (outputdata)

        #Einstellen des Servos
        #tbd

