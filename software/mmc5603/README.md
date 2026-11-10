# MicroPython driver for the MMC5603 Geomagnetic Sensor

This library provides a MicroPython driver for the MEMSIC MMC5603 3-axis geomagnetic (magnetometer) sensor over I2C.

> **Note**: This library is part of the [UNIT DevLab MicroPython Libraries Collection](../../README.md) - a curated compilation of useful MicroPython libraries.

## Credits and License

This driver is based on the original project by **Roman Shevchik (goctaprog)**:
https://github.com/octaprog7/MMC5603

The code is distributed under the **MIT License**. The full license text and copyright notice are at the top of `mmc5603.py`.

## Files

- `mmc5603.py`: the complete library. It is the only file required.
- `example.py`: example of continuous measurement of the three axes.

## Connection

- The MMC5603 is an **onboard** sensor. It is on I2C bus 0, with SDA on GPIO2 and SCL on GPIO3 (`I2C(0, sda=Pin(2), scl=Pin(3))`). The QWIIC bus (GPIO1/GPIO6) is not used for this sensor.
- The sensor operates at 3.3 V (1.62 V to 3.6 V).
- The I2C address is fixed: `0x30`.

## Installation

Copy `mmc5603.py` to the board with Thonny (**File > Save copy...** and choose the MicroPython device). Then copy `example.py` to the board and rename it (for example, to `main.py`) so it runs on boot.

## Basic Usage

```python
from machine import I2C, Pin
from mmc5603 import MMC5603, I2cAdapter

i2c = I2C(0, sda=Pin(2), scl=Pin(3), freq=400_000)
sensor = MMC5603(I2cAdapter(i2c))

sensor.set_update_rate(20)
sensor.start_measure(continuous_mode=True, auto_set_reset=True)

if sensor.is_data_ready():
    print(sensor.get_axis(-1))   # (X, Y, Z) in raw units
```

## Main Methods

- `get_id()`: returns the chip ID (0x10).
- `set_update_rate(hz)`: output data rate, 1 to 255 Hz (1000 Hz with `hi_power`).
- `start_measure(continuous_mode, auto_set_reset)`: starts the measurement.
- `is_data_ready()`: returns whether new data is available.
- `get_axis(-1)`: returns the three magnetic field components. Use `get_axis(0)`, `(1)` or `(2)` for a single axis.
- `get_temperature()`: sensor temperature in °C.
- `perform_self_test()`: runs the sensor self-test.
- `soft_reset()`: resets the sensor. Wait about 20 ms before using it again (`time.sleep_ms(20)`).

## Original Project

For the full project, including the module, `sensor_pack` and `main.py`, see https://github.com/octaprog7/MMC5603.
