# SD Card Driver for MicroPython

This library provides a MicroPython driver for SD/SDHC cards using the SPI interface. It allows you to mount SD cards to the filesystem and perform file operations.

> **Note**: This library is part of the [UNIT DevLab MicroPython Libraries Collection](../../README.md) - a curated compilation of useful MicroPython libraries.

## Credits

**Original Author**: MicroPython Project Contributors  
**Source**: [micropython/micropython-lib](https://github.com/micropython/micropython-lib)  
**License**: MIT License  
**Compiled by**: UNIT DevLab

This library is based on the SD card driver from the official MicroPython library repository. All credits go to the original authors and contributors. It is included here as part of a curated collection for convenience.

## Features

- Support for SD and SDHC cards
- SPI interface communication
- Standard filesystem operations (read, write, create, delete)
- Directory listing and navigation
- Compatible with MicroPython's `os` module

## Hardware Requirements

- MicroPython-compatible microcontroller (ESP32, ESP8266, RP2040, etc.)
- SD card module with SPI interface
- SD card (SD or SDHC, FAT16/FAT32 formatted)

### Wiring

Connect the SD card module to your microcontroller:

| SD Module | Microcontroller |
|-----------|----------------|
| MOSI      | SPI MOSI pin   |
| MISO      | SPI MISO pin   |
| SCK       | SPI SCK pin    |
| CS        | Any GPIO pin   |
| VCC       | 3.3V or 5V     |
| GND       | GND            |

## Installation

1. Copy `sdcard.py` to your MicroPython device
2. Place it in the root directory or `/lib` folder

## Usage

```python
import machine
import os
from sdcard import SDCard

# Define SPI pins
MOSI_PIN = 7
MISO_PIN = 2
SCK_PIN = 6
CS_PIN = 19

# Initialize SPI
spi = machine.SPI(1, 
                  baudrate=500000,
                  polarity=0,
                  phase=0,
                  sck=machine.Pin(SCK_PIN),
                  mosi=machine.Pin(MOSI_PIN),
                  miso=machine.Pin(MISO_PIN))

# Initialize SD card
sd = SDCard(spi, machine.Pin(CS_PIN))

# Mount the SD card to the filesystem
os.mount(sd, "/sd")

# List files on SD card
print("Files on SD card:")
print(os.listdir("/sd"))

# Create a file
with open("/sd/test.txt", "w") as f:
    f.write("Hello from MicroPython!")

# Read a file
with open("/sd/test.txt", "r") as f:
    content = f.read()
    print(content)

# Unmount when done (optional but recommended)
os.umount("/sd")
```

## API Reference

### Initialization

```python
SDCard(spi, cs_pin, baudrate=1320000)
```

**Parameters:**
- `spi` - SPI bus object (machine.SPI)
- `cs_pin` - Chip Select pin (machine.Pin)
- `baudrate` - SPI communication speed (optional, default 1320000)

### Filesystem Operations

After mounting with `os.mount(sd, "/sd")`, you can use standard Python file operations:

```python
# List directory
os.listdir("/sd")

# Create directory
os.mkdir("/sd/data")

# Remove directory
os.rmdir("/sd/data")

# Remove file
os.remove("/sd/file.txt")

# Rename file
os.rename("/sd/old.txt", "/sd/new.txt")

# Get file stats
os.stat("/sd/file.txt")

# Change directory
os.chdir("/sd")

# Get current directory
os.getcwd()
```

### File Operations

```python
# Write to file
with open("/sd/data.txt", "w") as f:
    f.write("Hello World\n")

# Read from file
with open("/sd/data.txt", "r") as f:
    content = f.read()

# Append to file
with open("/sd/data.txt", "a") as f:
    f.write("New line\n")

# Binary mode
with open("/sd/data.bin", "wb") as f:
    f.write(bytes([0x01, 0x02, 0x03]))
```

## Example

See [example.py](example.py) for a complete working example.

## Troubleshooting

**SD card not detected:**
- Check SPI wiring connections
- Verify the SD card is properly inserted
- Ensure the SD card is formatted as FAT16 or FAT32
- Try reducing the SPI baudrate (some cards are slower)
- Check power supply (SD cards need stable 3.3V)

**OSError: [Errno 19] ENODEV:**
- SD card initialization failed
- Check connections and try a different SD card
- Verify the CS pin is correct

**File operations fail:**
- Ensure the SD card is mounted before use
- Check available space on the SD card
- Verify the card isn't write-protected

**Slow performance:**
- Increase SPI baudrate (up to 10-20 MHz for fast cards)
- Use binary mode for faster operations
- Consider buffering for multiple small writes

## Performance Tips

1. Use higher baudrates for faster transfers (test compatibility first)
2. Write/read larger chunks of data instead of byte-by-byte
3. Close files properly to ensure data is written
4. Unmount the SD card before removing it to prevent corruption

## Compatibility

- SD cards: Up to 2GB
- SDHC cards: 4GB to 32GB
- File systems: FAT16, FAT32
- Not compatible with SDXC cards (>32GB) or exFAT

## License

MIT License - Original MicroPython library  
See [LICENSE](../../LICENSE) file for details

## Additional Resources

- [MicroPython os module documentation](http://docs.micropython.org/en/latest/library/os.html)
- [SD Card Specifications](https://www.sdcard.org/downloads/pls/)
- [MicroPython Library Repository](https://github.com/micropython/micropython-lib)
