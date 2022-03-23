
from mpu6050 import MPU
from machine import I2C, Pin
import time

i2c = I2C(2)

sensor=MPU(i2c,0x68)

while True:
    (AccelX,AccelY,AccelZ,TEMP,girX,girY,girZ)=sensor.get_values()
    print("AccelX:",AccelX)
    print("AccelY",AccelY)
    print("AccelZ",AccelZ)
    print("Temp",TEMP)
    print("GirX",girX)
    print("GirY",girY)
    print("GirZ",girZ)
    time.sleep (2)