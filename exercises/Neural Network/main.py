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
#https://forum.micropython.org/viewtopic.php?t=1747
# Thanks Niels..!!
#

import time
import math
import pycom
from machine import UART                    
from machine import I2C
from scd30 import SCD30
uart = UART(0, baudrate=115200)             # UART configuration
pycom.heartbeat(False)  # disable the heartbeat LED
i2c = I2C(2) # create and use default PIN assignments (P9=SDA, P10=SCL)
# NOTE: Could not make it work using the ESP32 hardware I2C buses (0 & 1), 
# but the bitbanged software bus (2) works
# Yay for libraries!
sensor = SCD30(i2c, 0x61)
y_pred=0
def sigmoid_fuction (input):
    e=2.71828
    return (1/(1+pow(e,-input)))

def neuralmodel (input):
    l0n0=(input[0]-1201.52)/(40000.0-1201.52)
    l0n1=(input[1]-22.19)/(32.04-22.19)
    l0n2=(input[2]-27.9)/(93.81-27.9)
    l1n0=max(0,((l0n0*-0.40)+(l0n1*-0.45)+(l0n2*-0.56)))
    l1n1=max(0,((l0n0*-0.20)+(l0n1*0.69)+(l0n2*1.41)) - 0.047)
    l1n2=max(0,((l0n0*-0.81)+(l0n1*0.04)+(l0n2*-0.85))-0.008)

    l2n0= max(0,((l1n0*0.11)+(l1n1*1.51)+(l1n2*-0.38))-0.011)
    l2n1= max(0,((l1n0*0.37)+(l1n1*-0.41)+(l1n2*-0.23))+1.025)
    l2n2=max(0,((l1n0*0.002)+(l1n1*-0.08)+(l1n2*-0.95)))

    l3n0=sigmoid_fuction(((l2n0*1.58)+(l2n1*-0.85)+(l2n2*-0.69))-0.5874)
    if l3n0 < 0.5:
        return 0
    else:
        return 1


while True:
    # Wait for sensor data to be ready to read (by default every 2 seconds)
    if sensor.get_status_ready() != 1:
        time.sleep_ms(200)
    (co2, temperature, hum) = sensor.read_measurement()
        # Adjust for PCB heating effect. 
    temperature -= 3 # NOTE: Found this value somewhere online

    if co2 > 0 and temperature > 0 and hum > 0:
        data=[co2,temperature,hum] # put in array the sensor data
        #make the prediction
        y_pred=neuralmodel(data)
        #send the information and the label
        print(round(co2,2),';',round(temperature,2),';',round(hum,2),';',y_pred)        
    time.sleep(4)
 
