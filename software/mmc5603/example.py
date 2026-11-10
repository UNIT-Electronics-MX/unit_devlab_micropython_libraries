# Ejemplo para mmc5603.py (MMC5603, magnetometro de 3 ejes por I2C)
# Basado en main.py del proyecto original de Roman Shevchik (goctaprog)
# https://github.com/octaprog7/MMC5603 - Licencia MIT
import time
from machine import I2C, Pin

from mmc5603 import MMC5603, I2cAdapter

# Bus I2C interno de la placa: los sensores integrados (MMC5603, etc.) estan en GPIO2/GPIO3.
# El bus QWIIC usa GPIO1/GPIO6 y no se usa aqui.
I2C_SDA_PIN = 2
I2C_SCL_PIN = 3

i2c = I2C(0, sda=Pin(I2C_SDA_PIN), scl=Pin(I2C_SCL_PIN), freq=400_000)

sensor = MMC5603(I2cAdapter(i2c))
print(f"Sensor id: {hex(sensor.get_id())}")

# Medicion continua a 20 Hz
sensor.set_update_rate(20)
sensor.start_measure(continuous_mode=True, auto_set_reset=True)

while True:
    if sensor.is_data_ready():
        x, y, z = sensor.get_axis(-1)
        print(f"X: {x}; Y: {y}; Z: {z}")
    time.sleep_ms(100)
