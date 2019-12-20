# imported wrong demo file from PI this is the old one. 

from kiFinder import location, detection, initializie
import serial
import pickle
import time
import RPi.GPIO as GPIO
import SimpleMFRC522

a= initializie();
print(a)
b = detection();
print(b)
c = location();
print(c) 