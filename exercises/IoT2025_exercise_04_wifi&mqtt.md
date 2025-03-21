# Exercise week 04
## Hello WiFi & MQTT! - Simple WiFi-program

### Before we begin, a status of where we are

(and if you are not there yet - ask! we have time!)

Our T-Beam boards are working and we connect through the Arduino IDE.

We got the LED blinking

We can scan for I2C devices:
```
Found address: 52 (0x34)
Found address: 83 (0x53)
Found address: 119 (0x77)
```

We can read sensors, e.g. for the Sparkfun Env Combo with BME280 and ENS160, each of with come with Examples (find them in the IDE menu).
Other sensors connected over I2C work largely the same, just with other libraries.

And we can combine them into one script:
```
Humidity: 15% Pressure: 103031 Pa Altitude: -141.1 m Temp: 28.82 C
Air Quality Index (1-5): 2
Total Volatile Organic Compounds: 112 ppb
CO2 concentration: 570 ppm
Gas Sensor Status Flag (0 - Standard, 1 - Warm up, 2 - Initial Start Up): 2
```

Critical look at sensor values?
Altitude really -141 m ??
Humidity?

What would we do about his? (==> Calibration!)

Now it's time to send measurements - we need to make a Wi-Fi connection and learn MQTT.

### Goal for the day

  * Familiarize yourself with the WiFi-functionality of the LilyGo-board
  * Setup and connect to WiFi on the board
  * Utilize the boards WiFi functionality to connect to a MQTT-broker

### The task

For this exercise, first we are going to send test messages and then a sensor reading (e.g. temperature) to a MQTT broker. 
MQTT is a protocol for message communication in between machines, where bandwidth often is restricted. 
It is not super low bandwidth though! Typically you find it in the data backend rather than in edge devices/nodes.
Why not in the nodes? Discuss! 

