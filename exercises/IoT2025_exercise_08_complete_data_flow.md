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

We connected the SCD30 with our board. 
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

## Payload formats

When working with IoT, we often have to compromise between bandwidth and the accuracy of what we want to transmit:

### Minimization

An example of minimization can be seen in [exercise 05](https://github.com/ITU-DASYALab/IoT_course/blob/main/exercises/IoT2024_exercise_05.md) where we first transmit data over LoRa.
Does it make sense to transmit the whole measurement?
Sometimes we can get measurements with decimals that are more accurate than what the sensor can provide.
Therefore we can skip some decimals to minimize the data that we transmit.

### Encoding / Bits and bytes

We have seen several times throughout the exercises encoded float numbers into both HEX bytes and base64:
- HEX bytes have an ordering of bytes that represent numbers in a way that can be sorted by largest or smallest byte (big-endian or little-endian)
- Base64 can be used for transmission over text-based protocols but can increase data size.


## LoRaWan stack

For our exercises, the LoRaWAN stack we have used is The Things Network (TTN).
A guide to using TTN can be found in [exercise 05](https://github.com/ITU-DASYALab/IoT_course/blob/main/exercises/IoT2024_exercise_05.md).

Some important keywords are:

- network and application server

- creating applications

- onboarding devices

- join process

## Data Integration

How to get data from the application server to data storage and analysis:

#### MQTT 

We have used an MQTT broker.
The case that is most important from exercises is the one provided by the Things Network (TTN).

#### Webhooks

Using the MQTT broker, we can listen to "up"-events to an application on TTN.
As can be seen in [this guide](https://github.com/ITU-DASYALab/IoT_course/blob/main/guides/TTN-MQTT-telegraf-Influx.md) we use [this script](https://github.com/ITU-DASYALab/IoT_course/blob/main/guides/ttn_code_examples/ttn-influx-db.py) to do this.
This script also stores all of the "up"-events in an InfluxDB bucket.
Note that we use a Python script for listening to a webhook.
Another alternative can be [Node-RED](https://nodered.org/).

## Timeseries Database

### InfluxDB

When working with InfluxDB some things are different from how we usually work with databases.
We write to a bucket instead of a database, and each of the entries we make are called points.
These differences between are traditional relative databases work, and how a time series database like InfluxDB works.
If you [in the script we used to store data we sent over TTN](https://github.com/ITU-DASYALab/IoT_course/blob/main/guides/ttn_code_examples/ttn-influx-db.py) you can see an example of how we can write to an InfluxDB database.

- Python script
telegraf (Sebastian will set this up during exercise and test)

## Data Visualization

We used [Grafana](https://grafana.com/) to visualize the data that we collected:

### Connecting data sources

When developing different visualizations in Grafana, we had to query our InfluxDB bucket to get the data that we wanted.
There are different ways to query an InfluxDB database:

- [Flux](https://docs.influxdata.com/influxdb/cloud/query-data/flux/)
- [InfluxQL](https://docs.influxdata.com/influxdb/v1/query_language/)

### Queries

[Here](https://github.com/ITU-DASYALab/IoT_course/blob/main/guides/ttn_code_examples/grafana_queries.md) are some examples of queries that can be used in Grafana to get the data from the measurements that we have made earlier.
