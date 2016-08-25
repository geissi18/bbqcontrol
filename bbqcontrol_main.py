#!/usr/bin/python
import requests
import json
from PIDCtrl.python_pid_controller import pid_controller
#import Adafruit_GPIO.SPI as SPI
#import MAX6675.MAX6675 as MAX6675

#Auslesen der "settemp" vom Webserver
url = 'http://geissi18.pythonanywhere.com/bbqcontrol/settemp'
#url = 'https://localhost/bbqcontrol/settemp'
response = requests.get(url)
json = response.json()
targettemp = json['temp']
#print (json['temp'])
print ('Targettemp = %d °C' % targettemp)

#Abfragen der actualTemp vom Sensor
#Raspberry Pi hardware SPI configuration.
SPI_PORT   = 0
SPI_DEVICE = 0
#sensor = MAX6675.MAX6675(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))
#actualTemp = sensor.readTempC()
actualTemp = 200
print ('Actual Temperature: %f °C' % actualTemp)

#Berechnen der PID-Controller Parameter
y = actualTemp
yc = targettemp
#Sampling Zeit alle 5 Sekunden (Cronjob!)
h = 5
#Konstanten tbd
Ti = 1
Td = 1
Kp = 1

outputdata = pid_controller(y, yc, h, Ti, Td, Kp, u0=0, e0=0)
print (outputdata)

#Daten auf Webserver posten

#Einstellen des Servos


