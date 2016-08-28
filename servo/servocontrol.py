#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import os

def servocontrol(percent):
        # Pin 12 als Ausgang deklarieren
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(12, GPIO.OUT)
        # PWM mit 50Hz an Pin 12 starten
        Servo = GPIO.PWM(12, 50)                       
        # PWM mit percent Dutycycle generieren
        Servo.start(percent)      
        # Programm beenden
        Servo.stop()
        GPIO.cleanup()
        return



