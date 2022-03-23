#!/usr/bin/env python
#
# Copyright (c) 2019, IT university of Copenhagen
#
# This software is licensed under the GNU GPL version 3 or any
# later version, with permitted additional terms. For more information
# see the Pycom Licence v1.0 document supplied with this file
# Code: project -> Binary classification algorithm
# IoT course
#
import machine
from machine import UART
import time
import os


uart = UART(0, baudrate=115200)
os.dupterm(uart)

machine.main('main.py')
