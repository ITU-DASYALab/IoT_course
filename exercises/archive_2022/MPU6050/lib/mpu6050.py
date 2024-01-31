#https://micronote.tech/2020/07/I2C-Bus-with-a-NodeMCU-and-MicroPython/
#https://github.com/adamjezek98/MPU6050-ESP8266-MicroPython/blob/master/mpu6050.py
class MPU():
    def __init__(self, i2c, addr):
        self.i2c = i2c
        self.addr = addr
        self.i2c.writeto_mem(self.addr, 0x6B, bytes([0]))

    def combine_register_values(self,h,l):
        if not h & 0x80:
            return h << 8 | l
        return -((h ^ 255) << 8) |  (l ^ 255) + 1


    def get_values(self):
        a = self.i2c.readfrom_mem(self.addr, 0x3B, 14)
        AcX = self.combine_register_values(a[1],a[0])
        AcY = self.combine_register_values(a[3],a[2])
        AcZ= self.combine_register_values(a[5],a[4])
        Tmp = self.combine_register_values(a[7],a[6]) / 340.00 + 36.53
        GyX = self.combine_register_values(a[9],a[8])
        GyY = self.combine_register_values(a[11],a[10])
        GyZ = self.combine_register_values(a[13],a[12])
        return (AcX,AcY,AcZ,Tmp,GyX,GyY,GyZ)
