ATE=$(date +"%Y-%m-%d_%H%M%S").jpg
DIR=/home/pi/webcam/
SRC=/mnt/mntfld/
NEW=_1.jpg
NEWDATE=$DIR$DATE$NEW
fswebcam -r 1280x720 -S 20 --jpeg 99 --no-banner $DIR$DATE
cp $DIR$DATE $SRC$DATE
python face3.py $DIR$DATE fc.xml
FACE='python face3.py $DIR$DATE fc.xml | tail '
./index2.php $DATE $DATE$NEW $FACE
cp  $NEWDATE $SRC$DATE$NEW
