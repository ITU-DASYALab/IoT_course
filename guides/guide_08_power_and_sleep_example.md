## Example sketch for trying sleep modes


Using the esp32 sleep lib ... but ... warning ... does it really go into deep sleep? measure!


```

int TIME_TO_SLEEP = 30;                        // Time ESP32 will go to sleep (in seconds)

unsigned long long uS_TO_S_FACTOR = 1000000;  // Conversion factor for microseconds to seconds

RTC_DATA_ATTR int bootCount = 0;              // Number of reboots

#define LED 4


void setup() {

  /****  Do your stuff here! ****/

  pinMode(LED, OUTPUT);

  Serial.begin(9600);                                 // Start serial communication at 115200 baud rate

  ++bootCount;                                          // Add 1 to the current value of bootCount

  Serial.println("Boot number: " + String(bootCount));  // print the value of bootCount on the serial monitor
   Serial.println("I am awake now! Yay!!!!! I might as well blink my LED");
   for (int i = 0; i <= 10; i++) {

        digitalWrite(LED, HIGH);
        Serial.println("off - round "+ String(i));
        delay(500); //delays are in ms
        digitalWrite(LED, LOW); 
        Serial.println("on - round " + String(i));
        delay(500);

      } 
      
 

  Serial.println("I have blunk .... I am getting tired ...."); 
  Serial.println("Going to sleep now");                 // Print when the ESP is about to go into deep sleep mode

  /* Now we wrap up for Deep Sleep - I hope you did everything you needed to... */

  esp_sleep_enable_timer_wakeup(TIME_TO_SLEEP * uS_TO_S_FACTOR);  // Set up timer as the wake up source and set sleep duration to 5 seconds

  Serial.flush();                                                 // Waits for the transmission of outgoing serial data to complete.

  esp_deep_sleep_start();                                         // Start the deep sleep mode

}

void loop() {

  // This is not going to be called

  }



```
`
