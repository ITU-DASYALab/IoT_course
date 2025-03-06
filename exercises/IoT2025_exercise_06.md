## Exercise Data Stacks, part 1

### Goal, long run

  * Get our data from the board via LoRaWAN/TTN to a data backend, e.g. InfluxDB, for further processing, analytics and visualization, e.g. with Grafana


### Goal for the day

  * Send one or some sensor reading(s) using LoRaWAN to the The Things Network (TTN)
      * In order to do that, we need to revisit fatatypes, conversions, formats ... 
        We will read this together: https://www.thethingsnetwork.org/docs/devices/bytes/ 
  * Listen to TTN's MQTT broker to receive your data - this is how: 

```
mosquitto_sub -h <TTN-MQTT-server> -p 1883/8883 -t "#" -u "<applicationName>" -P "<API-key>"
```

  * Begin to think of how to get data from TTN into our database, baed on lecture

### The task

This weeks exercise is made up of three elements:

- Setup your board and use the example script ([main.ino](https://github.com/ITU-DASYALab/IoT_course/blob/main/guides/ttn_code_examples/main.ino) + [payload_decoder.js](https://github.com/ITU-DASYALab/IoT_course/blob/main/guides/ttn_code_examples/payload_decoder.js)) or your own script from last exercise session to push temperature/CO2/humidity-measurements to The Things Network (TTN).



