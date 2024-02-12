# Exercise week 03
## Hello Sensors! - Simple sensor programs

### Goal for the day

  * Familiarize yourself with the connections of a LilyGo-board
  * Read the internal temperature sensor
  * Connect a CO2-sensor to the board
  * Read and understand the output of the sensor

### Reading the internal temperature sensor

The goal of this exercise is to be able to make some measurements of the environment. However, to get an understanding of how to read some sensor input, we can start by reading the temperature of the core on our board. Every ESP32 has an internal temperature sensor - not very useful for measuring the temperature in the surrounding environment, but useful for getting an understanding of the core's current temperature (which is useful in many development scenarios). Let's try and get some data from this sensor!

[This](https://circuits4you.com/2019/01/01/esp32-internal-temperature-sensor-example/#google_vignette) tutorial explains how to make use of this internal temperature sensor. I have boiled it down to a more readable and suitable (for our setup) below:

    extern "C" {
      uint8_t temprature_sens_read();
    }

    uint8_t temprature_sens_read();

    void setup() {
      Serial.begin(115200);
    }

    void loop() {
      Serial.print("Temperature: ");
    
      // Convert raw temperature in F to Celsius degrees
      Serial.print((temprature_sens_read() - 32) / 1.8);
      Serial.println(" C");
      delay(1000);
    }

    // Source: https://circuits4you.com/2019/01/01/esp32-internal-temperature-sensor-example/#google_vignette

This program is quite straightforward and similar to what we did last week. However, a new element is introduced:

    extern "C" {
      uint8_t temprature_sens_read();
    }

What this simply does is define a method to read the internal temperature, which is found on the uint8_t. However, as we are writing a type of C++ code, we need to use the method surrounding it to be able to read it. [Here](https://techexplorations.com/guides/arduino/programming/_t-in-uint8_t/) you can read more about this.

You should now be able to read your internal temperature in the serial monitor!

### Connecting and reading an external temperature Sensor

**Note before we start:** Remember when working with physical computing, there is always a risk of things going wrong and breaking, different from software.
Therefore, double-check you use the correct pins and make sure that your cables are away from the battery before even starting the device - just to be on the sure side ;)

#### Connecting the external sensor

Before we start writing code, let's connect the sensor to our board.

We use the Sensiron SCD30 sensor.
[Here](https://github.com/Sensirion/arduino-i2c-scd30/blob/master/pinouts/esp32-devkitc.md) you can find a pinout for the SCD30 sensor, and [here](https://github.com/Xinyuan-LilyGO/LilyGo-LoRa-Series/blob/master/assets/image/t-beam_v1.1_pinmap.jpg) you can find a pinmap for our board (TTGO T-Beam V1.1). Connect the pins from the board to the sensor via the breadboard using the handed-out jumper cables.
If you are unsure how a breadboard works, [this article](https://wiring.org.co/learning/tutorials/breadboard/) explains it pretty well.

Now we are ready to turn on the device and write some code!

#### Reading/programming the external sensor

To be able to communicate with the sensor, we need some sort of I2C bus. Curious about the I2C bus? [Here](https://learn.sparkfun.com/tutorials/i2c/all) you can find more information about it! :D
The simplest way to get an I2C bus for our sensor is to download it using the library manager in the Arduino IDE.
Search for "Sensirion I2C SCD30", and when asked for download dependencies, answer yes.
With both your board connected to the sensor, as well as the I2C library downloaded, you are ready to read some temperatures.

**The challenge for you:** Try writing a simple program reading what your sensor senses. You should be able to read the CO2 concentration, temperature, and humidity, and then print them in the serial monitor. Good luck! :D 

**Tip!** The library has an example of how to use the sensor. This is a good starting point for understanding how to write your program.



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