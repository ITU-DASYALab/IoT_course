


## Read more

https://www.thethingsindustries.com/docs/integrations/mqtt/

## Prerequisites

On TTN, create an API Key
via
==> Integrations ==> MQTT

## Topics

The Things Network Application Server publishes uplink traffic on the following topics:

```
    v3/{application id}@{tenant id}/devices/{device id}/join
    v3/{application id}@{tenant id}/devices/{device id}/up     <== we are mostly interested in this
    v3/{application id}@{tenant id}/devices/{device id}/down/queued
    v3/{application id}@{tenant id}/devices/{device id}/down/sent
    v3/{application id}@{tenant id}/devices/{device id}/down/ack
    v3/{application id}@{tenant id}/devices/{device id}/down/nack
    v3/{application id}@{tenant id}/devices/{device id}/down/failed
    v3/{application id}@{tenant id}/devices/{device id}/service/data
    v3/{application id}@{tenant id}/devices/{device id}/location/solved
```
   
## How to listen

```
mosquitto_sub -h <TTN-MQTT-server> -p 1883/8883 -t "#" -u "<applicationName>" -P "<API-key>"
```

### Example

Our lab co2 data is at

```
mosquitto_sub -h eu1.cloud.thethings.network -p 1883 -t "#" -u "dasya-co2-001@ttn" -P "NNSXS.NFBMRAJAH2NAT32PK626N44JNPPYUOKWUPRTEYA.RYINDYX7ZTL2XL54VK5RFVGYCK73IGIJKZJUQ3IOGI5GQOSNG3WA"	
```


or specifically for the lab sensor (DevID eui-70b3d54990564b35)
```
mosquitto_sub -h eu1.cloud.thethings.network -p 1883 -t "	" -u "	" -P "NNSXS.NFBMRAJAH2NAT32PK626N44JNPPYUOKWUPRTEYA.RYINDYX7ZTL2XL54VK5RFVGYCK73IGIJKZJUQ3IOGI5GQOSNG3WA"
```
## telegraf

Use web GUI to make a telegraf config for an mqtt consumer

```
telegraf --config http://influx.itu.dk:8086/api/v2/telegrafs/0ca6c4661e41d000
```

the MQTT part looks like this
```
[[inputs.mqtt_consumer]]

  servers = ["tcp://eu1.cloud.thethings.network:1883"]
  topics = [
    "v3/dasya-co2-001@ttn/devices/eui-70b3d54990564b35/up"	
  ]
  
  username = "dasya-co2-001@ttn"
  password = "NNSXS.NFBMRAJAH2NAT32PK626N44JNPPYUOKWUPRTEYA.RYINDYX7ZTL2XL54VK5RFVGYCK73IGIJKZJUQ3IOGI5GQOSNG3WA"
  
  data_format = "json"
```





then start telegraf like so:
```
root@influx:/home/sebastian# telegraf --config http://influx.itu.dk:8086/api/v2/telegrafs/0ca6c4661e41d000
2024-02-27T15:20:03Z I! Loading config: http://influx.itu.dk:8086/api/v2/telegrafs/0ca6c4661e41d000
2024-02-27T15:20:03Z I! Starting Telegraf 1.29.5 brought to you by InfluxData the makers of InfluxDB
2024-02-27T15:20:03Z I! Available plugins: 241 inputs, 9 aggregators, 30 processors, 24 parsers, 60 outputs, 6 secret-stores
2024-02-27T15:20:03Z I! Loaded inputs: mqtt_consumer
2024-02-27T15:20:03Z I! Loaded aggregators: 
2024-02-27T15:20:03Z I! Loaded processors: 
2024-02-27T15:20:03Z I! Loaded secretstores: 
2024-02-27T15:20:03Z I! Loaded outputs: influxdb_v2
2024-02-27T15:20:03Z I! Tags enabled: host=influx.itu.dk
2024-02-27T15:20:03Z I! [agent] Config: Interval:10s, Quiet:false, Hostname:"influx.itu.dk", Flush Interval:10s
2024-02-27T15:20:08Z I! [inputs.mqtt_consumer] Connected [tcp://eu1.cloud.thethings.network:1883]
```
