# Connect TTN and InfluxDB

*Acknowledgement:* This guide and attached code is heavily inspired by last years TA, Kasper: https://github.itu.dk/khjo/IoT2023-TestBedResources/blob/main/Using%20MQTT.md

## Influx DB Basics
InfluxDB is a time-series optimised database and as such is quite different than normal SQL-like databases.

That also mean that the way they store and describe data is different. The main concepts are:

- Buckets: Where data is stored. Can contain multiple measurements. In our case it contains one called "message" since it represents messages from your devices
- Measurements: Measurements are streams of Points who share the same tags.
- Points: Each Point has a Timestamp, one or more tags and a single field. Tags are often meta-data and the field is often the value we measure.
- Tags: Are key-value pairs of data that doesn't change often. In our case the dev_eui is a tag, since it provides context for the data and it is not prone to change.
- Fields: are key-value pairs that are prone to change. In our case its the actual payload of the device.
- Timestamp: The specific time in which this data was recorded

## InfluxDB & TTN connection

In the attached code (ttn-influx-db.py), I have added an example Python script that connects to TTN and InfluxDB.
This script utilizes the MQTT broker that TTN provides.
In the script, we connect to this MQTT broker, listen to any **UP**-events (which are the measurements that we send over LoRa to our end-node), and writes these to the database.
In a "production"-environment, such a script would probably run all the time on some VM. 
However, in the case of this exercise, it is enough that you run it on your computer for the duration of this exercise.

In order to run the script, you need to install two packages:

    pip install influxdb-client
    pip install paho-mqtt

After installing the packages, you also need to make some configurations to the script.
First you have to adjust the TTN accodring to below:

    TTN_ADDRESS = "eu1.cloud.thethings.network"
    TTN_PORT = 1883
    TTN_USER = "<redacted>" # Here you need to add the name of your application in this format: application-id@ttn
    TTN_PASS = "<redacted>" # Here you need to create your own API key in the TTN console
    ttn_client = Client(mqtt.CallbackAPIVersion.VERSION2)

You also have to update the Influx token as below:

    INFLUX_TOKEN = "<redacted - how should this be distributed?>"

And I also recommend updating the measurement name to something that makes sense to you/your group:

    measurement_name = "bjornars_measurement"

Running the script while receiving a message to your application from your board should look something like this:

    python .\ttn-influx-db.py
    TTN Connected with result code Success
    message received
    message,app_eui=***,dev_eui=***,device_id=***,port=1 payload="RVRUVFQ=" ***
