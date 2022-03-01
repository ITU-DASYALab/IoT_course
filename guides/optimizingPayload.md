## Payload Exercise

Currently your CO2 sensing device is in a system where it has (near) unlimited
power and (near) unlimited bandwidth, meaning that we can send a lot of data
often. Most IoT devices are not so lucky. In this exercise we will look at adapting
your payload to contrained conditions where every bit counts.

### Your current payload

  * How does your current payload look, and how is your data encoded?
  * How many bytes are you sending per measurement?
  * For this calculation you can exclude the meta data like topic or QoS
  * How many messages are you sending pr hour?
  * How many bytes per hour?
  
### Designing a smaller payload

Imagine that your device was somewhere in the himalayas, running on battery
on a low-bandwidth network.

  * Design a new payload with a minimal footprint.
  * You need to trade off the small size for reduced precision.
  * What would be a reasonable amount of precision given this sensor?
  
  * Explain your new payload format. How is the data encoded?
  
  * How many bytes per measurement?
  * How would you handle metadata in this case?
  
Assuming that this is general environmental monitoring of other gases or
pollutants, how often would you send a message? You might seed to talk
about your assumptions for the system here.

  * How many bytes per hour?
  
Assume that this is a larger deployment with 10.000 devices. 

  * How much network traffic can you save by using your new payload scheme?
