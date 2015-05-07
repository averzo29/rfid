#!/bin/bash

DATE=$(date +"%Y-%m-%d_%H%M%S").jpg
DIR=/home/pi/webcam/
SRC=/mnt/mntfld/
NEW=_1.jpg
NEWDATE=$DIR$DATE$NEW
fswebcam -r 640x480 -S 20 --no-banner $DIR$DATE
cp $DIR$DATE $SRC$DATE
./index2.php $DATE $DATE$NEW
python face3.py $DIR$DATE fc.xml
cp  $NEWDATE $SRC$DATE$NEW
