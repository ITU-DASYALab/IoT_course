## Exercise 1 - MQTT


The initial version of our MQTT broker allowed

a. anonymous publishing
b. http connections (not https)

We got contacted by DK-CERT and asked to change our configuration,
to have either one of these, but not both.
Please analyze this vulnerability by applying a
Confidentiality-Integrity-Availability approach.
Which aspects are affected by these two measures, and how?
What are possible exploits?

## Exercise 2 - CTF - compromise security of our own sensors

The sensor output is here:

https://training.itu.dk:3000/d/7f-VNsLGl/iot2021-co2-sebastian-2-currently_lab?orgId=1

you have access with
```
iot2025
very34sy
```



Let us assume that our sensor was a little more important than it is now.
For example, if a facility management depended on the data,
and could be forced to take action, even evacuate rooms.

Or, if this was indeed a smoke sensor, or a geiger counter.



Take starting point in slides on
IoT attack surfaces areas 
& Hypothetical scenario (approx slide 37/38) and suggest attacks. 

How could the system be attacked?
What aspects (C-I-A) are affected?
How could you protect your system against each of these?

Let us do this in teams.

An evil team -

### Suggest attacks

Explain your motivation, goals and strategy


A good team -

### Suggest defenses

How would you mitigate such attacks?
Preemptively, after attack, …


What are the IoT/LoRaWAN specifics here?
