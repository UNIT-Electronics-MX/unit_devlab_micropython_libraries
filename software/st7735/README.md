# ST7735 TFT Display Driver for MicroPython

This folder contains the ST7735 SPI driver, an example, and wiring
instructions for the [UNIT Electronics 0.96-inch ST7735S module](https://uelectronics.com/producto/tft-display-lcd-0-96-spi-hd-65k-colores-st7735/).
That module has an 80x160 visible area. It is part of the
[UNIT DevLab MicroPython Libraries Collection](../../README.md).

## Credits

`st7735.py` is based on [GuyCarver's ST7735 driver](https://github.com/GuyCarver/MicroPython/blob/master/lib/ST7735.py),
adapted for MicroPython by [boochow](https://github.com/boochow/MicroPython-ST7735).
The built-in text path and UNIT DevLab example are local additions.

## Wiring

| TFT pin | Board connection | GPIO |
|---|---|---|
| CS | A1 | 1 |
| DC / A0 | A2 | 4 |
| RES / RST | A3 | 5 |
| SDA / MOSI | SPI data | 2 |
| SCL / SCK | SPI clock | 3 |
| BLK / LED | No GPIO control (`-1`) | — |
| VCC | Module supply | — |
| GND | GND | — |

The display pins named SDA and SCL are SPI data and clock, not I2C pins.
The example uses software SPI on GPIO2/GPIO3 at 1 MHz to check the supplied
wiring. `SoftSPI` requires a MISO argument, so GPIO26 is configured as an
unconnected input; the TFT itself does not need MISO. Set `USE_SOFT_SPI = False`
to try hardware SPI on the same pins.

On the [UNIT PULSAR ESP32-C5](https://github.com/UNIT-Electronics-MX/unit_pulsar_esp32_c5/blob/main/tools/product-reference/chapters/04-connectors-pinouts.md),
GPIO2 and GPIO3 are the onboard sensor I2C bus with pull-ups and five
connected devices. The board's dedicated SPI signals are MOSI=GPIO7 (`D11`)
and SCK=GPIO27 (`D13`). If the supplied wiring still produces no image,
move the display SDA/SCL wires to those dedicated SPI pins and change the
two pin constants in `example.py` to 7 and 27; also set `USE_SOFT_SPI = False`.
The example then keeps the onboard microSD card deselected on GPIO23.

`BLK_PIN = -1` disables GPIO backlight control. If the module needs separate
LED power, connect BLK to its specified supply. For an active-high GPIO
backlight, change `BLK_PIN` in `example.py` to that GPIO number.

## Installation and example

Copy `st7735.py` to the board's root or `/lib` directory. Copy `example.py`
as `main.py`, or run it from the REPL. The example is configured for an
ESP32-C5 and the 80x160 module. It first shows a red screen for three
seconds, then writes two text labels and draws a
line, outline rectangle, filled rectangle, outline circle, filled circle,
and pixel.

```python
from machine import Pin, SoftSPI
from st7735 import TFT

spi = SoftSPI(baudrate=1_000_000, polarity=0, phase=0,
              sck=Pin(3), mosi=Pin(2), miso=Pin(26))
tft = TFT(spi, 4, 5, 1, width=80, height=160,
          xoffset=26, yoffset=1)  # DC, RES, CS
tft.initg()
tft.rgb(False)
tft.invertcolor(True)
tft.fill(TFT.BLACK)
tft.text((8, 8), "Hola", TFT.WHITE)
tft.rect((8, 30), (40, 30), TFT.RED)
```

## Drawing API

- `fill(color)` fills the configured display area (80x160 in the example).
- `text((x, y), string, color, font=None, size=1, nowrap=False)` writes text.
  Without a font argument, it uses MicroPython's built-in 8x8 `framebuf` font;
  a compatible font dictionary can still be passed as in the original driver.
- `pixel((x, y), color)` draws a pixel.
- `line(start, end, color)`, `hline(start, length, color)`, and
  `vline(start, length, color)` draw lines.
- `rect(start, (width, height), color)` and `fillrect(...)` draw rectangles.
- `circle(center, radius, color)` and `fillcircle(...)` draw circles.
- `rotation(0..3)` changes orientation; `size()` returns current dimensions.
- `TFTColor(r, g, b)` converts RGB values to RGB565.

For this 0.96-inch module, the example uses the common green-tab layout with
column offset 26, row offset 1, BGR color order, and color inversion. Some
80x160 modules instead use column offset 24, row offset 0 and RGB order; if
the red test appears but is shifted or has wrong colors, change those values
and use `tft.rgb(True)` and `tft.invertcolor(False)`.

If the example prints its status messages but never shows the red screen,
check display power and BLK first, then verify CS/DC/RES/SDA/SCL wiring. If
SPI construction raises an error, the selected SPI bus or pin combination is
not supported by that MicroPython port; use a compatible bus for the board.
