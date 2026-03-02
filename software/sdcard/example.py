import machine
import os
from sdcard import SDCard

# Definir pines para SPI y SD
MOSI_PIN = 7
MISO_PIN = 2
SCK_PIN = 6
CS_PIN = 19

# Inicializar SPI
spi = machine.SPI(1, baudrate=500000, polarity=0, phase=0,
                  sck=machine.Pin(SCK_PIN),
                  mosi=machine.Pin(MOSI_PIN),
                  miso=machine.Pin(MISO_PIN))

# Inicializar tarjeta SD
sd = SDCard(spi, machine.Pin(CS_PIN))

# Montar la SD en el sistema de archivos
os.mount(sd, "/sd")

# Listar archivos y directorios en la SD
print("Archivos en la SD:")
print(os.listdir("/sd"))