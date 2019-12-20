
import serial
import pickle
import time
import RPi.GPIO as GPIO
import SimpleMFRC522


def location():
 ser = serial.Serial ("/dev/ttyS0", 9600)
 sentences = []#Open port with baud rate
 current = time.time() # get current time
 timeout = 5
 endtime = time.time()+timeout 
 while current < endtime:
   current = time.time()
   received_data = ser.readline()              
   a = received_data.split(",")
   if a[0] == "$GNGGA":
		gpsData = {
			"ts" : a[1],
			"lat" : a[2]/100.0,
			"latDir" : a[3],
			"long" : a[4]/100.0,
			"longDir" : a[5],
			"fix" : a[6]
		}
		return gpsData
    
 with open("sentences.pkl", 'wb') as outfile:
    pickle.dump(sentences, outfile)

def intialize():
 reader = SimpleMFRC522.SimpleMFRC522()

 try:
	print("First, writing to the tag...")
	text = raw_input('Enter new data to write to tag, then hit Enter: ')

	 finally:
	
 GPIO.cleanup()

 return "Tag is intialized"

def initialize():
 reader = SimpleMFRC522.SimpleMFRC522()

 try:
	print("Place your tag next to the antenna to write")
	reader.write(text)

	print("Wait 5 seconds...")
	time.sleep(5)

	print("Now, reading tag - place it next to the antenna...")
	id, text = reader.read()

 finally:

	GPIO.cleanup()

 return "Tag is read"

