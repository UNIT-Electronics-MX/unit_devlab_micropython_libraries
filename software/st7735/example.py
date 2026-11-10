# Library: st7735.py
# Description: Displays text and basic shapes on an 80x160 ST7735S TFT over SPI.
# Suggested file name on the board: main.py

from machine import Pin, SPI, SoftSPI
from st7735 import TFT
import time

# ST7735 display labels SDA/SCL correspond to SPI MOSI/SCK.
SPI_ID = 1
SDA_MOSI_PIN = 7
SCL_SCK_PIN = 27
UNUSED_MISO_PIN = 26  # Required by SoftSPI; no wire to the TFT.
USE_SOFT_SPI = False  # Hardware SPI on the dedicated D11/D13 pins.
CS_PIN = 1       # A1
DC_PIN = 4       # A2
RES_PIN = 5      # A3
BLK_PIN = -1     # No GPIO control of the backlight.

# If rewired to D11/GPIO7 (MOSI) and D13/GPIO27 (SCK), keep
# the onboard microSD card deselected on the shared SPI bus.
if SDA_MOSI_PIN == 7 and SCL_SCK_PIN == 27:
    Pin(23, Pin.OUT, value=1)

if USE_SOFT_SPI:
    print("ST7735: configurando SPI por software")
    spi = SoftSPI(
        baudrate=1_000_000,
        polarity=0,
        phase=0,
        sck=Pin(SCL_SCK_PIN),
        mosi=Pin(SDA_MOSI_PIN),
        miso=Pin(UNUSED_MISO_PIN),
    )
else:
    print("ST7735: configurando SPI de hardware")
    spi = SPI(
        SPI_ID,
        baudrate=1_000_000,
        polarity=0,
        phase=0,
        sck=Pin(SCL_SCK_PIN),
        mosi=Pin(SDA_MOSI_PIN),
    )

if BLK_PIN >= 0:
    Pin(BLK_PIN, Pin.OUT, value=1)

tft = TFT(spi, DC_PIN, RES_PIN, CS_PIN,
          width=80, height=160, xoffset=26, yoffset=1)
print("ST7735: inicializando pantalla")
tft.initg()
tft.rgb(False)
tft.invertcolor(True)

print("ST7735: prueba de color rojo")
tft.fill(TFT.RED)
time.sleep_ms(3000)

tft.fill(TFT.BLACK)
tft.text((8, 8), "UNIT", TFT.WHITE)
tft.text((8, 20), "ST7735", TFT.CYAN)
tft.line((4, 40), (75, 40), TFT.YELLOW)
tft.rect((4, 50), (30, 32), TFT.RED)
tft.fillrect((46, 50), (30, 32), TFT.GREEN)
tft.circle((20, 116), 14, TFT.BLUE)
tft.fillcircle((58, 116), 14, TFT.PURPLE)
tft.pixel((40, 116), TFT.WHITE)
print("ST7735: dibujo terminado")