A good source for more information about MQTT and MQTT brokers can be found [here](https://aws.amazon.com/what-is/mqtt/).


First we need to install and include two packages:

    #include <WiFi.h>
    #include <PubSubClient.h>

We already have the WiFi package from the board manager and our T-Beam board - if not, install it (ESP32WiFi).
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

For our current exercise, the settings are here:

https://github.com/ITU-DASYALab/IoT_course/blob/main/exercises/IoT2025_exercise_04_settings_wifi_mqtt.md

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


- Should we agree on a good topic organistion? and not just post all in one topic?
- Should it look for something else being published on the channel?
- Should it send on a given time interval?
- Perhaps this could be done in the if (!mqtt_client.connected()) in the loop function?

### Optional: Making it secure: Adding SSL

In order to make a connection to the MQTT broker using SSL, we need to first add a new package to our file:

    #include <WiFiClientSecure.h>

This includes changing our WiFiClient to a WiFiClientSecure. It should look like this:

    WiFiClientSecure espClient;

In addition, we also have to change our port from TCP to SSL:

    const int mqtt_port = 8883;  

In our code, we also have to place our certificate somewhere in the top of your file:

    const char *ca_cert = R"EOF(
        -----BEGIN CERTIFICATE-----
        MIIFFjCCAv6gAwIBAgIRAJErCErPDBinU/bWLiWnX1owDQYJKoZIhvcNAQELBQAw
        TzELMAkGA1UEBhMCVVMxKTAnBgNVBAoTIEludGVybmV0IFNlY3VyaXR5IFJlc2Vh
        cmNoIEdyb3VwMRUwEwYDVQQDEwxJU1JHIFJvb3QgWDEwHhcNMjAwOTA0MDAwMDAw
        WhcNMjUwOTE1MTYwMDAwWjAyMQswCQYDVQQGEwJVUzEWMBQGA1UEChMNTGV0J3Mg
        RW5jcnlwdDELMAkGA1UEAxMCUjMwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEK
        AoIBAQC7AhUozPaglNMPEuyNVZLD+ILxmaZ6QoinXSaqtSu5xUyxr45r+XXIo9cP
        R5QUVTVXjJ6oojkZ9YI8QqlObvU7wy7bjcCwXPNZOOftz2nwWgsbvsCUJCWH+jdx
        sxPnHKzhm+/b5DtFUkWWqcFTzjTIUu61ru2P3mBw4qVUq7ZtDpelQDRrK9O8Zutm
        NHz6a4uPVymZ+DAXXbpyb/uBxa3Shlg9F8fnCbvxK/eG3MHacV3URuPMrSXBiLxg
        Z3Vms/EY96Jc5lP/Ooi2R6X/ExjqmAl3P51T+c8B5fWmcBcUr2Ok/5mzk53cU6cG
        /kiFHaFpriV1uxPMUgP17VGhi9sVAgMBAAGjggEIMIIBBDAOBgNVHQ8BAf8EBAMC
        AYYwHQYDVR0lBBYwFAYIKwYBBQUHAwIGCCsGAQUFBwMBMBIGA1UdEwEB/wQIMAYB
        Af8CAQAwHQYDVR0OBBYEFBQusxe3WFbLrlAJQOYfr52LFMLGMB8GA1UdIwQYMBaA
        FHm0WeZ7tuXkAXOACIjIGlj26ZtuMDIGCCsGAQUFBwEBBCYwJDAiBggrBgEFBQcw
        AoYWaHR0cDovL3gxLmkubGVuY3Iub3JnLzAnBgNVHR8EIDAeMBygGqAYhhZodHRw
        Oi8veDEuYy5sZW5jci5vcmcvMCIGA1UdIAQbMBkwCAYGZ4EMAQIBMA0GCysGAQQB
        gt8TAQEBMA0GCSqGSIb3DQEBCwUAA4ICAQCFyk5HPqP3hUSFvNVneLKYY611TR6W
        PTNlclQtgaDqw+34IL9fzLdwALduO/ZelN7kIJ+m74uyA+eitRY8kc607TkC53wl
        ikfmZW4/RvTZ8M6UK+5UzhK8jCdLuMGYL6KvzXGRSgi3yLgjewQtCPkIVz6D2QQz
        CkcheAmCJ8MqyJu5zlzyZMjAvnnAT45tRAxekrsu94sQ4egdRCnbWSDtY7kh+BIm
        lJNXoB1lBMEKIq4QDUOXoRgffuDghje1WrG9ML+Hbisq/yFOGwXD9RiX8F6sw6W4
        avAuvDszue5L3sz85K+EC4Y/wFVDNvZo4TYXao6Z0f+lQKc0t8DQYzk1OXVu8rp2
        yJMC6alLbBfODALZvYH7n7do1AZls4I9d1P4jnkDrQoxB3UqQ9hVl3LEKQ73xF1O
        yK5GhDDX8oVfGKF5u+decIsH4YaTw7mP3GFxJSqv3+0lUFJoi5Lc5da149p90Ids
        hCExroL1+7mryIkXPeFM5TgO9r0rvZaBFOvV2z0gp35Z0+L4WPlbuEjN/lxPFin+
        HlUjr8gRsI3qfJOQFy/9rKIJR0Y/8Omwt/8oTWgy1mdeHmmjk7j1nYsvC9JSQ6Zv
        MldlTTKB3zhThV1+XWYp6rjd5JW1zbVWEkLNxE7GJThEUG3szgBVGP7pSWTUTsqX
        nLRbwHOoq7hHwg==
        -----END CERTIFICATE-----
    )EOF";

Using this, we can modify our setup to allow for verifying our certificate:

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

        // ****** THIS IS NEW ******
        espClient.setCACert(ca_cert);
        // ****** THIS IS NEW ******

        mqtt_client.setServer(mqtt_broker, mqtt_port);
        mqtt_client.setKeepAlive(60);
        mqtt_client.setCallback(mqttCallback);
        while (!mqtt_client.connected()) {
            String client_id = "esp32-client-" + String(WiFi.macAddress());
            Serial.printf("Connecting to MQTT Broker as %s.....\n", client_id.c_str());
            if (mqtt_client.connect(client_id.c_str(), mqtt_username, mqtt_password)) {
                Serial.println("Connected to MQTT broker");
                mqtt_client.subscribe(mqtt_topic);
                mqtt_client.publish(mqtt_topic, "test"); // Publish message upon successful connection
            } else {
                Serial.print("Failed, rc=");
                Serial.print(mqtt_client.state());
                Serial.println(" try again in 5 seconds");
                delay(5000);
            }
        }
    }

### Acknowledgements

The code used to provide a basic connection for the MQTT broker is a modified version to the one found in this guide:

https://docs.emqx.com/en/cloud/latest/connect_to_deployments/esp32.html#connect-over-tls-ssl-port
