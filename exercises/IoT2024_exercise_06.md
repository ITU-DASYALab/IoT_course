# Exercise week 06
## Hello InfluxDB!

### Goal for the day

  * Send CO2, temperature and humidity data using LoRa to the The Things Network (TTN)
  * Listen to TTN's MQTT broker and save data in InfluxDB using Python
  * Visualized the data saved in InfluxDB in Grafana

### The task

This weeks exercise is made up of three elements:

- Setup your board and use the example script ([main.ino](https://github.com/ITU-DASYALab/IoT_course/blob/main/guides/ttn_code_examples/main.ino) + [payload_decoder.js](https://github.com/ITU-DASYALab/IoT_course/blob/main/guides/ttn_code_examples/payload_decoder.js)) or your own script from last exercise session to push temperature/CO2/humidity-measurements to The Things Network (TTN).
- Setup a Python script that connect InfluxDB to TTN. You can find a guide [here](https://github.com/ITU-DASYALab/IoT_course/blob/main/guides/connect-ttn-influxdb-python.md).
- Setup a Grafana dashboard that displays the data you have sent to InfluxDB. You can find a guide [here](https://github.com/ITU-DASYALab/IoT_course/blob/main/guides/using_Grafana.md). 

In the end, the goal is that you will have a setup where your board records some environment measurement, passes it to InfluxDB using your Python script, and finally visualizes the saved data in Grafana.

Good luck! :)
