# Assignment 1 - A networked sensor node

Please note that we connect exercises 2-6 and accompanying questions to this assignment.
Find them below.

You are not expected to hand in a report or such, but we encourage you to go through the questions,
and you are welcome to hand in answers for review by the teaching team.

## Idea

Monitoring of indoor climate is a relevant task, and more so in time of covid,
as the general room climate coorelates to some extent with aerosol concentrations.
CO2 (carbondioxide) concentrations are a good marker for indoor climate.

We draw some inspiration here from a widely popular german project, #Co2Ampel:
https://twitter.com/search?q=%23co2ampel

Most of the existing implementations are Arduino/C based, whereas we will work on

embedded python aka micropython on an ESP32 board.

The general goal is to measure, communicate and store CO2 concentrations, Temperature and relative humidity.

You have some freedom of choice as to how you achieve this, e.g.

- which networking technology to use (it could be Wi-Fi, sigfox, LoRa, bluetooth, ..)
- what additonal user interfaces you implement (local display? LEDs, sounds, mobile app notifications, ..?)
- which data backend you choose

All these design choices will be tightly connected to things we talk about in the lectures, and will require your active input -
come up with your idea and request support as needed! You are welcome to work on variations of this general idea.

## Base kit

pycom LoPy4 boards & accessories (expansion board, antenna, display, batteries (where needed), ...)
https://docs.pycom.io/datasheets/development/lopy4/

A sensirion SCD30
https://www.sensirion.com/en/environmental-sensors/carbon-dioxide-sensors/carbon-dioxide-sensors-co2/


Here are some good starting points:

pycom general doc
https://docs.pycom.io/

LoPy4 pinout
https://docs.pycom.io/gitbook/assets/lopy4-pinout.pdf

SCD30 lib
https://github.com/agners/micropython-scd30

Display lib (optional)
https://github.com/mcauser/micropython-pcd8544

MQTT lib
https://github.com/pycom/pycom-libraries/blob/master/examples/mqtt/mqtt.py

I2C doc
https://docs.pycom.io/firmwareapi/pycom/machine/i2c/#app

---

# Exercises connected to this Assignment


## Exercise 2 - Embedded Systems

### Goal for the day

  * Familiarize yourself with a LoPy4 board
  * Connect to it
  * Say "Hello World".

The guide is here:

https://github.com/ITU-DASYALab/IoT_course/blob/main/guides/gettingStartedWithPycom.md

### Optional

and if you are ambitious:

  * code a little sleep loop

https://docs.pycom.io/tutorials/basic/sleep/


### Accompanying Questions:

  * What are key components of an embedded system?
  * What are some common relevant pins and connectors of an embedded board?
  * What are common ways of interacting with an embedded system during development and deployment?
  * What are the constraints you would expect when designing an indoor air quality sensor system?
  * How does sleep mode work? 
  * How do we wake up?
  * Can you run Linux on a esp32?

---

## Exercise 3 - Sensors

### Goal for the day

  * Understand how a sensor works - from "real world property" to digital reading
  * Understand sensor terminology
  * Understand the importance of calibration
  * Learn how to connect and read an air quality sensor

For our concrete example, the Sensirion SCD30, there is a micropython library:
https://github.com/agners/micropython-scd30

In order to make this work, you will need to understand how to work with libraries in micropython,
on embedded boards - where they go, how to use them.
Also, pay attention - not every sample code is perfect or complete.

There are valuable hints on in this [Teams-post](https://teams.microsoft.com/l/message/19:ebx-0qQEyExpjRK8hQpPJFXx72WsjsymOEbmUx8r3dY1@thread.tacv2/1644422368141?tenantId=bea229b6-7a08-4086-b44c-71f57f716bdb&groupId=5b99cef7-1831-4e1d-8a36-06654ffca320&parentMessageId=1644422368141&teamName=IoT2022&channelName=General&createdTime=1644422368141)

### Accompanying Questions:

- What is the difference between analog and digital sensors?
- What is an ADC? What are its interesting parameters?
- How do we communicate with sensors on a board?
- What are the most important performance characteristics of a sensor?
- What are indicators of data integrity and quality?
- What strategies for calibration of sensors do you know?
- For our concrete example, CO2 measuremnets, what can be said about the values we measure, and their meaning?
- What are examples of actuators that you could use to provide local feedback on sensor data?

---

## Exercise 4
## Networking 1 - Wi-Fi and MQTT

### Goal for the day

  * Connect the LoPy4 board to a Wi-Fi network
  * Understand the MQTT protocol
  * Send data via MQTT
    * from laptop and/or phone
    * from the LoPy4

### MQTT server info you need:

Server/broker:	influx.itu.dk
Port:		8883 SSL / perhaps 1883 without encryption

In case you need certificates:	
		https://influx.itu.dk/certs/

MQTT User:	iot2022
Password:	50b1ll10n

	topic readwrite IoT2022sec/#
	topic readwrite IoT2022/#
	topic readwrite test/#




#### MQTT from your laptop (and/or phone)

Install an MQTT client of your liking, e.g. via
https://mqtt.org/software/
https://www.hivemq.com/mqtt-toolbox/
https://www.eclipse.org/paho/index.php?page=downloads.php

Connect to broker, publish and subscribe to topics.


#### MQTT from LoPy4

Pycom MQTT example: 
https://docs.pycom.io/tutorials/networkprotocols/mqtt/
Library:
https://github.com/pycom/pycom-libraries/blob/master/examples/mqtt/mqtt.py

#### Optional, if you are ambitious

Write a python script or use a tool such as Node-RED to listen to and store incoming messages.

If you have access to some cloud instance or a Pi, install and run your own MQTT broker.


### Accompanying Questions:

- What network options do you see for your indoor air sensor?
- What are their benefits and disadvantages?
- In particular, how would you compare Wi-Fi, Bluetooth, Mobile?
- What kind of data is MQTT suitable for?
- What are some prerequisites for using MQTT?
- What can you say about security measures in MQTT?

---




