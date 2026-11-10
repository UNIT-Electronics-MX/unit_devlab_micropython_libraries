# MicroPython Driver for the Bosch BMI270 Accelerometer/Gyro Sensor

This project was initially written by [jposada202020](https://github.com/jposada202020/MicroPython_BMI270) and is licensed under the [MIT License](https://github.com/jposada202020/MicroPython_BMI270/blob/master/LICENSE).

I did only some minor changes to the examples to get it working on the [Infineon PSOC6 AI Eval Kit](https://www.infineon.com/cms/en/product/evaluation-boards/cy8ckit-062s2-ai/) using Infineon's [PSOC6 MicroPython port](https://github.com/Infineon/micropython).

## Installation

To install directly using a Wi-Fi capable board:

```python
import mip
mip.install("github:ederjc/micropython_bmi270")
```

Alternatively, use Thonny: copy the `bmi270.py` file to the board's file system (**File > Save copy...** and choose the MicroPython device). Then rename the example file on the board (for example, `example.py` to `main.py`) to run it when the board starts.

## Usage Example

```python
from machine import I2C, Pin
import bmi270

i2c = I2C(1, sda=Pin(2), scl=Pin(3))
sensor = bmi270.BMI270(i2c)
print(sensor.acceleration)
```

Take a look at the `example.py` and `bmi270_simpletest.py` files for complete examples.

## Documentation

API documentation for this library can be found on [Read the Docs](https://micropython-bmi270.readthedocs.io/en/latest/api.html).
