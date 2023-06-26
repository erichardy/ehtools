#!/usr/bin/bash

MAX_DELAY=2700

if [ $# != 0 ]
then
	DELAY=$1
else
	DELAY=180
fi

gsettings set org.gnome.desktop.session idle-delay $DELAY

# spd-say $DELAY -i -95

if [ $DELAY -le 60 ]
then
	let SLEEP=($DELAY * 8)
	sleep $SLEEP
	gsettings set org.gnome.desktop.session idle-delay $MAX_DELAY
	# spd-say $MAX_DELAY -i -95
fi


