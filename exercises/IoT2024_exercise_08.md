# Revision of full data path so far

The following is an overview of the steps involved in our exercise work up to this point, 
listing some of the aspects and learning outcomes.

you may see this as a checklist for self-evaluation, but also a memo list for possible exam areas.


## Board

### Physical assembly

We have throughout the semester connected a sensor to our board.
However, there are several other possibilities for connections to the board.
The [pinmap](https://github.com/Xinyuan-LilyGO/LilyGo-LoRa-Series/blob/master/assets/image/t-beam_v1.1_pinmap.jpg) is a good place to get started to get an overview of the board, and which pins it is possible to connect to.

Remember that we also have used a breadboard for the process of connecting sensors and other equipment to our board.
If you need to refresh your memory on how the breadboard works, take a look [here](https://wiring.org.co/learning/tutorials/breadboard/).

### Antenna 

We have looked into how the antenna is connected to the board, as well as we have created pin mappings to ensure that we connect to the antenna in a way that our programs can use.
See an example of such a pin mapping on [this line in the example code](https://github.com/ITU-DASYALab/IoT_course/blob/85be575ee369b2f1460cdbfc0f8e66532cdc210a/guides/ttn_code_examples/main.ino#L88).

### Serial USB

Some students using Macs had issues connecting their boards via Serial USB because of the way that their drivers worked. 
Please refer to [this](https://github.com/espressif/esptool/issues/280) GitHub-issue for more information about a driver that solves this issue (the webpage for the driver that fixes the issue is in Chinese, but it seems to be possible to understand how to download/install it using Google Translate).

### Arduino IDE

We have utilized the Arduino IDE as a way to produce programs for our board.
This could have been done using other IDE's, like VS Code.
For a comprehensive guide to the Arduino IDE, please refer to [this guide](https://github.com/ITU-DASYALab/IoT_course/blob/main/guides/lilyGo_hello_world.md).

## Sensors

### Cabling

We connected the SCD30 together with our board. 
For a tutorial on how this is done, please refer to this [tutorial](https://github.com/ITU-DASYALab/IoT_course/blob/main/exercises/IoT2024_exercise_03.md).

### I2C bus

We used the I2C bus to communicate with our sensor. 
[Here](https://learn.sparkfun.com/tutorials/i2c/all) you can find more information about how it works.
Also, here is a simple [I2C scanner](https://github.com/ITU-DASYALab/IoT_course/blob/main/guides/I2C_scanner.md) to show you what I2C devices there are connected to your board, which is useful for troubleshooting I2C.

## Networking

### WiFi

We have utilized WiFi on our boards to send temperature measurements.
This is explained further in [this tutorial](https://github.com/ITU-DASYALab/IoT_course/blob/main/exercises/IoT2024_exercise_04.md).

### LoRa/LoRaWAN

We also use LoRa/LoRaWAN for the same purpose.
How this is done is explained in [this tutorial](https://github.com/ITU-DASYALab/IoT_course/blob/main/exercises/IoT2024_exercise_05.md).

Some students have had issues with the libraries we have used for LoRa communication.
The two most common pitfalls are:

1. There are several libraries installed for the same purpose/many libraries with the same name. 
To fix this, find the folder "Libraries" under the "Arduino IDE" folder, and delete the libraries that you do not intend to use.
2. Sometimes you have to make adjustments to the project config of the library that we use in the tutorials. 
Go to the library's folder (should be named "MCCI_LoRaWAN_LMIC_library") in the "Libraries" folder (as explained above).
Here, find the "project_config" folder, and open the "lmic_project_config.h" file.
The content of this file should be:

        // project-specific definitions
        #define CFG_eu868 1
        // #define CFG_us915 1
        //#define CFG_au915 1
        //#define CFG_as923 1
        // #define LMIC_COUNTRY_CODE LMIC_COUNTRY_CODE_JP      /* for as923-JP; also define CFG_as923 */
        //#define CFG_kr920 1
        //#define CFG_in866 1
        #define CFG_sx1276_radio 1
        //#define LMIC_USE_INTERRUPTS
        #define hal_init LMICHAL_init
    Where the last line is the most important one, as it overwrites a commonly used variable in many libraries, which can result in your programs not being able to run.
    We also change the frequency from the standard one (US) to a European one.

## MQTT

We have also used an MQTT broker.
The case that is most important from exercises is the one provided by the Things Network (TTN).
This broker allows you to listen to "up"-events to an application on TTN.
An explanation of how this is used in our "setup" can be found in [this guide](https://github.com/ITU-DASYALab/IoT_course/blob/main/guides/TTN-MQTT-telegraf-Influx.md). (Note that we use a Python script for listening for up-events and writing them to a database.
This can be done in several ways, this is just a simple approach to easily illustrate how a full setup can be done).

## Payload formats

### Minimization

How many digits make sense? How many bytes to use?

### Encoding / Bits and bytes

From float number to HEX bytes and base64



## LoRaWan stack

For our exercises, the LoRaWAN stack we have used is The Things Network (TTN).
A guide to using TTN can be found in [exercise 05](https://github.com/ITU-DASYALab/IoT_course/blob/main/exercises/IoT2024_exercise_05.md).

Some important keywords are:

- network and application server

- creating applications

- onboarding devices

- join process

## Data Integration

How to get data from application server to data storage and analysis

(we

#### MQTT 

Same as before? almost - now we are using it to subscribe to TTN MQTT 

#### Webhooks

The possibility of using any custom receiver script and pointing at it via URL

## Timeseries Database

### InfluxDB

How do i write to InfluxDB?

python script
telegraf (Sebastian will actually set this up during exercise and test)

## Data Visualization

### Connecting data sources

Different options for data source - Flux, InfluxQL

### Queries

Sample queryto get all CO2 readings of today
