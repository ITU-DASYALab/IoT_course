# Exercise week 04
## Hello WiFi! - Simple WiFi-program

### Goal for the day

  * Familiarize yourself with the WiFi-functionality of the LilyGo-board
  * Setup and connect to WiFi on the board
  * Write and upload programs allowing for your board to act as a HTTP client/server

### The task

For this exercise, we are going to utilize the temperature/CO2-sensor we hooked up to our board to send the temperature of the board to a MQTT broker. MQTT is a protocol for message communication in between machines, where bandwidth often is restricted. A good source for more information about MQTT and MQTT brokers can be found [here](https://aws.amazon.com/what-is/mqtt/).


First we need to install and include two packages:

    #include <WiFi.h>
    #include <PubSubClient.h>

We already have the WiFi package from the board manager and our T-Beam board. However, in order to be able to use the PubSubClient we need to install the "PubSubClient" library by Nick O'Leary. You can find this using the library manager as you did in previous exercises. If interested, you can read more about it [here](https://github.com/knolleary/pubsubclient).

Up next we have to define some constants that we use to verify our connection.
These constants can look something like this for WiFi:

    // WiFi settings
    const char *ssid = "wifi_name";             // Replace with your WiFi name
    const char *password = "wifi_password";     // Replace with your WiFi password

And something like this for the connection to your MQTT broker:

    // MQTT Broker settings
    const char *mqtt_broker = "****";     // EMQX broker endpoint
    const char *mqtt_topic = "****";      // MQTT topic
    const char *mqtt_username = "****";   // MQTT username for authentication
    const char *mqtt_password = "****";   // MQTT password for authentication
    const int mqtt_port = ******;         // MQTT port (TCP)

We then have to write our initial setup function, where we also connect to WiFi:

    setup

In the loop, we define how we want to connect to the MQTT broker.

    loop

Here you can see that we subscribe to a topic and publish something in the publish function. Your task however is to define how we publish the temperature to this topic. Try and incoporate the example you were working on last time, and see if you are able to publish the temperature to the MQTT broker.

