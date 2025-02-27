

## first lecture

lecture - #OK

exercise - logistics, overview, 
  * ILOs
  * exams
  * balloon idea, context with other courses (how to ..)
    * mail Mads, contact  
  * LLMs



## week 2:

intro to boards - https://github.com/ITU-DASYALab/IoT_course/blob/main/exercises/IoT2024_exercise_02.md

check this: https://github.com/ITU-DASYALab/IoT_course/blob/main/guides/lilyGo_hello_world.md


hand out kits - if boxes arrive

kit:
t-beam
usb micro
see old kit: https://github.com/ITU-DASYALab/IoT_course/blob/main/kit/kits.md

Library link: https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json


## Week 5: 

If you care to know your MAC Address, run this sketch first: 

#include "WiFi.h"
#include "esp_wifi.h"

void setup() {
    Serial.begin(115200);
    WiFi.begin();
    Serial.print("MAC Address: ");
    Serial.println(WiFi.macAddress());
}

void loop() {
  Serial.println("MAC: ");
  Serial.println(WiFi.macAddress());
  delay(1000);
}
