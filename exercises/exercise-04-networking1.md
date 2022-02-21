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

---




