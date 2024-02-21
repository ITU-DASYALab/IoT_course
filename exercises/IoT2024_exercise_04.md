# Exercise week 04
## Hello WiFi & MQTT! - Simple WiFi-program

### Goal for the day

  * Familiarize yourself with the WiFi-functionality of the LilyGo-board
  * Setup and connect to WiFi on the board
  * Utilize the boards WiFi functionality to connect to a MQTT-broker

### The task

For this exercise, we are going to utilize the temperature/CO2-sensor we hooked up to our board to send the temperature of the board to a MQTT broker. 
MQTT is a protocol for message communication in between machines, where bandwidth often is restricted. 
A good source for more information about MQTT and MQTT brokers can be found [here](https://aws.amazon.com/what-is/mqtt/).


First we need to install and include two packages:

    #include <WiFi.h>
    #include <PubSubClient.h>

We already have the WiFi package from the board manager and our T-Beam board. 
However, in order to be able to use the PubSubClient we need to install the "PubSubClient" library by Nick O'Leary. 
You can find this using the library manager as you did in previous exercises. 
If interested, you can read more about the library [here](https://github.com/knolleary/pubsubclient) (might be useful if there is something in the code you are unsure what means).

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

It is also needed to define these two global variables:

    WiFiClient espClient;
    PubSubClient mqtt_client(espClient);

We then have to write our initial setup function, where we also connect to WiFi and define our connection to the MQTT broker:

    void setup() {
      Serial.begin(115200);

      // Connect to WiFi
      WiFi.begin(ssid, password);
      Serial.print("Connecting to WiFi");
      while (WiFi.status() != WL_CONNECTED) {
          delay(500);
          Serial.print(".");
      }
      Serial.println("\nConnected to WiFi");

      // Setup MQTT broker connection
      mqtt_client.setServer(mqtt_broker, mqtt_port);
      mqtt_client.setKeepAlive(60);
      mqtt_client.setCallback(mqttCallback);
      while (!mqtt_client.connected()) {
          String client_id = "esp32-client-" + String(WiFi.macAddress());
          Serial.printf("Connecting to MQTT Broker as %s.....\n", client_id.c_str());
          if (mqtt_client.connect(client_id.c_str(), mqtt_username, mqtt_password)) {
              Serial.println("Connected to MQTT broker");
              mqtt_client.subscribe(mqtt_topic);
              mqtt_client.publish(mqtt_topic, "Your message"); // Publish some message upon successful connection
          } else {
              Serial.print("Failed, rc=");
              Serial.print(mqtt_client.state());
              Serial.println(" try again in 5 seconds");
              delay(5000);
          }
      }
    }

As you can see in this setup function, we call a *.setCallBack()*-method on the mqtt_client variable we defined earlier.
The function we set here will be called when there is something published to the channel that we subscribe to.
Such a function could look something like this:

    void mqttCallback(char *mqtt_topic, byte *payload, unsigned int length) {
      Serial.print("Message received on mqtt_topic: ");
      Serial.println(mqtt_topic);
      Serial.print("Message: ");
      for (unsigned int i = 0; i < length; i++) {
          Serial.print((char) payload[i]);
      }
      Serial.println("\n-----------------------");
    }

To ensure we keep the connection upon, we can in the loop function check if the connection is still intact, and if not, do the same as we did in *setup()* and connect the broker again.
Otherwise we just use the loop()-method on the broker to keep the connection alive.

    void loop() {
        if (!mqtt_client.connected()) {
          while (!mqtt_client.connected()) {
              String client_id = "esp32-client-" + String(WiFi.macAddress());
              Serial.printf("Connecting to MQTT Broker as %s.....\n", client_id.c_str());
              if (mqtt_client.connect(client_id.c_str(), mqtt_username, mqtt_password)) {
                  Serial.println("Connected to MQTT broker");
                  mqtt_client.subscribe(mqtt_topic);
              } else {
                  Serial.print("Failed, rc=");
                  Serial.print(mqtt_client.state());
                  Serial.println(" try again in 5 seconds");
                  delay(5000);
              }
          }
        }
        mqtt_client.loop();
    }

Here you can see that we subscribe to a topic and publish something.
Your task however is to define how we publish the temperature to this topic. 
Try and incoporate the example you were working on last time, and see if you are able to publish the temperature to the MQTT broker. 
It is also up to you to consider how/when the broker should publish new temperatures to the channel:

- Should it look for something else being published on the channel?
- Should it send on a given time interval?
- Perhaps this could be done in the if (!mqtt_client.connected()) in the loop function?

### Acknowledgements

The code used to provide a basic connection for the MQTT broker is a modified version to the one found in this guide:

https://docs.emqx.com/en/cloud/latest/connect_to_deployments/esp32.html#connect-over-tls-ssl-port