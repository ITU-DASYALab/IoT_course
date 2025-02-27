# Exercise week 05
## Hello LoRaWAN! - Simple LoRaWAN program

### Goal for the day

  * Familiarize yourself with the LoRa-capabilities of the T-Beam board
    * Frequencies, radio chip versions
  * Send data to a LoRaWAN network (The Things Network)
  * Consideration of data formatting: which data in what format?

### The task

Sending data to a LoRaWAN network requires two main things:

1. Configuring the backend (Network and Application Server)

2. Programming the node

#### Back end: Setup The Things Network

1. Create an account at [The Things Networks](https://www.thethingsnetwork.org/) website.
2. Create an application in the [console](https://eu1.cloud.thethings.network/console/). Make sure it is something you recognize :) - 
You may also use the course application called "iot2025-course" - let us discuss the pros and cons of having all devices in one application vs independent applications.
3. In the application you just created, click the "Register End Device"-button to create a new end device. Choose "Enter end device specifics manually", and enter this: 
    - Freqency plan: Europe 863-870 MHz (SF9 for RX2 - recommended)
    - LoraWAN version: 1.0.1
    - Paste in your Device EUI - which you know from where?
      - The DevEUI is the globally unique identifier of a LoRaWAN® device - at least in theory, much like a MAC address. But, TTGO boards (which includes T-Beam) do not come with factory provided DevEUI and DevAddr. One good way of generating you DevEUI in this case, to keep the DevEUI somewhat unique, is:
        - Take your MAC address
        - Put a FFFE in the middle (as the MAC is 48bit and the DevEUI needs to be 64 bit)
        - Like so:  MAC = D4:D4:DA:5C:DF:94 ==> DevEUI = D4:D4:DA:FF:FE:5C:DF:94
        - (The terms "little endian" and LSB, "big endian" and MSB might need some explaining - you need to understand them to get the settings right in your code.)
4. Fill the APP_EUI with 0s (or another fantasy EUI - discuss?)
    - In real life, this would often be provided by a vendor, or network operator
5. Generate an APP_KEY
6.  Make up a device ID that you (and we!) can recognize, e.g. "IoT2025-GroupNumberOrName"

#### Connect your board to The Things Network

1. First, as always: attach the antenna before connecting the board
2. Add the "MCCI Arduino LoRaWAN Library" using the library manager - it will install some dependencies.

```
A side note; we very much hope that all our boards are the exact same hardware version this semester!
T-Beams can be found with two different LoRa chips, SX1276 and the (newer and more performant) SX1262 -
and these need different libraries.
For the SX1276, the MCCI Arduino LoRaWAN Library
for the SX1262, the Basic Radio Lib -
https://github.com/Xinyuan-LilyGO/LilyGo-LoRa-Series/tree/master/examples/LoRaWAN/RadioLib_OTAA
(it should be able to do both SX1262 and SX1276).

We hope all our boards are SX1276 - also note the settings under Tools in the Arduino IDE!
``` 
3. Go to "Examples" -> "MCCI LoRaWAN LMIC Arduino" -> "ttn-otaa.ino" 
4. Use this example as a basis for your connection to the TTN. Some hints:
    - You will have to change the APPEUI, DEVEUI & APPKEY according to what you added on the TTN.
    - You will have to change the pinmap:
  ```   
          // Pin mapping
          const lmic_pinmap lmic_pins = {
            .nss = 18,
            .rxtx = LMIC_UNUSED_PIN,
            .rst = 23, // was "14,"
            .dio = {26, 33, 32},
          };

```
5. Changes in other files

in
```libraries/MCCI_LoRaWAN_LMIC_library/project_config/lmic_project_config.h```
you need to set frequency :

```#define CFG_eu868 1```

radio type:

```
#define CFG_sx1276_radio 1
//#define CFG_sx1261_radio 1
//#define CFG_sx1262_radio 1
```
also add a line:
```
#define hal_init LMICHAL_init
```
After these chnages, you should be ready to join the TTN.
Learn how to monitor the join process - both on the serial terminal and on the web console of the TTN.

#### Formatting the payload

It is time to look at how we are sending our sensor data. As long as we were on Wi-Fi and had plenty of bandwidth, and time-on-air did not matter, all was easy:
We could send things like:
``` 
 {
    "temperature": 25.43,
    "humidity": 25.82
  }
```

However, there is a lot of redundant data in this.
All we really need to send is 2 bytes - one for temperature, one for humidity. We could even do with less.
(How did we get to this decision? Discuss ranges and errors margins!)
The receiving side will know which is which (how?).

  - This guide on packing data into bytes is extremely helpful: [TTN - Working with bytes](https://www.thethingsnetwork.org/docs/devices/bytes/)
  - An working example connecting to the TTN and also publish some fake data can be found under LoRaWAN_examples/main.ino

#### Add a payload decoder


Now go back to your browser and the TTN console:

1. Confirm that you get some data arriving in the TTN console

2. Add a decoding script to allow TTN to read the data you just sent. Here is an example of such for co2, temp and humidity data.
Look at the way that the sensor readings have been packed into bytes - does it make sense? If not, let s talk about it.
An working example can be found under lorawan_examples/payload_decoder.js.
  
3. You can also add an MQTT integration already now. Please refer to this guide: https://github.com/ITU-DASYALab/IoT_course/blob/main/guides/TTN-MQTT-telegraf-Influx.md

### Acknowledgements

This exercise is heavily inspired by the work of previous TA's: https://github.com/ITU-DASYALab/IoT_course/blob/main/exercises/archive_2022/exercise-05-networking2.md


#### Appendix: TTN connection info

```
iot2025-sebastian

Frequency plan
Europe 863-870 MHz (SF9 for RX2 - recommended)

LoRaWAN version
LoRaWAN Specification 1.0.1

Regional Parameters version
TS001 Technical Specification 1.0.1

If you d like to join sebastian's course app:

iot2025-sebastian

AppEUI
CAFFEEBABE202505


in code:
static const u1_t PROGMEM APPEUI[8]={ 0x05, 0x25, 0x20, 0xBE, 0xBA, 0xEE, 0xFF, 0xCA };


App key:
A4B44F330E43D180405706AD6A936D03

in code:
static const u1_t PROGMEM APPKEY[16] = { 0xA4, 0xB4, 0x4F, 0x33, 0x0E, 0x43, 0xD1, 0x80, 0x40, 0x57, 0x06, 0xAD, 0x6A, 0x93, 0x6D, 0x03 };

Sebastian will need your DevEUI

You can also share devices and apps and gateways, by inviting other users.
Sebastian is: _sebastianb_

```

