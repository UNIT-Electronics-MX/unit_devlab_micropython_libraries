# MicroPython driver for the MAX17043 / MAX17048 LiPo Fuel Gauge

This library provides a MicroPython driver for the Maxim MAX17043, MAX17044 and MAX17048 LiPo battery fuel gauges over I2C. It reports the cell voltage, the state of charge and the alert status.

> **Note**: This library is part of the [UNIT DevLab MicroPython Libraries Collection](../../README.md) - a curated compilation of useful MicroPython libraries.

## Credits

This driver is based on the original project by **Andre Peeters**:
https://github.com/andrethemac/max17043.py/tree/master

Modified by **Cesar (@Cesar)**.

## Files

- `max1704x.py`: the complete library. It is the only file required.
- `example.py`: example that reads the cell voltage and the state of charge.

## Connection

- The MAX17048 on this board is an **onboard** sensor. It is on I2C bus 0, with SDA on GPIO2 and SCL on GPIO3 (`I2C(0, sda=Pin(2), scl=Pin(3))`).
- The I2C address is fixed: `0x36`.

## Installation

Copy `max1704x.py` to the board with Thonny (**File > Save copy...** and choose the MicroPython device). Then copy `example.py` to the board and rename it (for example, to `main.py`) so it runs on boot.

## Basic Usage

```python
from machine import I2C, Pin
from max1704x import max1704x

i2c = I2C(0, sda=Pin(2), scl=Pin(3), freq=400_000)
battery = max1704x(i2c, is_max17048=True)

print(battery.getVCell())   # cell voltage in V
print(battery.getSoc())     # state of charge in %
```

## Parameters

- `i2c`: the I2C bus object (`machine.I2C` or `machine.SoftI2C`).
- `address`: I2C address. Default `0x36`.
- `is_max17048`: `True` for the MAX17048 (default), `False` for the MAX17043/MAX17044. This changes how the cell voltage is converted.

## Main Methods

- `getVCell()`: cell voltage in volts.
- `getSoc()`: state of charge in percent.
- `getVersion()`: chip version.
- `getAlertThreshold()` / `setAlertThreshold(percent)`: low-battery alert threshold, 1 to 32 %.
- `inAlert()`: `True` if the alert flag is set. `clearAlert()` clears it.
- `getCompensateValue()`: compensation value from the configuration register.
- `quickStart()`: restarts the state-of-charge estimation. Use it after replacing the battery.
- `reset()`: resets the sensor.
- `sensor_exists()`: checks that the sensor answers on the bus.
- `address()`: returns the I2C address.
