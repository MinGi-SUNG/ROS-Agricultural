#! /bin/bash
while true; do
	sshpass -p "turtlebot" scp -r /home/lee99/문서/code/store_fruits_count.txt root@192.168.0.9:/media/usb
done
