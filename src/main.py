# -*- coding: utf-8 -*-

import click
import sys
import time
import os
import subprocess
from threading import Thread

## Set maximum lifespan of file before it is deleted
MAX_LIFESPAN_FILE_SECS = 60 * 60 * 24 * 5  ## 5 days

## Sets time to run garbage colllector job
GARBAGE_CHECK_TIME_SECS = 2  ## 2 seconds

def clear_old_files(folder, lifespan_secs):
    """
    Removes old files that are no longer used.
    """
    print 'running garbage collector..'
    now = time.time()
    for root, dirs, files in os.walk(folder):
        for f in files:
            long_file_path = os.path.join(root, f)
            if now - os.stat(long_file_path).st_mtime > lifespan_secs:
                print 'Removing file ' + f + '..'
                os.remove(long_file_path)


def garbage_daemon(folder, lifespan_secs, interval_secs):
    while True:
        clear_old_files(folder, lifespan_secs)
        time.sleep(interval_secs)


def init_garbage_daemon(folder, lifespan_secs, interval_secs):
    thread = Thread(target = garbage_daemon, args = (folder, lifespan_secs, interval_secs))
    thread.start()


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

    ## Run the daemons ----------
    init_garbage_daemon('./rec', MAX_LIFESPAN_FILE_SECS, GARBAGE_CHECK_TIME_SECS)
    run_cam_daemon(args)
    ## --------------------------

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
