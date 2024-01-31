#!/usr/bin/env python
#
# Copyright (c) 2019, IT university of Copenhagen
#
# This software is licensed under the GNU GPL version 3 or any
# later version, with permitted additional terms. For more information
# see the Pycom Licence v1.0 document supplied with this file
# Code: project -> Data Acquisition process
# IoT
#Libraries
import time
import pycom

from machine import I2C
from scd30 import SCD30
from model_svm import svm

#sensor
i2c = I2C(2) # create and use default PIN assignments (P9=SDA, P10=SCL)
sensor = SCD30(i2c, 0x61)
pycom.heartbeat(False)

while True:
    if sensor.get_status_ready() != 1:
            time.sleep_ms(200)
    (co2, temperature, hum) = sensor.read_measurement()
            # Adjust for PCB heating effect. 
    temperature -= 3 # NOTE: Found this value somewhere online
    data=[temperature] # put in array the sensor data
        #make the prediction
    y_pred_linear=temperature*0.28563522+15.997669224596054    
    y_pred_svm=svm(data)
        #send the information and the label
    print(round(temperature,2),';',round(hum,2), ';', y_pred_svm ,';', y_pred_linear)
    time.sleep(4)