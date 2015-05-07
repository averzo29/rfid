import binascii 
import serial 
import time
import requests
import os
import cv2
import sys
from cv2 import *

device = serial.Serial("/dev/ttyUSB0", 9600)
arduino = serial.Serial("/dev/ttyACM0", 115200)

os.system("clear")
cam = cv2.VideoCapture(0)

imagePath ="/home/pi/filename.jpg"
cascPath = "/home/pi/fc.xml"
newname = "/home/pi/filename_1.jpg"

while True:
#	device.flushInput()
#	instring = device.read(device.inWaiting())
	instring = device.read(20)
	outstring = ""
#	print(instring)
	instring = binascii.hexlify(bytearray(instring))
	print(instring)
	data = instring[18:] #data starts at 18th char of instring
	print(data)
#	test = 'string'
#	value = {'tag':data, 'test': test}
#	link = requests.get('http://192.168.10.1/?tag=',params=value)
#	print(link.url)
#	time.sleep(1)  # important to indent this line
	if len(instring) > 0:
		thermalData = arduino.readline()
		print(data)
		print(thermalData)
		time.sleep(2)
		s, img = cam.read()
		if s:    # frame captured without any errors
		    imwrite("filename.jpg",img) #save image

		# Create the haar cascade
		faceCascade = cv2.CascadeClassifier(cascPath)

		# Read the image
		image = cv2.imread(imagePath)
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

		# Detect faces in the image
		faces = faceCascade.detectMultiScale(
		    gray,
		    scaleFactor=1.32,
		    minNeighbors=5,
		    minSize=(30, 30),
		    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
		)
		cnt=len(faces)
		# Draw a rectangle around the faces
		for (x, y, w, h) in faces:
		    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

		cv2.imwrite(newname, image)
		print "end"
		cam.release()
		
		value = {'rfidTag': data, 'temp': thermalData, 'faceCount': cnt}
		link = requests.get('http://192.168.10.6:8080/Security/PassData?',params=value)
		print(link.url)
		os.system("sudo ./xpix.sh")
		print "file moved"
#		os.system("sudo rm face3.pyc")
#		files = {'file': open('filename_1.jpg', 'rb')}
#		url2 = requests.post('http://192.168.10.1/post', files=files)
#		url2.text
# press return here to execute the while loop
# control C to abort while loop

device.write("ver")
device.read(20)
