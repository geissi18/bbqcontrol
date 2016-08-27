#!/usr/bin/python
#Only for testing porpses
from python_pid_controller import pid_controller
import time
#import os

#pid = os.getpid()
#print(pid)

#Sampling Time alle 5 Sekunden
samplingtime = 10
#Koeffizienten
Ti = 5
Td = 3
Kp = 0.8
#Tagettemp
targettemp = 300
#Actualtemp
actualTemp = 200

y, yc, h = actualTemp, targettemp, samplingtime

#Berechnen der PID-Controller Parameter
while 1:
    print ('Actual Temperature: %f C' % actualTemp)
    correctionvalue = pid_controller(y, yc, h, Ti, Td, Kp)
    #print (outputdata)
    #print(list(itertools.islice(outputdata, 1)))
    #print('Correctionvalue: %f' % correctionvalue.next())
    print (correctionvalue.next())
    time.sleep(h)
