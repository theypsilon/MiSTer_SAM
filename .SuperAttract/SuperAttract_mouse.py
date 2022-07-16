#!/usr/bin/env python

import struct
import time
import glob
import sys
import os
import errno

FIFO = '/tmp/.SAM_tmp/SAM_Activity'

try:
    os.mkfifo(FIFO)
except OSError as oe:
    if oe.errno != errno.EEXIST:
        raise

packstring = "i"

infile_path = sys.argv[1]
EVENT_SIZE = struct.calcsize(packstring)
while True:
    try:
        file = open(infile_path, "rb")
        event = file.read(EVENT_SIZE)
        (a) = struct.unpack(packstring, event)
        if a != 111:
            f = open(FIFO, "w")
            f.write("Mouse moved")
            f.write("\n")
            f.close()
        time.sleep(0.4)
    except FileNotFoundError:
        print(" Mouse disconnected")
        sys.exit(1)