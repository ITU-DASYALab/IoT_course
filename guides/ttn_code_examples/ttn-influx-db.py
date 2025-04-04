from paho.mqtt.client import Client
import paho.mqtt.client as mqtt

import influxdb_client
from influxdb_client import Point
from influxdb_client.client.write_api import SYNCHRONOUS
import json


#### NOTE you may have to adjust these settings!!! READ what you copypaste! :)

TTN_ADDRESS = "eu1.cloud.thethings.network"
TTN_PORT = 1883
TTN_USER = "iot2025-course@ttn"
TTN_PASS = "NNSXS.YU3AC2K7WN7FPGME32KAYCERB3YEEEHL6DW6RIY.WDLKCM6HC2VXNZDMU5NRMEUPD7MQSHX65K2LLABWBQX5KUHXWYZA"
ttn_client = Client(mqtt.CallbackAPIVersion.VERSION2)

INFLUX_TOKEN = "JxwpvAuulwm_JXhZcPZVetmdqBu51WRmNalD8VcMUp35QZt1DjQZvXDXpiJbWFZhs-sn5jN0cb6LlDRrqd3kUw=="

INFLUX_ORG = "iot2025"
INFLUX_URL = "http://influx.itu.dk:8086"
INFLUX_BUCKET = "iot2025"

measurement_name = "YOUR_NAME_measurement"

# Set up InfluxDB Client
write_client = influxdb_client.InfluxDBClient(url=INFLUX_URL, token=INFLUX_TOKEN, org=INFLUX_ORG)
write_api = write_client.write_api(write_options=SYNCHRONOUS)


# Set up callbacks for MQTT events
# The callback for when the client receives a CONNACK response from the server.
def on_ttn_connect(client, _userdata, _flags, return_code, _properties):
    print("TTN Connected with result code "+str(return_code))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    subscribe_string = "v3/" + TTN_USER + "/devices/+/up"

    client.subscribe(subscribe_string)


# The callback for when a PUBLISH message is received from the server.
def on_ttn_message(client, userdata, msg):
    message = json.loads(msg.payload)

    if "decoded_payload" in message["uplink_message"].keys():

        decoded_co2 = message["uplink_message"]["decoded_payload"].get("co2")
        decoded_humidity = message["uplink_message"]["decoded_payload"].get("humidity")
        decoded_temperature = message["uplink_message"]["decoded_payload"].get("temperature")
        print(decoded_co2, decoded_humidity, decoded_temperature)
        # we recieve and read the relevant information into tags and fields
        # please replace with your name!

        point = Point(measurement_name) \
            .tag("device_id", message["end_device_ids"]["device_id"]) \
            .tag("dev_eui", message["end_device_ids"]["dev_eui"]) \
            .tag("app_eui", message["end_device_ids"]["join_eui"]) \
            .tag("port", int(message["uplink_message"]["f_port"])) \
            # NOTE we have hardcoded our payload format here - if we send different measuremnets, keys, values, we need to adjust!
            .field("co2", decoded_co2) \
            .field("humidity", decoded_humidity) \
            .field("temperature", decoded_temperature) \
            .field("pressure", decoded_pressure) \
            .field("voc", decoded_voc) \
            .field("altitude", decoded_altitude) \
            .time(message["received_at"])  # Fix the timestamp to be the TTN received time
            .time(message["received_at"])  # Fix the timestamp to be the TTN received time
            
        print(point)
        write_api.write(bucket=INFLUX_BUCKET, org=INFLUX_ORG, record=point)


# set up iot client for TTN
ttn_client.on_connect = on_ttn_connect
ttn_client.on_message = on_ttn_message
ttn_client.username_pw_set(TTN_USER, TTN_PASS)
ttn_client.connect(TTN_ADDRESS, TTN_PORT, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
ttn_client.loop_forever()
