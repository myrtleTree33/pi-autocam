# -*- coding: utf-8 -*-

import click
import sys
import time
import os
import subprocess

def make_command(command, val):
    return "--" + command + " " + str(val)

def take_video(duration):
    startRec = "./hooks/start_record"
    stopRec = "./hooks/stop_record"

    # remove all files
    try:
        os.remove(startRec)
        os.remove(stopRec)
    except Exception:
        pass

    subprocess.call(["touch", startRec])
    time.sleep(duration)
    subprocess.call(["touch", stopRec])
    time.sleep(2)


@click.command()
@click.option('--fps', default=2, help='Frames per second/')
@click.option('--width', default=1280, help='The screen capture width')
@click.option('--height', default=720, help='The screen capture height')
@click.option('--duration', default=5, help='The duration of each file, in seconds')
@click.option('--videobitrate', default=2000, help='The video bit rate of each file')
def prog(fps, width, height, duration, videobitrate):
    """
    Simple program to take pictures
    """
    args = " " + make_command("fps", fps) + " " + make_command("width", width) + " " + make_command("height", height) + " " + make_command("videobitrate", videobitrate)

    run_cam_daemon(args)

    while(True):
        take_video(duration)
        time.sleep(0.01) # short sleep to prevent overuse of CPU


def run_cam_daemon(args):
    print args
    subprocess.Popen(['./picam'] + args.split(' '))
    time.sleep(1)

if __name__ == '__main__':
    print "Running timer.."
    prog()
