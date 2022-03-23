
# Data acquisition locally #
Lopy sends data by serial port to jupyter notebook.
* First: Compile the data acquisition code in LoPy
This code each time that the S1 button is pushed will send 200 samples by serial port.
 ``` python
# Code: project -> Data Acquisition process
#IoT
#Libraries
import time
import pycom
from machine import Pin
from machine import I2C
from scd30 import SCD30


##############ISR##########################
def acquisition():
    time.sleep(2)
    pycom.rgbled(0x007f00) # green 
    if sensor.get_status_ready() != 1:
        time.sleep_ms(200)
    for i in range(200):
        (co2, temperature, hum) = sensor.read_measurement()
            # Adjust for PCB heating effect. 
        temperature -= 3 # NOTE: Found this value somewhere online
            #send the information and the label
        print(round(co2,2),';',round(temperature,2),';',round(hum,2))
        time.sleep(4)
    pycom.rgbled(0x7f0000) # red
#################configuration################
button=Pin('P14', mode=Pin.IN,pull=Pin.PULL_UP)
#sensor
i2c = I2C(2) # create and use default PIN assignments (P9=SDA, P10=SCL)
sensor = SCD30(i2c, 0x61)
pycom.heartbeat(False)
pycom.rgbled(0x7f0000) # red

while True:
    if(button()==1):
        acquisition()

```
* Note: If you have issues with S1 button, you can chance to P13 and use extra button in hardware.
* Second: When LoPy is ready to sent data with the red light power on. Disconnect the LoPy of the serial port of Visual Studio  (Pymakr Console check)
* Third: Run the [code](https://github.com/ITU-DASYALab/IoT_course/blob/main/guides/Data%20acquisition.ipynb) changing the COM number to yours. 
* Fourth: Save your dataset in csv format

