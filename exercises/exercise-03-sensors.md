## Exercise 3
## Sensors

### Goal for the day

  * Understand how a sensor works - from "real world property" to digital reading
  * Understand sensor terminology
  * Understand the importance of calibration
  * Learn how to connect and read an air quality sensor

For our concrete example, the Sensirion SCD30, there is a micropython library:
https://github.com/agners/micropython-scd30

In order to make this work, you will need to understand how to work with libraries in micropython,
on embedded boards - where they go, how to use them.
Also, pay attention - not every sample code is perfect or complete.

There are valuable hints on in this [Teams-post](https://teams.microsoft.com/l/message/19:ebx-0qQEyExpjRK8hQpPJFXx72WsjsymOEbmUx8r3dY1@thread.tacv2/1644422368141?tenantId=bea229b6-7a08-4086-b44c-71f57f716bdb&groupId=5b99cef7-1831-4e1d-8a36-06654ffca320&parentMessageId=1644422368141&teamName=IoT2022&channelName=General&createdTime=1644422368141)

## Accompanying Questions:

- What is the difference between analog and digital sensors?
- What is an ADC? What are its interesting parameters?
- How do we communicate with sensors on a board?
- What are the most important performance characteristics of a sensor?
- What are indicators of data integrity and quality?
- What strategies for calibration of sensors do you know?
- For our concrete example, CO2 measuremnets, what can be said about the values we measure, and their meaning?
- What are examples of actuators that you could use to provide local feedback on sensor data?
