For Wi-Fi and MQTT connections, you need:


```

// WiFi settings
const char *ssid = "sensors";             // Replace with your WiFi name
const char *password = "gQx694ne";     // Replace with your WiFi password

    
// MQTT Broker settings
const char *mqtt_broker = "influx.itu.dk";     // EMQX broker endpoint
const char *mqtt_topic = "iot2024/04";      // MQTT topic
const char *mqtt_username = "iot2024";   // MQTT username for authentication
const char *mqtt_password = "r34lth1ng";   // MQTT password for authentication
const int mqtt_port = 1883;         // MQTT port (TCP), dpends on whether we use TLS or non-TLS

```
