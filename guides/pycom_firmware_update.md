
## Update pycom firmware 

last check: 20220126

### lopy

https://docs.pycom.io/updatefirmware/device/
https://software.pycom.io/downloads/linux-1.16.5.html
https://software.pycom.io/downloads/LoPy.html

e.g. on linux:

pycom-fwtool-cli  -v -p /dev/ttyACM0 flash -t ./LoPy-1.20.3.b0.tar.gz 

### expansion board

https://docs.pycom.io/updatefirmware/expansionboard/

e.g. on linux:

dfu-util -D expansion31_0.0.11.dfu 

