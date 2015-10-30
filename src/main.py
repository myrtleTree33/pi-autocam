#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
import time
import os
import subprocess

def make_command(command, val):
    return "--" + command + " " + str(val)

def take_video(duration):
    startRec = "./hooks/start_record"
    stopRec = "./hooks/stop_record"
    f = open(startRec, 'w')
    f.close()

    time.sleep(duration)

    os.remove(startRec)
    f = open(stopRec, 'w')
    f.close()
    time.sleep(1)
    os.remove(stopRec)



@click.command()
@click.option('--fps', default=2, help='Frames per second/')
@click.option('--width', default=1280, help='The screen capture width')
@click.option('--height', default=720, help='The screen capture height')
@click.option('--duration', default=5, help='The duration of each file, in seconds')
def prog(fps, width, height, duration):
    """
    Simple program to take pictures
    """
    args = " " + make_command("fps", fps) + " " + make_command("width", width) + " " + make_command("height", height) + " "

    while(True):
        take_video(duration)
        time.sleep(1) # short sleep to prevent overuse of CPU


def run_cam_daemon():
    subprocess.call(["./picam"])

if __name__ == '__main__':
    run_cam_daemon()
    #prog()
