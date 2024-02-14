Here is a little I2C scanner that works on a TTGO T-Beam,
courtesy of [Nick Gammon 2011](http://www.gammon.com.au/i2c)

It has one dependency, the "Wire" library.

For our current course boards

Scanning a regular T-Beam with Sensirion SCD30 connected, i get
```
11:28:50.454 -> I2C scanner. Scanning ...
11:28:50.454 -> Found address: 52 (0x34) // GPS
11:28:50.554 -> Found address: 60 (0x3C) // Sensirion SCD30
```

Scanning I2C on a T-Beam with LED screen and Sensirion SCD30 connected, i get
```
11:19:03.208 -> I2C scanner. Scanning ...
11:19:03.208 -> Found address: 52 (0x34) // GPS
11:19:03.274 -> Found address: 60 (0x3C) // Screen
11:19:03.407 -> Found address: 97 (0x61) // Sensirion SCD30
11:19:03.507 -> Done.
11:19:03.507 -> Found 3 device(s).
```

Here s the code:

```
// I2C Tester
// Written by Nick Gammon
// Date: 20th April 2011

#include <Wire.h>

void setup() {
  Serial.begin (115200);
   Serial.println ("I2C scanner");
  Wire.begin(21,22);  // for T-Beam pass 21 (SCL) and 22 (SDA) GPIO pins
  
}  // end of setup

void loop() {

  Serial.println ();
  Serial.println ("I2C scanner. Scanning ...");
  byte count = 0;

  // Wire.begin(21,22);  
  for (byte i = 8; i < 120; i++)
  {
    Wire.beginTransmission (i);
    if (Wire.endTransmission () == 0)
      {
      Serial.print ("Found address: ");
      Serial.print (i, DEC);
      Serial.print (" (0x");
      Serial.print (i, HEX);
      Serial.println (")");
      count++;
      delay (100);  // maybe unneeded?
      } // end of good response
  } // end of for loop
  Serial.println ("Done.");
  Serial.print ("Found ");
  Serial.print (count, DEC);
  Serial.println (" device(s).");
  
  delay (30000); // wait 30 secs to scan again
  
  
  }

```
