# Getting Started with the LoPy

## General documentation for pycom devices, micropython etc

https://docs.pycom.io

## Prepare your Software

For programming the LoPy, we will be using **MicroPython**, 
with the PyMakr plugin for Atom https://atom.io/ or VS Code https://code.visualstudio.com/.
Our recommendation is VS Code.
There are other possibilities, too,
such as rshell https://pypi.org/project/rshell/ or mpfshell https://github.com/wendlers/mpfshell -

but start by

- installing VS Code (if you don't have it)
- installing the pymakr plugin - https://docs.pycom.io/gettingstarted/software/vscode/

(update:  it seems there s problems with vscode 1.53 ... for now, we have to stick to 1.52)

## Hardware / Parts

To get started, you will need these parts:

 - a LoPy4 - https://docs.pycom.io/datasheets/development/lopy4/
 - an Expansion Board, to provide a USB micro port, connectivity to your computer - https://docs.pycom.io/datasheets/expansionboards/expansion3/
 - an Antenna kit / Antenna and "pigtail" (cable) - for use with LoRa - https://docs.pycom.io/tutorials/networks/lora/
	For Wi-Fi, there is an on-board antenna by default, so no external antenna is needed to get started.
 - a micro USB cable

 ### Remarks on hardware

 - Never run a radio chip (such as a LoRa radio) without an antenna or terminator on its output! the reflected wave might damage the chip. Wi-Fi has an on-board antenna by default, so no external antenna is needed to get started
 - Keep an eye on those little black jumpers on the expansion board! if they come off (and they do!), things will not work.
 - Dont push the micro USB connector too hard - this part of the board loves to break.
 - Carefully check the orientation of the LoPy board relative to the Expansion Board - different versions of the LoPy board have the print turning different ways! Check pin alignment!



When both software and hardware are in place:

### Connecting to the LoPY

In general, pycoms guide is pretty good. 

https://docs.pycom.io/gettingstarted/
https://docs.pycom.io/tutorials/basic/ 

We add a few remarks.

##### Serial connection through USB micro

Serial connection via USB cable is our preferred choice - rather than WiFi.

##### Hello World, LEDs and other initial fun

 - Try the interactive prompt (the REPL) -

 Note: here s some useful shortcuts for interacting with the MicroPython REPL:

  ```
    Ctrl-A on a blank line will enter raw REPL mode.
            This is similar to permanent paste mode, except that characters are not echoed back.
    Ctrl-B on a blank like goes to normal REPL mode.
    Ctrl-C cancels any input, or interrupts the currently running code.
    Ctrl-D on a blank line will do a soft reset.
    Ctrl-E enters ‘paste mode’ that allows you to copy and paste chunks of text. Exit this mode using Ctrl-D.
  ```
 Now, let s say "hello world":

 ```
 >>> print('hello world!')
  ```

  - Stop WiFi AP - per default, the LoPys start running a WiFi Access Point - that is a bad idea in many ways (in what ways?)
  This is how you stop it:

  ```
from network import WLAN
wlan = WLAN() # we call the constructor without params
# turn off Wifi
wlan.deinit()
print('Turned off WiFi')
 ```

 If you really need a WiFi AP for short periods of time - this is how you start it

  ```
 from network import WLAN
wlan.init(mode=WLAN.AP, ssid='aTemporarySSID', auth=(WLAN.WPA2,'yourPassword'), channel=7, antenna=WLAN.INT_ANT)
 ```

 From the pycom API examples, 
find the LED example and make the LED blink -
https://docs.pycom.io/tutorials/basic/rgbled/

You should now be familiar with the basics of LoPy and pymakr -
and ready to take on more challenging code examples, such as sensors and networking.

