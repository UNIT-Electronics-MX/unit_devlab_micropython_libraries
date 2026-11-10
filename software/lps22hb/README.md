# MicroPython driver for the LPS22HB Pressure Sensor

This library provides a MicroPython driver for the STMicroelectronics LPS22HB absolute pressure sensor (barometer) over I2C. It reports pressure in hPa and temperature in °C.

> **Note**: This library is part of the [UNIT DevLab MicroPython Libraries Collection](../../README.md) - a curated compilation of useful MicroPython libraries.

## Files

- `lps22hb.py`: the complete library. It is the only file required.
- `example.py`: example that reads the pressure and the temperature every 2 seconds.

## Connection

- The LPS22 on this board is an **onboard** sensor. It is on I2C bus 0, with SDA on GPIO2 and SCL on GPIO3 (`I2C(0, sda=Pin(2), scl=Pin(3))`).
- The I2C address is `0x5C` (SA0 low). If your board ties SA0 high, use `0x5D`.

## Installation

Copy `lps22hb.py` to the board with Thonny (**File > Save copy...** and choose the MicroPython device). Then copy `example.py` to the board and rename it (for example, to `main.py`) so it runs on boot.

## Basic Usage

```python
from machine import I2C, Pin
from lps22hb import LPS22HB

i2c = I2C(0, sda=Pin(2), scl=Pin(3), freq=400_000)
sensor = LPS22HB(i2c)

print(sensor.pressure)      # hPa
print(sensor.temperature)   # degrees Celsius
```

## Main Methods

- `pressure`: pressure in hPa.
- `temperature`: temperature in °C.
- `soft_reset()`: resets the sensor registers to their defaults.

The sensor is configured at construction time for continuous measurement at 1 Hz with block data update enabled.

## Notes

- The register map and the WHO_AM_I value (0xB1) follow the LPS22HB datasheet. The scale factors (4096 LSB/hPa for pressure, 100 LSB/°C for temperature) should be checked against the datasheet if your readings look wrong.
