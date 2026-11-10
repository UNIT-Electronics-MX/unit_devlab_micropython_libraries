# Library: fht40.py
# Description: Reads the temperature (C) and the relative humidity (%) of the FHT40 every 2 s. Uses the onboard I2C bus on GPIO2/GPIO3.
# Suggested file name on the board: main.py

import time
from machine import I2C, Pin

from fht40 import FHT40

# Bus I2C interno de la placa: el FHT40 esta en GPIO2/GPIO3.
I2C_SDA_PIN = 2
I2C_SCL_PIN = 3

i2c = I2C(0, sda=Pin(I2C_SDA_PIN), scl=Pin(I2C_SCL_PIN), freq=400_000)

sensor = FHT40(i2c)

while True:
    sensor.measure()
    print("Temperature (C): {:.2f}".format(sensor.temperature))
    print("Humidity (%): {:.2f}".format(sensor.humidity))
    print(16 * "_")
    time.sleep(2)
