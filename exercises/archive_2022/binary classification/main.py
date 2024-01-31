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
# Thanks Niels..!!
#


import time
import math
import pycom
from machine import UART                    
from machine import I2C
from scd30 import *
from svm_model import svm
from tree_model import tree
uart = UART(0, baudrate=115200)             # UART configuration
pycom.heartbeat(False)  # disable the heartbeat LED
i2c = I2C(2) # create and use default PIN assignments (P9=SDA, P10=SCL)
# NOTE: Could not make it work using the ESP32 hardware I2C buses (0 & 1), 
# but the bitbanged software bus (2) works
# Yay for libraries!
sensor = SCD30(i2c, 0x61)


while True:
    for i in range (500):
         # Wait for sensor data to be ready to read (by default every 2 seconds)
        if sensor.get_status_ready() != 1:
            time.sleep_ms(200)
        (co2, temperature, hum) = sensor.read_measurement()
            # Adjust for PCB heating effect. 
        temperature -= 3 # NOTE: Found this value somewhere online
        data=[co2,temperature,hum] # put in array the sensor data
        #make the prediction
        y_pred_svm=svm(data)
        y_pred_tree=tree(data)
        #send the information and the label
        print(round(co2,2),';',round(temperature,2),';',round(hum,2), ';', y_pred_svm,';', y_pred_tree)
        time.sleep_ms(2000)
