
# Data acquisition locally #
Lopy sends data by serial port to jupyter notebook.
* First: Compile the data acquisition code in LoPy
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
button=Pin('P13', mode=Pin.IN,pull=Pin.PULL_UP)
#sensor
i2c = I2C(2) # create and use default PIN assignments (P9=SDA, P10=SCL)
sensor = SCD30(i2c, 0x61)
pycom.heartbeat(False)
pycom.rgbled(0x7f0000) # red

while True:
    if(button()==1):
        acquisition()

```

