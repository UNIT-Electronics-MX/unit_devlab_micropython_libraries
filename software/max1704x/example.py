# Library: max1704x.py
# Description: Reads the cell voltage and the state of charge of the MAX17048 every 2 s. Uses the onboard I2C bus on GPIO2/GPIO3.
# Suggested file name on the board: main.py

import time
from machine import I2C, Pin

from max1704x import max1704x

# Bus I2C interno de la placa: el MAX17048 esta en GPIO2/GPIO3.
I2C_SDA_PIN = 2
I2C_SCL_PIN = 3

i2c = I2C(0, sda=Pin(I2C_SDA_PIN), scl=Pin(I2C_SCL_PIN), freq=400_000)

battery = max1704x(i2c, is_max17048=True)
print("I2C address: 0x{:02X}".format(battery.address()))
print("Version: 0x{:04X}".format(battery.getVersion()))

while True:
    print("Cell voltage (V): {:.3f}".format(battery.getVCell()))
    print("State of charge (%): {:.1f}".format(battery.getSoc()))
    print(16 * "_")
    time.sleep(2)
