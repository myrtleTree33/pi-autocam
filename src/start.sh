#!/usr/bin/env sh

###############################################
## Bootloader script to take videos.
###############################################


## Delete all files older than 10 days.  Scan for these files every 60 seconds.
## CAUTION: This command is very dangerous, ensure is already in correct folder.
## DO NOT TOUCH BELOW COMMAND
# (cd rec && while true; do sleep 2; find . -mtime +10 -delete; done &)

## Start taking photos
## Modify numbers as required here.
## Do note that screen dimensions are fixed to preset number; 
## Please check Picam manual for more information.
## Features: Picam apparently uses Hardware embedded MPEG encoder for TS files
## So this offsets load from Raspberry Pi to the hardware itself.
python main.py --fps 2 --width 160 --height 90 --duration 1200 --videobitrate 500000
