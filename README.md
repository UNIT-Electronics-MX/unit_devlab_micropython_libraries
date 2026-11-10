# UNIT DevLab - MicroPython Libraries Collection

A curated collection of useful MicroPython libraries for embedded development. This repository serves as a compendium of various drivers and utilities, gradually compiled to support different hardware modules and sensors.

[![GitHub](https://img.shields.io/badge/GitHub-UNIT_Electronics-blue?logo=github)](https://github.com/UNIT-Electronics-MX/unit_devlab_micropython_libraries)
[![Documentation](https://img.shields.io/badge/Documentation-Wiki-orange)](https://wiki.uelectronics.com/tutoriales/micropython)
[![Website](https://img.shields.io/badge/Website-UNIT_Electronics-green)](https://uelectronics.com/)

## About This Repository

This is a **collection repository** that compiles and organizes MicroPython libraries from various sources. Each library retains its original authorship and license. The goal is to provide a centralized, easy-to-use resource for MicroPython developers working with common hardware components.


## Libraries

| Library | Device | Folder | Main file | Example |
|---|---|---|---|---|
| BMI270 | Accelerometer / gyroscope (Bosch) | [software/bmi270/](software/bmi270/) | [bmi270.py](software/bmi270/bmi270.py) | [example.py](software/bmi270/example.py) |
| MMC5603 | 3-axis magnetometer (MEMSIC) | [software/mmc5603/](software/mmc5603/) | [mmc5603.py](software/mmc5603/mmc5603.py) | [example.py](software/mmc5603/example.py) |
| MAX17043 / MAX17048 | LiPo fuel gauge (Maxim) | [software/max1704x/](software/max1704x/) | [max1704x.py](software/max1704x/max1704x.py) | [example.py](software/max1704x/example.py) |
| FHT40 | Temperature and humidity | [software/fht40/](software/fht40/) | [fht40.py](software/fht40/fht40.py) | [example.py](software/fht40/example.py) |
| LPS22HB | Pressure and temperature (STMicroelectronics) | [software/lps22hb/](software/lps22hb/) | [lps22hb.py](software/lps22hb/lps22hb.py) | [example.py](software/lps22hb/example.py) |
| VCNL4040 | Proximity and ambient light (Vishay) | [software/vcnl4040/](software/vcnl4040/) | [vcnl4040.py](software/vcnl4040/vcnl4040.py) | [example.py](software/vcnl4040/example.py) |
| SSD1306 | OLED display (I2C / SPI) | [software/ssd1306/](software/ssd1306/) | [ssd1306.py](software/ssd1306/ssd1306.py) | [example.py](software/ssd1306/example.py) |
| SD card | SD card over SPI | [software/sdcard/](software/sdcard/) | [sdcard.py](software/sdcard/sdcard.py) | [example.py](software/sdcard/example.py) |
| ST7735 | 80x160 TFT display (SPI) | [software/st7735/](software/st7735/) | [st7735.py](software/st7735/st7735.py) | [example.py](software/st7735/example.py) |

Each folder has a `README.md` with the connection, installation and usage details.

## Example Structure

Each library folder follows the same layout:

```
software/<library>/
├── <library>.py   # the driver: the only file you need on the board
├── example.py     # minimal example with the board pins configured at the top
└── README.md      # connection, installation and API summary
```

Some folders include an extra example (for instance `bmi270_simpletest.py`). The pins are set at the top of each `example.py`: the onboard sensors (MMC5603, MAX17048, FHT40, LPS22HB, VCNL4040) use GPIO2 / GPIO3, while the BMI270 and SSD1306 examples use GPIO6 / GPIO7. The ST7735 SPI example uses GPIO2 / GPIO3 for MOSI / SCK and GPIO1 / GPIO4 / GPIO5 for CS / DC / RES.

## Installation

Each library can be installed independently:

1. Navigate to the specific library folder
2. Copy the `.py` file(s) to your MicroPython device
3. Place them in the root directory or `/lib` folder
4. Import and use as shown in each library's documentation

## Usage

Each library includes:
- ✅ Complete source code
- ✅ Usage examples
- ✅ API documentation
- ✅ Hardware wiring diagrams
- ✅ Troubleshooting guides

See individual library README files for detailed usage instructions.

## Credits

**Compiled and Maintained by**: [UNIT Electronics](https://uelectronics.com/)

This repository is a compilation of libraries from various sources:

- **MicroPython Project**: Core libraries from [micropython/micropython-lib](https://github.com/micropython/micropython-lib)
- **Community Contributors**: Various open-source contributors

Each library folder contains proper attribution to its original authors. We do not claim authorship of these libraries - they are collected here for convenience and educational purposes.

## License

Each library maintains its original license (typically MIT). See individual library folders for specific license information.

The compilation and organization of this repository is provided as-is for educational and development purposes.

## Contributing

This is a curated collection. If you'd like to suggest additional libraries to include:

1. Ensure the library has a compatible open-source license
2. Provide proper attribution to original authors
3. Include documentation and examples
4. Test the library with MicroPython devices

## Compatibility

These libraries are designed for:
- ESP32
- ESP8266
- Raspberry Pi Pico (RP2040)
- Other MicroPython-compatible microcontrollers

Check individual library documentation for specific hardware requirements.

## Support

For library-specific issues, please refer to:
- [UNIT Electronics MicroPython Documentation](https://wiki.uelectronics.com/tutoriales/micropython)
- [UNIT Electronics Website](https://uelectronics.com/)
- Individual library documentation
- Original library repositories
- MicroPython official documentation: [docs.micropython.org](https://docs.micropython.org)

## Resources

### UNIT Electronics
- [UNIT Electronics Website](https://uelectronics.com/)
- [UNIT Electronics MicroPython Tutorials](https://wiki.uelectronics.com/tutoriales/micropython)
- [GitHub Repository](https://github.com/UNIT-Electronics-MX/unit_devlab_micropython_libraries)

### MicroPython Official
- [MicroPython Official Website](https://micropython.org/)
- [MicroPython Documentation](https://docs.micropython.org/)
- [MicroPython Library Repository](https://github.com/micropython/micropython-lib)
- [MicroPython Forum](https://forum.micropython.org/)

---

**Note**: This is a collection repository. All credits go to the original library authors. This compilation is maintained for educational purposes and to provide easy access to commonly used MicroPython libraries.
