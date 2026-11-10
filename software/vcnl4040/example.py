import time
from machine import I2C, Pin

from vcnl4040 import VCNL4040

# Bus I2C interno de la placa: el VCNL4040 esta en GPIO2/GPIO3.
I2C_SDA_PIN = 2
I2C_SCL_PIN = 3

i2c = I2C(0, sda=Pin(I2C_SDA_PIN), scl=Pin(I2C_SCL_PIN), freq=400_000)

sensor = VCNL4040(i2c)
sensor.light_integration_time = VCNL4040.ALS_640MS

while True:
    print("Proximity: {}".format(sensor.proximity))
    print("Ambient light (lux): {:.2f}".format(sensor.lux))
    print(16 * "_")
    time.sleep(0.5)
