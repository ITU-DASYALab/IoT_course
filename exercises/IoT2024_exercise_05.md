# Exercise week 05
## Hello LoRaWAN! - Simple LoRaWAN program

### Goal for the day

  * Familiarize yourself with the LoRa-capabilities of a LilyGo-board
  * Send data to a LoRaWANnetwork
  * Connect to The Things Network
  * Make some considerations about how/which data we send

### The task

#### Setup The Things Network

There are a few short steps we need to do before we are able to connect to The Things Network:
 
1. Create an account at [The Things Networks](https://www.thethingsnetwork.org/) website.
2. Create an application in the [console](https://eu1.cloud.thethings.network/console/applications). Make sure it is something you recognize :)
3. In the application you just created, click the "Register End Device"-button to create a new end device. Choose "Enter end device specifics manually", and enter this: 
    - Freqency plan: Europe 863-870 MHz (SF9 for RX2 - recommended)
    - LoraWAN version: 1.0.1
    - Paste in your Device EUI
    - Fill the APP_EUI with 0s
    - Genereate an APP_KEY
    - Make up a device ID that you can recognize
4. Type 0's as your 'JoinEUI', and let the console generate both an DevEUI and an AppKey for you

#### Connect your board to The Things Network

1. First, attach the antenna before connecting the board
2. Add the "MCCI Arduino LoRaWAN Library" using the library manager
3. Go to "Examples" -> "LMIC-Arduino" -> "ttn-otaa.ino" 
4. Use this example as a basis for your connection to the TTN. Some hints:
    - You will have to change the APPEUI, DEVEUI & APPKEY according to what you added on the TTN.
    - You will have to change the pinmap to something like this, so that it suits our specific ports for our board:
          
          // Pin mapping
          const lmic_pinmap lmic_pins = {
            .nss = 18,
            .rxtx = LMIC_UNUSED_PIN,
            .rst = 23, // was "14,"
            .dio = {26, 33, 32},
          };
5. When deciding on the payload of the request you send, remember to consider how to format it later.

#### Add a payload decoder

Now go back to your browser and the TTN console:

1. Confirm that you get some data arriving in the TTN console

2. Add a decoding script to allow TTN to read the data you just sent. Here is an example of such for co2, temp and humidity data:

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
  
3. You can also add an integration to allow for more cool functionality. Please refer to this guide: https://github.com/ITU-DASYALab/IoT_course/blob/main/guides/TTN-MQTT-telegraf-Influx.md

### Acknowledgements

This exercise is heavily inspired by the work of previous TA's: https://github.com/ITU-DASYALab/IoT_course/blob/main/exercises/archive_2022/exercise-05-networking2.md