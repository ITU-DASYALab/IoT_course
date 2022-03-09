# Practical Networking: The Things Network (TTN)

In this exercise we'll convert our WIFI-based networked sensing-node into a LoRaWAN-based version.

We'll use the TTN web-interface to register an application and an end-device (your lopy). Then we'll plug in the keys we get from TTN into the example code for the LoPy and see that the first messages come through.

Next we'll merge this TTN-code with our Co2-sensing code. 
Here we'll fit three measurements into a 4 byte payload and send that with LoRa. 
On the TTN-side we'll decode the data with a decoder we give you and send it to an endpoint on training.itu.dk. Here the data will be picked up and put in an InfluxDB.

> __NOTE:__ Save a version of your current WiFi/MQTT-setup. If you want to run your device at home, you'll probably want to use WiFi.

---

## Steps to do
The steps you'll go through in this exercise is:

1. Configure an application on The Things Network
    - Create a user on [The Things Network](thethingsnetwork.org/login/) 
    - Create an application on the [TTN console}(https://eu1.cloud.thethings.network/console/) (See hints further down)
    - Register an End Device (See hints further down)
        - Get your LoPys Device EUI (run the script from [our github](https://github.com/ITU-DASYALab/IoT_course/blob/main/guides/lopyLoRa%26TTN.md))
    - Look at the live data (while you do the next step: connect your device) 

2. Connect your LoPy to The Things Network
    - __REMEMBER__ to attach the antenna to the LoPy. We'll need the connector next to the LED _which is __not__ right next to the reset button_ 
    - Grab the default code from [our github](https://github.com/ITU-DASYALab/IoT_course/blob/main/guides/lopyLoRa%26TTN.md)
    - Fill in the APP_EUI and APP_KEY from your end-device in the example code and run it. If all is configured correctly you should be able to see it in the TTN console.
    - _Q:_ What is this code sending? And how is the payload constructed?

3. Prepare your sensors payload.
    - We have defined the payload format you must follow. It is specified in the hints and snippets below. If you don't follow this format you need to write your own decoder.
    - A few questions to think about:
        - What are the supported ranges for each value? 
        - How lossy is this encoding? 
        - What is the sensitivity of each value after encoding?
    
4. Add LoRa-connectivity to this
    - Copy the relevant parts of your TTN example code into your payload-producing sensor script
    - Alter the sending part so you send your new payload instead.
    - Alter your script so you only send every minute or so.

5. Back to the TTN console!
    - Confirm that there is now 4 bytes arriving in the TTN console.
    - Add the decoding script to TTN (under "payload formatters")
    - Confirm that you can see the correct values in the live data.
    - Add an "Integration". You should add a custom webhook with format JSON and baseurl "https://training.itu.dk/iot2022". Enable uplink messages with the path "/".

6. Grafana: Looking at the data
    - Create your user at the Grafana instance at training.itu.dk. You should have gotten an invitation in your itu-mail.
    - Go to our [communal TTN dashboard](https://training.itu.dk:3000/d/z7rSMlY7z/ttn-co2-lopy-all?orgId=5&refresh=10s) and see if you can see your device readings.
7. Finally done!

## Home edition

There is also a script listening to messages on the MQTT-broker we used last time, so if you use the script we created last time, connect it to your home network, and send messages on the IoT2022sec-topic, they will automatically be picked up and saved to an automatically generated measurement in Influx, so you can plot them in Grafana.

Example: sending a value to IoT2022sec/niec/co2 will automatically saved in IoT2022sec-niec-co2, which you'll be able to find in grafana.

---

## Code Snippets and settings

### Register applications
You can enter almost whatever. Just make it something you can recognize.

### Register device
Choose to register the device manually

- Freqency plan: Europe 863-870 MHz (SF9 for RX2 - recommended)
- LoraWAN version: 1.0.1
- Paste in your Device EUI
- Fill the APP_EUI with 0s
- Genereate an APP_KEY
- Make up a device ID that you can recognize

### The Payload Specification

The payload format we would like you to use fills __4 bytes__ and is encoded in the following way:

- Co2-value: Round to int, pack into two bytes (big-endian)
- Temperature: add 64, multiply by 2, round to int, pack into one byte
- Humidity: multiply by 2, round to int, pack into one byte
- Concatenate these 4 bytes in this order

#### Payload example:
measurement:
"co2": 816,
"humidity": 32,
"temperature": 17.5

payload: 
hex: 03 30 A3 40
Binary: 00000011 00110000 10100011 01000000

The decoder we provide is just the inverse of this, but written in JavaScript.

### Get the device EUI
```python
#get your device's EUI
from network import LoRa
import binascii
lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)
print(binascii.hexlify(lora.mac()).upper().decode('utf-8'))
```

### TTN connection example code
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

### Decoder for TTN
```javascript
function decodeUplink(input) {
  co2 = (input.bytes[0] << 8) + input.bytes[1]
  temp = (input.bytes[2] / 2.0) - 64.0
  relh = input.bytes[3] / 2
  return {
    data: {
      co2: co2,
      temperature: temp,
      humidity: relh
    },
    warnings: [],
    errors: []
  };
}
```

