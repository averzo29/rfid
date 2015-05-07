import cv2
import sys
import MySQLdb
import os
from cv2 import *
# initialize the camera
cam = cv2.VideoCapture(0)   # 0 -> index of camera
s, img = cam.read()
if s:    # frame captured without any errors
    imwrite("filename.jpg",img) #save image
#os.system("fswebcam -r 1280x720 --no-banner /home/pi/filename.jpg")
# Get user supplied values
imagePath ="/home/pi/filename.jpg"
cascPath = "/home/pi/fc.xml"
newname = "/home/pi/filename_1.jpg"
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
