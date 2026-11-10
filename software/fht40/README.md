# MicroPython driver for the FHT40 Temperature and Humidity Sensor

This library provides a MicroPython driver for the FHT40 temperature and humidity sensor over I2C. The sensor uses the same command set and measurement format as the Sensirion SHT4x family.

> **Note**: This library is part of the [UNIT DevLab MicroPython Libraries Collection](../../README.md) - a curated compilation of useful MicroPython libraries.

## Files

- `fht40.py`: the complete library. It is the only file required.
- `example.py`: example that reads the temperature and the humidity every 2 seconds.

## Connection

- The FHT40 on this board is an **onboard** sensor. It is on I2C bus 0, with SDA on GPIO2 and SCL on GPIO3 (`I2C(0, sda=Pin(2), scl=Pin(3))`).
- The I2C address is fixed: `0x44`.

## Installation

Copy `fht40.py` to the board with Thonny (**File > Save copy...** and choose the MicroPython device). Then copy `example.py` to the board and rename it (for example, to `main.py`) so it runs on boot.

## Basic Usage

```python
from machine import I2C, Pin
from fht40 import FHT40

i2c = I2C(0, sda=Pin(2), scl=Pin(3), freq=400_000)
sensor = FHT40(i2c)

sensor.measure()
print(sensor.temperature)   # degrees Celsius
print(sensor.humidity)      # relative humidity, %
```

## Main Methods

- `measure()`: starts a high-repeatability measurement, checks the CRC of both values and stores them. Takes about 10 ms.
- `temperature`: temperature in °C from the last `measure()` call.
- `humidity`: relative humidity in % from the last `measure()` call.
- `soft_reset()`: resets the sensor.

## Notes

- The conversion formulas and the CRC-8 check are the ones used by the Sensirion SHT4x family. The command set and the 0x44 address were taken from the FHT40 product specification. Check them against the vendor's current document if your sensor behaves differently.
