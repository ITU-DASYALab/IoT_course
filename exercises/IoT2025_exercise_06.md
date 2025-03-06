## Exercise Data Stacks, part 1

### Goal, long run

  * Get our data from the board via LoRaWAN/TTN to a data backend, e.g. InfluxDB, for further processing, analytics and visualization, e.g. with Grafana


### Goal for the day

  * Send one or some sensor reading(s) using LoRaWAN to the The Things Network (TTN)
      * In order to do that, we need to revisit datatypes, conversions, formats ... 
        We will read this together: https://www.thethingsnetwork.org/docs/devices/bytes/ 


  * Based on our discussion, let us agree on one shared formatting of our data - to the extent possible.
  

  * Listen to TTN's MQTT broker to receive your data - this is how: 

```
mosquitto_sub -h <TTN-MQTT-server> -p 1883/8883 -t "#" -u "<applicationName>" -P "<API-key>"
```

Note that you need to make an API key for this!

Further explanation of the MQTT connection to TTN here: https://github.com/ITU-DASYALab/IoT_course/blob/main/guides/TTN-MQTT-telegraf-Influx.md

  * Begin to think of how to get data from TTN into our database, baed on lecture





