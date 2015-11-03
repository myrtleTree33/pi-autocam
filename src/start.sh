#!/usr/bin/env sh

## Starts Picam daemon in background, if not already running
./picam &

## Delete all files older than 10 days.  Scan for these files every 60 seconds.
## CAUTION: This command is very dangerous, ensure is already in correct folder.
(cd rec && while true; do sleep 2; find . -mtime +10 -delete; done &)

## Start taking photos
python main.py --fps 2 --width 300 --height 300 --duration 5 --videobitrate 8000
