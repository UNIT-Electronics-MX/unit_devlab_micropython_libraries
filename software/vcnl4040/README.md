# MicroPython driver for the VCNL4040 Proximity and Ambient Light Sensor

This library provides a MicroPython driver for the Vishay VCNL4040 proximity and ambient light sensor over I2C. It reports the proximity value, the ambient light in lux, and the white channel, and it supports the proximity and light interrupts.

> **Note**: This library is part of the [UNIT DevLab MicroPython Libraries Collection](../../README.md) - a curated compilation of useful MicroPython libraries.

## Credits and License

This driver is a MicroPython port of the CircuitPython library
[`adafruit_vcnl4040`](https://github.com/adafruit/Adafruit_CircuitPython_VCNL4040)
by **Kattni Rembor for Adafruit Industries**, distributed under the **MIT License**.
The SPDX license header is at the top of `vcnl4040.py`.

## Files

- `vcnl4040.py`: the complete library. It is the only file required.
- `example.py`: example that prints the proximity and the ambient light every 0.5 seconds.

## Connection

- The VCNL4040 on this board is an **onboard** sensor. It is on I2C bus 0, with SDA on GPIO2 and SCL on GPIO3 (`I2C(0, sda=Pin(2), scl=Pin(3))`).
- The I2C address is fixed: `0x60`.

## Installation

Copy `vcnl4040.py` to the board with Thonny (**File > Save copy...** and choose the MicroPython device). Then copy `example.py` to the board and rename it (for example, to `main.py`) so it runs on boot.

## Basic Usage

```python
from machine import I2C, Pin
from vcnl4040 import VCNL4040

i2c = I2C(0, sda=Pin(2), scl=Pin(3), freq=400_000)
sensor = VCNL4040(i2c)

sensor.light_integration_time = VCNL4040.ALS_640MS
print(sensor.proximity)   # raw proximity value
print(sensor.lux)         # ambient light in lux
```

## Main Properties and Methods

- `proximity`: raw proximity value.
- `lux`: ambient light in lux. `light` gives the raw value.
- `white`: white channel, scaled like `lux`.
- `light_integration_time`: `ALS_80MS`, `ALS_160MS`, `ALS_320MS` or `ALS_640MS`. Setting it waits for the sensor to settle.
- `proximity_integration_time`, `led_current`, `led_duty_cycle`, `proximity_bits`: sensor configuration, with the constants defined in the class.
- `proximity_low_threshold`, `proximity_high_threshold`, `light_low_threshold`, `light_high_threshold`: interrupt thresholds.
- `proximity_high_interrupt`, `proximity_low_interrupt`, `light_high_interrupt`, `light_low_interrupt`: interrupt flags. Each one returns `True` once after the event and then clears.
- `proximity_shutdown`, `light_shutdown`, `white_shutdown`: turn each channel off.

## Notes

- The register map follows the VCNL4040 layout used by the Adafruit library. The driver was checked with a simulated I2C bus; test it on your board before relying on it.
