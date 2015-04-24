<?php
$con=mysql_connect('192.168.1.4','jake','') or die(mysql_error());
mysql_select_db('rpitest') or die("Cannot Select DB");
$setpic=$argv[1]."_1.jpg";
$sql="INSERT INTO upload(imgname,imgmod,tmpread,idread,status) VALUES('$argv[1]','$setpic','2','3','4')";

$result=mysql_query($sql);

if($result){
echo "Upload Successful";
} else {
echo "Failed to create";
}
?>
