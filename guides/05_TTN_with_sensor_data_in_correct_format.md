## Example of complete code for ESP32 T-Beam

NOTE: there are device specifc settings!!! circa line 65 ...

```
/*******************************************************************************
 * Copyright (c) 2015 Thomas Telkamp and Matthijs Kooijman
 * Copyright (c) 2018 Terry Moore, MCCI
 *
 * Permission is hereby granted, free of charge, to anyone
 * obtaining a copy of this document and accompanying files,
 * to do whatever they want with them without any restriction,
 * including, but not limited to, copying, modification and redistribution.
 * NO WARRANTY OF ANY KIND IS PROVIDED.
 *
 * This example sends a valid LoRaWAN packet with payload "Hello,
 * world!", using frequency and encryption settings matching those of
 * the The Things Network.
 *
 * This uses OTAA (Over-the-air activation), where where a DevEUI and
 * application key is configured, which are used in an over-the-air
 * activation procedure where a DevAddr and session keys are
 * assigned/generated for use with all further communication.
 *
 * Note: LoRaWAN per sub-band duty-cycle limitation is enforced (1% in
 * g1, 0.1% in g2), but not the TTN fair usage policy (which is probably
 * violated by this sketch when left running for longer)!

 * To use this sketch, first register your application and device with
 * the things network, to set or generate an AppEUI, DevEUI and AppKey.
 * Multiple devices can use the same AppEUI, but each device has its own
 * DevEUI and AppKey.
 *
 * Do not forget to define the radio type correctly in
 * arduino-lmic/project_config/lmic_project_config.h or from your BOARDS.txt.
 *
 *******************************************************************************/
//sensor stuff
#include <Wire.h>
#include "SparkFunBME280.h"
#include "SparkFun_ENS160.h"
// sensors
BME280 mySensor;
SparkFun_ENS160 myENS;

#include <lmic.h>
#include <hal/hal.h>
#include <SPI.h>

//
// For normal use, we require that you edit the sketch to replace FILLMEIN
// with values assigned by the TTN console. However, for regression tests,
// we want to be able to compile these scripts. The regression tests define
// COMPILE_REGRESSION_TEST, and in that case we define FILLMEIN to a non-
// working but innocuous value.
//
#ifdef COMPILE_REGRESSION_TEST
# define FILLMEIN 0
#else
# warning "You must replace the values marked FILLMEIN with real values from the TTN control panel!"
# define FILLMEIN (#dont edit this, edit the lines that use FILLMEIN)
#endif

// This EUI must be in little-endian format, so least-significant-byte
// first. When copying an EUI from ttnctl output, this means to reverse
// the bytes. For TTN issued EUIs the last bytes should be 0xD5, 0xB3,
// 0x70.
static const u1_t PROGMEM APPEUI[8]={ 0x05, 0x25, 0x20, 0xBE, 0xBA, 0xEE, 0xFF, 0xCA };
void os_getArtEui (u1_t* buf) { memcpy_P(buf, APPEUI, 8);}

// This should also be in little endian format, see above.
static const u1_t PROGMEM DEVEUI[8]={ 0x94, 0xDF, 0x5C, 0xFE, 0xFF, 0xDA, 0xD4, 0xD4 };
void os_getDevEui (u1_t* buf) { memcpy_P(buf, DEVEUI, 8);}

// This key should be in big endian format (or, since it is not really a
// number but a block of memory, endianness does not really apply). In
// practice, a key taken from ttnctl can be copied as-is.
static const u1_t PROGMEM APPKEY[16] = { 0xA4, 0xB4, 0x4F, 0x33, 0x0E, 0x43, 0xD1, 0x80, 0x40, 0x57, 0x06, 0xAD, 0x6A, 0x93, 0x6D, 0x03 };
void os_getDevKey (u1_t* buf) {  memcpy_P(buf, APPKEY, 16);}


static osjob_t sendjob;


    
    // Schedule TX every this many seconds (might become longer due to duty
// cycle limitations).
const unsigned TX_INTERVAL = 300;  //orig was 120, but at 0.06 s airtime, we should do max 500 msgs/day, 20 msgs/h

// Pin mapping


const lmic_pinmap lmic_pins = {
  .nss = 18,
  .rxtx = LMIC_UNUSED_PIN,
  .rst = 23, // was "14,"
  .dio = {26, 33, 32},
};

void printHex2(unsigned v) {
    v &= 0xff;
    if (v < 16)
        Serial.print('0');
    Serial.print(v, HEX);
}

void onEvent (ev_t ev) {
    Serial.print(os_getTime());
    Serial.print(": ");
    switch(ev) {
        case EV_SCAN_TIMEOUT:
            Serial.println(F("EV_SCAN_TIMEOUT"));
            break;
        case EV_BEACON_FOUND:
            Serial.println(F("EV_BEACON_FOUND"));
            break;
        case EV_BEACON_MISSED:
            Serial.println(F("EV_BEACON_MISSED"));
            break;
        case EV_BEACON_TRACKED:
            Serial.println(F("EV_BEACON_TRACKED"));
            break;
        case EV_JOINING:
            Serial.println(F("EV_JOINING"));
            break;
        case EV_JOINED:
            Serial.println(F("EV_JOINED"));
            {
              u4_t netid = 0;
              devaddr_t devaddr = 0;
              u1_t nwkKey[16];
              u1_t artKey[16];
              LMIC_getSessionKeys(&netid, &devaddr, nwkKey, artKey);
              Serial.print("netid: ");
              Serial.println(netid, DEC);
              Serial.print("devaddr: ");
              Serial.println(devaddr, HEX);
              Serial.print("AppSKey: ");
              for (size_t i=0; i<sizeof(artKey); ++i) {
                if (i != 0)
                  Serial.print("-");
                printHex2(artKey[i]);
              }
              Serial.println("");
              Serial.print("NwkSKey: ");
              for (size_t i=0; i<sizeof(nwkKey); ++i) {
                      if (i != 0)
                              Serial.print("-");
                      printHex2(nwkKey[i]);
              }
              Serial.println();
            }
            // Disable link check validation (automatically enabled
            // during join, but because slow data rates change max TX
	    // size, we don't use it in this example.
            LMIC_setLinkCheckMode(0);
            break;
        /*
        || This event is defined but not used in the code. No
        || point in wasting codespace on it.
        ||
        || case EV_RFU1:
        ||     Serial.println(F("EV_RFU1"));
        ||     break;
        */
        case EV_JOIN_FAILED:
            Serial.println(F("EV_JOIN_FAILED"));
            break;
        case EV_REJOIN_FAILED:
            Serial.println(F("EV_REJOIN_FAILED"));
            break;
        case EV_TXCOMPLETE:
            Serial.println(F("EV_TXCOMPLETE (includes waiting for RX windows)"));
            if (LMIC.txrxFlags & TXRX_ACK)
              Serial.println(F("Received ack"));
            if (LMIC.dataLen) {
              Serial.print(F("Received "));
              Serial.print(LMIC.dataLen);
              Serial.println(F(" bytes of payload"));
            }
            // Schedule next transmission
            os_setTimedCallback(&sendjob, os_getTime()+sec2osticks(TX_INTERVAL), do_send);
            break;
        case EV_LOST_TSYNC:
            Serial.println(F("EV_LOST_TSYNC"));
            break;
        case EV_RESET:
            Serial.println(F("EV_RESET"));
            break;
        case EV_RXCOMPLETE:
            // data received in ping slot
            Serial.println(F("EV_RXCOMPLETE"));
            break;
        case EV_LINK_DEAD:
            Serial.println(F("EV_LINK_DEAD"));
            break;
        case EV_LINK_ALIVE:
            Serial.println(F("EV_LINK_ALIVE"));
            break;
        /*
        || This event is defined but not used in the code. No
        || point in wasting codespace on it.
        ||
        || case EV_SCAN_FOUND:
        ||    Serial.println(F("EV_SCAN_FOUND"));
        ||    break;
        */
        case EV_TXSTART:
            Serial.println(F("EV_TXSTART"));



            break;
        case EV_TXCANCELED:
            Serial.println(F("EV_TXCANCELED"));
            break;
        case EV_RXSTART:
            /* do not print anything -- it wrecks timing */
            break;
        case EV_JOIN_TXCOMPLETE:
            Serial.println(F("EV_JOIN_TXCOMPLETE: no JoinAccept"));
            break;

        default:
            Serial.print(F("Unknown event: "));
            Serial.println((unsigned) ev);
            break;
    }
}

void do_send(osjob_t* j){

  // Read BME280 values
            Serial.print("Humidity: ");
            Serial.print(mySensor.readFloatHumidity(), 0);
            Serial.print("% ");
    
            Serial.print("Pressure: ");
            Serial.print(mySensor.readFloatPressure(), 0);
            Serial.print(" Pa ");

    
            Serial.print("Altitude: ");
            Serial.print(mySensor.readFloatAltitudeMeters(), 1);
            Serial.print(" m ");
    
            Serial.print("Temp: ");
            Serial.print(mySensor.readTempC(), 2);
            Serial.println(" C");

            Serial.print("Total Volatile Organic Compounds: ");
            Serial.print(myENS.getTVOC());
            Serial.println(" ppb");

            Serial.print("CO2 concentration: ");
            Serial.print(myENS.getECO2());
            Serial.println(" ppm");
/*
  byte senddata[] = {
  (uint8_t)(round(mySensor.readFloatHumidity())),
  highByte(int(mySensor.readFloatPressure()/100)),
    lowByte(int(mySensor.readFloatPressure()/100)),
  (uint8_t)(round(mySensor.readFloatAltitudeMeters()/1000)),
    (uint8_t)(round(mySensor.readFloatAltitudeMeters()/1000)),
  (uint8_t)(round(mySensor.readTempC())),
    (uint8_t)(round(myENS.getTVOC())),
      (uint8_t)(round(myENS.getECO2())),
            (uint8_t)(round(myENS.getECO2()))
  };
  */

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

  Serial.print("senddata element by element = ");
   for   (int i=0; i<sizeof(senddata)-1; ++i) {
                  Serial.print(i);Serial.print(": ");Serial.print(senddata[i]);Serial.println(" ");
              }
                                                                                                                                                                                             
    // Check if there is not a current TX/RX job running
    if (LMIC.opmode & OP_TXRXPEND) {
        Serial.println(F("OP_TXRXPEND, not sending"));
    } else {
        // Prepare upstream data transmission at the next possible time.
        LMIC_setTxData2(1, senddata, sizeof(senddata)-1, 0);
        Serial.println(F("Packet queued"));
    }
    // Next TX is scheduled after TX_COMPLETE event.
}

void setup() {

    Serial.begin(9600);

/////////////////////////////////////////////////// sensors
Serial.println("Initializing Sensors...");
    
    Wire.begin();
    
    // Initialize BME280
    if (mySensor.beginI2C() == false)
    {
        Serial.println("BME280 not responding. Check wiring.");
        while (1);
    }
    Serial.println("BME280 initialized.");

    // Initialize ENS160
    if (!myENS.begin())
    {
        Serial.println("ENS160 not responding. Check wiring.");
        while (1);
    }
    Serial.println("ENS160 initialized.");
    
    myENS.setOperatingMode(SFE_ENS160_STANDARD);
    Serial.print("Gas Sensor Status Flag (0 - Standard, 1 - Warm up, 2 - Initial Start Up): ");
    Serial.println(myENS.getFlags());
//////////////////// EO sensors


    Serial.println(F("Starting LMIC/TTN"));

    #ifdef VCC_ENABLE
    // For Pinoccio Scout boards
    pinMode(VCC_ENABLE, OUTPUT);
    digitalWrite(VCC_ENABLE, HIGH);
    delay(1000);
    #endif

    // LMIC init
    os_init();
    // Reset the MAC state. Session and pending data transfers will be discarded.
    LMIC_reset();

    // Start job (sending automatically starts OTAA too)
    do_send(&sendjob);
}

void loop() {


    os_runloop_once();
}

``
