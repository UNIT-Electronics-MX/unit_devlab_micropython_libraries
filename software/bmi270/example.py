# Library: bmi270.py
# Description: Reads the acceleration (m/s2) and the gyroscope (deg/s) of the BMI270 every 0.5 s. Uses SoftI2C on GPIO6/GPIO7 and address 0x69.
# Suggested file name on the board: main.py

import machine
import time
from bmi270 import BMI270

I2C_SDA_PIN = 6
I2C_SCL_PIN = 7

i2c = machine.SoftI2C(sda=machine.Pin(I2C_SDA_PIN), scl=machine.Pin(I2C_SCL_PIN))

imu = BMI270(i2c, 0x69)

while True:
    accx, accy, accz = imu.acceleration
    print("x:{:.2f} y:{:.2f} z:{:.2f} m/s2".format(accx, accy, accz))
    time.sleep(0.5)

    gyrox, gyroy, gyroz = imu.gyro
    print("x:{:.2f} y:{:.2f} z:{:.2f} deg/s".format(gyrox, gyroy, gyroz))
    time.sleep(0.5)
