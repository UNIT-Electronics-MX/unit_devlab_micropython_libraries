import machine
from ssd1306 import SSD1306_I2C

I2C_SDA_PIN = 6
I2C_SCL_PIN = 7

i2c = machine.SoftI2C(sda=machine.Pin(I2C_SDA_PIN), scl=machine.Pin(I2C_SCL_PIN))

oled = SSD1306_I2C(128, 32, i2c)

oled.fill(1)
oled.show()

oled.fill(0)
oled.show()
oled.text('UNIT', 50, 10)
oled.text('ELECTRONICS', 25, 20)

oled.show()