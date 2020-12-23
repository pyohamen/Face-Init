#!/bin/sh
cd /home/pi/s03p12a207/Pi
LD_PRELOAD=/usr/lib/arm-linux-gnueabihf/libatomic.so.1 python3 recognizer.py
