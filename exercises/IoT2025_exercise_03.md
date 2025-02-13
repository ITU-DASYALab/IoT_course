# Exercise week 03
## Hello Sensors! - Simple sensor programs

### Goal for the day

  * Familiarize yourself with the connections of a LilyGo-board, and with using a breadboard
  * Connect a sensor (or several) to the board
  * Read and understand the output of the sensor

### Connecting and reading an external Sensor

**Note before we start:** Remember when working with physical computing, there is always a risk of things going wrong and breaking, different from software.
Therefore, double-check you use the correct pins and make sure that your cables are away from the battery before even starting the device - just to be on the sure side ;)

Also, be aware that connections made via jumper cables and breadboard can be shaky -
and of course nothing you find in real IoT devices.
Before despairing, check and move all cables!

#### Connecting the external sensor

Before we start writing code, let's connect the sensor to our board.

This time around, we are offering a variety of sensors:

| Sensor               | for| Doc|
|-----------------------|-------|-------|
|SparkFun Env ENS160/BME280| TAQI, TVOCs, CO2, barometric pressure, humidity, and temperature | https://www.sparkfun.com/sparkfun-environmental-combo-breakout-ens160-bme280-qwiic.html |
|SparkFun Environmental Sensor - BME688 | temperature, humidity, & barometric pressure| https://www.sparkfun.com/sparkfun-environmental-sensor-bme688-qwiic.html | 
|-----------------------|-------|-------|
| SparkFun 6DoF IMU BMI270 | accelero, gyroscope | https://www.sparkfun.com/sparkfun-6dof-imu-breakout-bmi270-qwiic.html |
| Sensirion SEN55 | Particle, VOC, Humidity, and Temperature |https://www.sparkfun.com/sensirion-particle-voc-humidity-and-temperature-sensor-sen55.html|
|Sensirion Sensor  SPS30| PM | https://www.sparkfun.com/particulate-matter-sensor-sps30.html | 
|SparkFun Indoor AirQuality Sensor ENS160 | CO2-equivalents, TVOC, air quality indices (AQIs) | https://www.sparkfun.com/sparkfun-indoor-air-quality-sensor-ens160-qwiic.html |
|Sensiron SCD30 | CO2 | https://www.sparkfun.com/co-humidity-and-temperature-sensor-scd30.html https://www.sparkfun.com/co-humidity-and-temperature-sensor-scd30.html |https://github.com/Sensirion/arduino-i2c-scd30/blob/master/pinouts/esp32-devkitc.md) |

and many more - just ask us!

Light detection, Load Cells, Power / Voltage / Current - it s all there.





[Here](https://github.com/Xinyuan-LilyGO/LilyGo-LoRa-Series/blob/master/assets/image/t-beam_v1.1_pinmap.jpg) 
you can find a pinmap for our board (TTGO T-Beam V1.1). Connect the pins from the board to the sensor via the breadboard using the handed-out jumper cables.



If you are unsure how a breadboard works, [this article](https://wiring.org.co/learning/tutorials/breadboard/) explains it pretty well. Below how to connect the sensors are expanded on:

Using the jumper cables & the breadboard, you should connect the pins on your board and the pins on the SCD30 as follow:

| T-Beam                | Sensor |
|-----------------------|-------|
|21                     |RX/SDA |
|22                    |TX/SCL |

Using these resources, we can conclude that our setup should look something like this:

![pinout](images/scd_ttgo_pinout.png)

**Source of pinmaps:** https://blog.fh-kaernten.at/ingmarsretro/files/2021/04/anschluss-rotated.jpg && https://github.com/Xinyuan-LilyGO/LilyGo-LoRa-Series/blob/master/assets/image/t-beam_v1.1_pinmap.jpg?raw=true

Now we are ready to turn on the device and write some code!

#### Reading/programming the external sensor

To be able to communicate with the sensor, we need some sort of I2C bus. Curious about the I2C bus? [Here](https://learn.sparkfun.com/tutorials/i2c/all) you can find more information about it! :D
Also, here is a simple [I2C scanner](https://github.com/ITU-DASYALab/IoT_course/blob/main/guides/I2C_scanner.md) to show you what I2C devices there are connected on your board. 
Start by making a scan!

Also Useful for troubleshooting I2C!


**The challenge for you:** Try writing a simple program reading what your sensor senses. 

You should be able to read the sensor output, and then print it in the serial monitor. Good luck! :D 

**Tip!** The library has an example of how to use the sensor. You will find it under ... Examples :), in your Arduino IDE menu. This is a good starting point for understanding how to write your program.

Once you got it running, let us talk about what we are seeing and how to interprete it.

---

### Acknowledgements

The exercise is inspired by some of the previous TA's nice exercises from previous years:

https://github.com/FlapKap/IoT-CO2-sensor-exercise?tab=readme-ov-file

https://github.com/ITU-DASYALab/IoT_course/blob/main/exercises/archive_2022/exercise-03-sensors.md


**All links used in the exercise**

https://github.com/Sensirion/arduino-i2c-scd30

https://github.com/Sensirion/arduino-i2c-scd30/blob/master/pinouts/esp32-devkitc.md

https://github.com/Xinyuan-LilyGO/LilyGo-LoRa-Series/blob/master/assets/image/t-beam_v1.1_pinmap.jpg

https://wiring.org.co/learning/tutorials/breadboard/

https://learn.sparkfun.com/tutorials/i2c/all
