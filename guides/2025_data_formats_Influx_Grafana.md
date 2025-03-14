## Data format

```
Humidity: 	0 ... 100 			==> 1 byte
Pressure: 5 digits relevant, e.g. 1018.4 	==> 2 bytes ... 11 bits would do, but ....
Altitude: we want meters: 0 ... 50000 		==> 2 bytes
Temperature: 					==> 1 byte, bias shifted as (T+40)*2
VOC:	  					==> 2 bytes
CO2:						==> 2 bytes
```

With this, a possible data format to use on the ESP32 board:

```
byte senddata[] = {
  (uint8_t)(int(mySensor.readFloatHumidity())),
  (uint8_t)(highByte(int(mySensor.readFloatPressure()/10))),
    (uint8_t)(lowByte(int(mySensor.readFloatPressure()/10))),
  (uint8_t)(highByte(int(mySensor.readFloatAltitudeMeters()))),
    (uint8_t)(lowByte(int(mySensor.readFloatAltitudeMeters()))),
  (uint8_t)((int(mySensor.readTempC())+40)*2),
  (uint8_t)(highByte(int(myENS.getTVOC()))),
    (uint8_t)(lowByte(int(myENS.getTVOC()))),
  (uint8_t)(highByte(int(myENS.getECO2()))),
    (uint8_t)(lowByte(int(myENS.getECO2()))),
  (uint8_t)(0)
  };
```

## Payload decoder on The Things Network Application

```
function Decoder(bytes, port) {

var decoded = {};
        
 decoded.humidity = bytes[0];
 decoded.pressure = ((bytes[1] << 8)
              + bytes[2])/10;
 decoded.altitude = (bytes[3] << 8)
              + bytes[4];
 decoded.temperature = bytes[5]/2-40;
 decoded.voc = (bytes[6] << 8)
              + bytes[7];
 decoded.co2 = (bytes[8] << 8)
              + bytes[9];
  return decoded;
}

```

## InfluxDB / Data ingestion

There is currently a script, a "webhook" at

```
https://influx.itu.dk/iot2025/integration/rec-01.php
```

which you might use (or you may write/configure your own, e.g. using node-red, telegraf or any script language of your choice).

This webhook handles any incoming messages that contain
a Device ID
and a decoded payload

and adds it to a measurement "iot2025" in bucket "iot2025", tagged with the Device ID.

The raw messages look like this:

```
s:1442:"{"end_device_ids":{"device_id":"iot2025-sebastian","application_ids":{"application_id":"iot2025-course"},"dev_eui":"D4D4DAFFFE5CDF94","join_eui":"CAFFEEBABE202505","dev_addr":"260B9B83"},"correlation_ids":["gs:uplink:01JNX3CYHVSYN8N90JRHK3N720"],"received_at":"2025-03-09T09:22:25.671340777Z","uplink_message":{"session_key_id":"AZV6KtR70+laBDdN1ryqYA==","f_port":1,"f_cnt":6,"frm_payload":"GyeRAACKADwB3Q==","decoded_payload":{"altitude":0, "co2":477, "humidity":27, "pressure":1012.9, "temperature":29, "voc":60},"rx_metadata":[{"gateway_ids":{"gateway_id":"new-purple-home","eui":"B827EBFFFEAA8FF3"},"time":"2025-03-09T09:22:35.688Z","timestamp":2055542779,"rssi":-39,"channel_rssi":-39,"snr":8,"location":{"latitude":55.685867242712696,"longitude":12.55436934346968,"altitude":15,"source":"SOURCE_REGISTRY"},"uplink_token":"Ch0KGwoPbmV3LXB1cnBsZS1ob21lEgi4J+v//qqP8xD7r5TUBxoMCNG7tb4GEMyVyd4BIPjYlr/p03UqDAjbu7W+BhCAmIjIAg==","channel_index":2,"gps_time":"2025-03-09T09:22:35.688Z","received_at":"2025-03-09T09:22:25.466766540Z"}],"settings":{"data_rate":{"lora":{"bandwidth":125000, "spreading_factor":7, "coding_rate":"4/5"}}, "frequency":"868500000", "timestamp":2055542779, "time":"2025-03-09T09:22:35.688Z"},"received_at":"2025-03-09T09:22:25.468189461Z","consumed_airtime":"0.061696s","network_ids":{"net_id":"000013","ns_id":"EC656E0000000181","tenant_id":"ttn","cluster_id":"eu1","cluster_address":"eu1.cloud.thethings.network"}}}";
```

The corresponding Influx command looks like this:

```
curl --request POST \
"http://localhost:8086/api/v2/write?org=iot2025&bucket=iot2025&precision=s" \
  --header "Authorization: Token JxwpvAuulwm_JXhZcPZVetmdqBu51WRmNalD8VcMUp35QZt1DjQZvXDXpiJbWFZhs-sn5jN0cb6LlDRrqd3kUw==" \
  --header "Content-Type: text/plain; charset=utf-8" \
  --header "Accept: application/json" \
  --data-binary 'iot2025,dev_id=iot2025-sebastian temperature=29,humidity=27,co2=549,voc=100,altitude=0,pressure=1012.8,devEUI="D4D4DAFFFE5CDF94",apptime="2025-03-09T09:26:38.368103574Z",apptimestamp=1741508798,sf=7,gateway="new-purple-home",rssi=-39,frequency=867100000 1741508798' 
```

You find the necessary information in this, in case you d like to write your own data in.

## Grafana

You can access Grafana here:

https://influx.itu.dk:3000/

(at the moment with one shared user:
```
2025student
eej4Raipie4f
```

- we might make individual users once we find time :) )

You can create dashboards and graphs.

