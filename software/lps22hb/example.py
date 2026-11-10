import time
from machine import I2C, Pin

from lps22hb import LPS22HB

# Bus I2C interno de la placa: el LPS22 esta en GPIO2/GPIO3.
I2C_SDA_PIN = 2
I2C_SCL_PIN = 3

i2c = I2C(0, sda=Pin(I2C_SDA_PIN), scl=Pin(I2C_SCL_PIN), freq=400_000)

sensor = LPS22HB(i2c)

while True:
    print("Pressure (hPa): {:.2f}".format(sensor.pressure))
    print("Temperature (C): {:.2f}".format(sensor.temperature))
    print(16 * "_")
    time.sleep(2)
