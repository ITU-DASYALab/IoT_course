# Goal for the day

We will review the full path of data from sensor/board over the LoRaWAN network, LoRaWAN backend to database and data dashboard.

By the end of the exercise,

we should have a dashboard and incoming data for each group/student on our Grafana server.

So our success checkpoint is __visible data__!

As pointed out repeatedly, there are many different ways of getting there -
the elements in our data path are exchangeable.

But regardless of which one you choose -
__we want to see your data__ :)

# Revision of full data path so far

The following is an overview of the steps involved in our exercise work up to this point, 
listing some of the aspects and learning outcomes.

you may see this as a checklist for self-evaluation, but also __a memo list for possible exam areas__.


## Board

### Physical assembly

We have connected a sensor to our board, using the serial I2C bus.
There are several other possibilities for connections to the board.
The [pinmap](https://github.com/Xinyuan-LilyGO/LilyGo-LoRa-Series/blob/master/assets/image/t-beam_v1.1_pinmap.jpg) is a good place to get started to get an overview of the board, and which pins it is possible to connect to.

We also have used a breadboard for the process of connecting sensors and other equipment to our board.

If you need to refresh your memory on how the breadboard works, take a look [here](https://wiring.org.co/learning/tutorials/breadboard/).

### Antenna 

We have looked into how the antenna is connected to the board, as well as we have created pin mappings to ensure that we connect to the antenna in a way that our programs can use.
See an example of such a pin mapping on [this line in the example code](https://github.com/ITU-DASYALab/IoT_course/blob/85be575ee369b2f1460cdbfc0f8e66532cdc210a/guides/ttn_code_examples/main.ino#L88).

### Serial USB

Some students using Macs had issues connecting their boards via Serial USB because of the way that their drivers worked. 
Please refer to [this](https://github.com/espressif/esptool/issues/280) GitHub-issue for more information about a driver that solves this issue (the webpage for the driver that fixes the issue is in Chinese, but it seems to be possible to understand how to download/install it using Google Translate).

### Arduino IDE

We have utilized the Arduino IDE as a way to code programs (sketches) for our board.
This could have been done using other IDE's, like VS Code, or just any editor of chocie.
For a comprehensive guide to the Arduino IDE, please refer to [this guide](https://github.com/ITU-DASYALab/IoT_course/blob/main/guides/lilyGo_hello_world.md).

## Sensors

### I2C bus

We used the I2C bus to communicate with our sensor. 
[Here](https://learn.sparkfun.com/tutorials/i2c/all) you can find more information about how it works.
Also, here is a simple [I2C scanner](https://github.com/ITU-DASYALab/IoT_course/blob/main/guides/I2C_scanner.md) to show you what I2C devices there are connected to your board, which is useful for troubleshooting I2C.

## Networking

### WiFi

At first, we used WiFi on our boards to send measurements, via MQTT messages.
We relied on having plenty of datarate / data throughput (often called bandwidth, though that's imprecise).
This is explained further in [this tutorial](https://github.com/ITU-DASYALab/IoT_course/blob/main/exercises/IoT2024_exercise_04.md).

### LoRa/LoRaWAN

We then moved over to LoRa/LoRaWAN for the same purpose.
How this is done is explained in [this tutorial](https://github.com/ITU-DASYALab/IoT_course/blob/main/exercises/IoT2024_exercise_05.md).

Important steps when configuring the code for LoRaWAN include:

1. The project config of the library that we use in the tutorials. 
Go to the library's folder (should be named "MCCI_LoRaWAN_LMIC_library") in the "Libraries" folder (as explained above).
Here, find the "project_config" folder, and open the "lmic_project_config.h" file.
The content of this file should be:

```
        // project-specific definitions -
// frequency: - we use EU868
        #define CFG_eu868 1
        // #define CFG_us915 1
        //#define CFG_au915 1
        //#define CFG_as923 1
        // #define LMIC_COUNTRY_CODE LMIC_COUNTRY_CODE_JP      /* for as923-JP; also define CFG_as923 */
        //#define CFG_kr920 1
        //#define CFG_in866 1
   // the LoRa chip we are using - hopefully all our boards have a SX1276 ... though we might find SX1262 in some batches
        #define CFG_sx1276_radio 1
        //#define LMIC_USE_INTERRUPTS
        #define hal_init LMICHAL_init
```

## Payload formats

When working with IoT, we often have to compromise between data rate available and the ammount of data we want to transmit.

Generally, size of our data messgaes directly translates into

time on air, power usage, battery lifetime,  - and with that deployment  lifetimes, budget, money .... business feasibility.

### Minimization

An example of minimization can be seen in [exercise 05](https://github.com/ITU-DASYALab/IoT_course/blob/main/exercises/IoT2024_exercise_05.md) where we first transmit data over LoRa.
Does it make sense to transmit the whole measurement?
Sometimes we can get measurements with decimals that are more accurate than what the sensor can provide.
Therefore we can skip some decimals to minimize the data that we transmit.

We suggest this data formate:

```
Humidity: 	0 ... 100 			==> 1 byte
Pressure: 5 digits relevant, e.g. 1018.4 	==> 2 bytes ... 11 bits would do, but ....
Altitude: we want meters: 0 ... 50000 		==> 2 bytes
Temperature: 					==> 1 byte, bias shifted as (T+40)*2
VOC:	  					==> 2 bytes
CO2:						==> 2 bytes
```

Note that in case you d like to use our data ingestion webhook later on, you will need to follow this format -
at least to the extent that your measure meant provides the paylaod as specified!

### Code for the ESP32 T-Beam

To create this data set, here s the code to be sued in your sketch:

```
byte senddata[] = {
  (uint8_t)(int(mySensor.readFloatHumidity())),
  (uint8_t)(highByte(int(mySensor.readFloatPressure()/10))),
    (uint8_t)(lowByte(int(mySensor.readFloatPressure()/10))),
  (uint8_t)(highByte(int(mySensor.readFloatAltitudeMeters()))),
    (uint8_t)(lowByte(int(mySensor.readFloatAltitudeMeters()))),
  (uint8_t)((int(mySensor.readTempC())+40)*2),
  (uint8_t)(highByte(int(myENS.getTVOC()))),
    (uint8_t)(lowByte(int(myENS.getTVOC()))),
  (uint8_t)(highByte(int(myENS.getECO2()))),
    (uint8_t)(lowByte(int(myENS.getECO2()))),
  (uint8_t)(0)
  };
```

### Encoding / Bits and bytes

We have seen several times throughout the exercises encoded float numbers into both HEX bytes and base64:
- HEX bytes have an ordering of bytes that represent numbers in a way that can be sorted by largest or smallest byte (big-endian or little-endian)


## LoRaWan stack

For our exercises, the LoRaWAN stack we have used is The Things Network (TTN).
A guide to using TTN can be found in [exercise 05](https://github.com/ITU-DASYALab/IoT_course/blob/main/exercises/IoT2024_exercise_05.md).

Some important keywords are:

- network and application server

- creating applications

- onboarding devices

- join process

## Data Integration

How to get data from the application server to data storage and analysis -

First of all, the applciations erver needs to decode what we send:

#### Decoder

You can add decoders under menu 

_Payload Formatters - uplink_

either on application level or device level.

Here is a js decoder script:


```
function Decoder(bytes, port) {

var decoded = {};
        
 decoded.humidity = bytes[0];
 decoded.pressure = ((bytes[1] << 8)
              + bytes[2])/10;
 decoded.altitude = (bytes[3] << 8)
              + bytes[4];
 decoded.temperature = bytes[5]/2-40;
 decoded.voc = (bytes[6] << 8)
              + bytes[7];
 decoded.co2 = (bytes[8] << 8)
              + bytes[9];
  return decoded;
}

```

#### MQTT 

We have used a local MQTT broker for some exercises, to learn how to use MQTT.


We can use the one provided by the Things Network (TTN) to read our data:

https://www.thethingsindustries.com/docs/integrations/other-integrations/mqtt/

In short form, we can read the published uplink messages like so (using the cmd line mosquitto client - but any other MQTT client will do!):

```
mosquitto_sub -h eu1.cloud.thethings.network -p 1883 -t "v3/{application id}@{tenant id}/devices/{device id}/up" -u "{application id}@{tenant id}" -P "{api_key}"

Example for one specific sensor node 

mosquitto_sub -h eu1.cloud.thethings.network -p 1883 -t "v3/iot2025-course@ttn/devices/iot2025-sebastian/up" -u "iot2025-course@ttn" -P "NNSXS.YU3AC2K7WN7FPGME32KAYCERB3YEEEHL6DW6RIY.WDLKCM6HC2VXNZDMU5NRMEUPD7MQSHX65K2LLABWBQX5KUHXWYZA"
```

#### Receiving MQTT messages 

##### Receiving MQTT messages - on your own computer

Again there are several options:

You could use __[Node-RED](https://nodered.org/)__ -
it has all the pre-made nodes for TTN, Influx, etc.


Another possibility is a __python script__ to run on your computer of choice:

[explanation](https://github.com/ITU-DASYALab/IoT_course/blob/main/guides/connect-ttn-influxdb-python.md)

[python code](https://github.com/ITU-DASYALab/IoT_course/blob/main/guides/ttn_code_examples/ttn-influx-db.py)

results in

```
(base) sebastian@x:~/nextcloud/itu/courses/IoT2025/code/python$ python3 mqtt_ingestion.py 
TTN Connected with result code Success
Received message
0 20 23 1024.3 0 65444
sebastian_mqtt_python,app_eui=CAFFEEBABE202505,dev_eui=D4D4DAFFFE5CDF94,device_id=iot2025-sebastian,port=1 altitude=65444i,co2=0i,humidity=20i,pressure=1024.3,temperature=23i,voc=0i 1742387392329750000
```

##### Receiving MQTT messages - in the backend

The database server also has the telegraf daemon, which can be used to ingest mqtt messages.

(We currently havent configured that. Might still do it until exercises time .. :) )



#### Webhooks

Webhhoks are configured in the TTN application, under

_Integrations_

They define URL endpoints - typically a script capable of receiving a POST request,
parsing and handling the incoming message. 

There is currently a script, a "webhook" at

```
https://influx.itu.dk/iot2025/integration/rec-01.php
```

which you might use).

This webhook handles any incoming messages that contain
a Device ID
and a decoded payload as defined above.

and adds it to a measurement "iot2025" in bucket "iot2025", tagged with the Device ID.

__WARNING! This script is currently not protected against malformatted messages!
In case your message does NOT contain the payload fields agreed on, it will likely just fail. At best ... :)__


## Timeseries Database

### InfluxDB

Any of the ingestion methods above write data to a bucket in InfluxDB, which we then visaulize.

## Data Visualization

We use [Grafana](https://grafana.com/) to visualize the data that we collected:

### Connecting data sources

When developing different visualizations in Grafana, we had to query our InfluxDB bucket to get the data that we wanted.
There are different ways to query an InfluxDB database:

- [Flux](https://docs.influxdata.com/influxdb/cloud/query-data/flux/)
- [InfluxQL](https://docs.influxdata.com/influxdb/v1/query_language/)

### Queries

[Here](https://github.com/ITU-DASYALab/IoT_course/blob/main/guides/ttn_code_examples/grafana_queries.md) are some examples of queries that can be used in Grafana to get the data from the measurements that we have made earlier.


## Overview of data flow

```
sensor node
||				{LoRa - LoRaWAN}
||
Gateway
||
||				{ethernet - TCP/IP}
||
||
TTN Network Server
TTN Application Server
||
||________________________________________________
||		||		||		||
||		||		||		||
mqtt		mqtt		mqtt		http POST
||		||		||		||
||		||		||		||
telegraf	python		Node-RED	webhook		
||		||		||		||
||		||		||		||
||______________||______________||______________||
||
InfluxDB
||
Grafana
||
(all kinds of data analytics)
```
