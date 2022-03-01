## Requirements

We know how to connect to and program the LoPy4.

## LoRaWAN

Now let s talk LoRa, or more specifically, LoRaWAN.

First, let s get our DevEUI we will need this to register our device:

```python
#get your device's EUI
from network import LoRa
import binascii
lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)
print(binascii.hexlify(lora.mac()).upper().decode('utf-8'))
```

Now that we know our DevEUI,

we need to either

1/ register on TTN, make an application, register our device

or

2/ collaborate on the current course app called "iot2022-course" (ask lecturer, TA)

or

3/ request keys for existing application from lecturer, TA

Everybody is welcome to register on TTN themselves, if they like to.

When this is done, we know our AppEUI and AppKey.

We are ready to run this code, to register our device OTAA:

```python
import binascii
import pycom
import socket
import time
from network import LoRa

# Colors
off = 0x000000
red = 0xff0000
green = 0x00ff00
blue = 0x0000ff

# Turn off heartbeat LED
pycom.heartbeat(False)

# Initialize LoRaWAN radio
lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)

# Set network keys
app_eui = binascii.unhexlify('YOUR_APP_EUI')
app_key = binascii.unhexlify('YOUR_APP_KEY')

# Join the network
lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)
pycom.rgbled(red)

# Loop until joined
while not lora.has_joined():
    print('Not joined yet...')
    pycom.rgbled(off)
    time.sleep(0.1)
    pycom.rgbled(red)
    time.sleep(2)

print('Joined')
pycom.rgbled(blue)

s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
s.setblocking(True)

i = 0
while True:
    count = s.send(bytes([i % 256]))
    print('Sent %s bytes' % count)
    pycom.rgbled(green)
    time.sleep(0.1)
    pycom.rgbled(blue)
    time.sleep(9.9)
    i += 1
```


Check if all devices show up  ok, and are sending data.

=======================================================================
## Sensor data via LoRaWAN
=======================================================================

Now combine the two elements -

1/ LoRaWan network
&
2/ Sensors

to send sensor data to TTN.

You may want to start sending some bogus data at first,
and then add the actual sender readings.









