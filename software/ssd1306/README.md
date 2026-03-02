# SSD1306 OLED Display Driver for MicroPython

This library provides a MicroPython driver for SSD1306-based OLED displays (128x64, 128x32, etc.) using I2C or SPI interfaces.

> **Note**: This library is part of the [UNIT DevLab MicroPython Libraries Collection](../../README.md) - a curated compilation of useful MicroPython libraries.

## Credits

**Original Author**: MicroPython Project Contributors  
**Source**: [micropython/micropython-lib](https://github.com/micropython/micropython-lib)  
**License**: MIT License  
**Compiled by**: UNIT DevLab

This library is from the official MicroPython library repository. All credits go to the original authors and contributors of the MicroPython project. It is included here as part of a curated collection for convenience.

## Features

- Support for both I2C and SPI interfaces
- Multiple display sizes (128x64, 128x32, 64x48, etc.)
- Full FrameBuffer graphics support
- Text rendering
- Basic shapes (lines, rectangles, circles)
- Pixel-level control

## Hardware Requirements

- MicroPython-compatible microcontroller (ESP32, ESP8266, RP2040, etc.)
- SSD1306 OLED display (I2C or SPI)

### I2C Wiring
- SDA → GPIO pin (configurable)
- SCL → GPIO pin (configurable)
- VCC → 3.3V or 5V
- GND → GND

### SPI Wiring
- MOSI → GPIO pin
- SCK → GPIO pin
- CS → GPIO pin
- DC → GPIO pin
- RES → GPIO pin
- VCC → 3.3V or 5V
- GND → GND

## Installation

1. Copy `ssd1306.py` to your MicroPython device
2. Place it in the root directory or `/lib` folder

## Usage

### I2C Interface

```python
import machine
from ssd1306 import SSD1306_I2C

# Configure I2C pins
I2C_SDA_PIN = 6
I2C_SCL_PIN = 7

# Initialize I2C
i2c = machine.SoftI2C(sda=machine.Pin(I2C_SDA_PIN), scl=machine.Pin(I2C_SCL_PIN))

# Create display object (128x32 pixels)
oled = SSD1306_I2C(128, 32, i2c)

# Clear display
oled.fill(0)
oled.show()

# Display text
oled.text('Hello World!', 0, 0)
oled.show()
```

### SPI Interface

```python
import machine
from ssd1306 import SSD1306_SPI

# Configure SPI pins
spi = machine.SPI(1, baudrate=1000000)
dc = machine.Pin(4)
res = machine.Pin(5)
cs = machine.Pin(15)

# Create display object
oled = SSD1306_SPI(128, 64, spi, dc, res, cs)

# Clear display
oled.fill(0)
oled.show()

# Display text
oled.text('Hello SPI!', 0, 0)
oled.show()
```

## API Reference

### Display Initialization

**I2C:**
```python
SSD1306_I2C(width, height, i2c, addr=0x3C, external_vcc=False)
```

**SPI:**
```python
SSD1306_SPI(width, height, spi, dc, res, cs, external_vcc=False)
```

### Methods

- `fill(color)` - Fill entire display (0=black, 1=white)
- `pixel(x, y, color)` - Set a single pixel
- `text(string, x, y, color=1)` - Draw text at position
- `show()` - Update the display with buffer contents
- `contrast(value)` - Set display contrast (0-255)
- `invert(True/False)` - Invert display colors
- `poweroff()` - Turn off display
- `poweron()` - Turn on display

### FrameBuffer Methods

Inherits all methods from MicroPython's FrameBuffer class:
- `hline(x, y, w, color)` - Horizontal line
- `vline(x, y, h, color)` - Vertical line
- `line(x1, y1, x2, y2, color)` - Draw line
- `rect(x, y, w, h, color)` - Draw rectangle
- `fill_rect(x, y, w, h, color)` - Filled rectangle
- `scroll(dx, dy)` - Scroll display content
- `blit(fbuf, x, y)` - Copy another FrameBuffer

## Example

See [example.py](example.py) for a complete working example.

## Troubleshooting

**Display not working:**
- Check I2C/SPI connections
- Verify I2C address (default 0x3C, some use 0x3D)
- Ensure proper pull-up resistors on I2C lines
- Check power supply voltage

**Garbled display:**
- Verify display resolution matches code (128x64 vs 128x32)
- Check SPI polarity and phase settings
- Reduce SPI baudrate if using long wires

## License

MIT License - Original MicroPython library  
See [LICENSE](../../LICENSE) file for details

## Additional Resources

- [MicroPython FrameBuffer documentation](http://docs.micropython.org/en/latest/library/framebuf.html)
- [SSD1306 Datasheet](https://cdn-shop.adafruit.com/datasheets/SSD1306.pdf)
- [MicroPython Library Repository](https://github.com/micropython/micropython-lib)
