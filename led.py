#!/usr/bin/python
import time
from neopixel import *
from threading import Thread

# LED strip configuration:
LED_COUNT      = 5      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 125     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
n=200

class RgbLed(Thread):
    def __init__(self):
        self.strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
        self.strip.begin()
        Thread.__init__(self)

    def fade(self,Rstart,Gstart,Bstart,Rend,Gend,Bend):
        for i in range(0,n,+1):
            Rnew = Rstart + (Rend - Rstart) * i / n
            Gnew = Gstart + (Gend - Gstart) * i / n
            Bnew = Bstart + (Bend - Bstart) * i / n
            self.colorSet(self.strip,Color(Rnew, Gnew, Bnew))
            self.strip.show()
            time.sleep(0.05)
        time.sleep(1)
        for i in range(0,n,+1):
            Rnew = Rend + (Rstart - Rend) * i / n
            Gnew = Gend + (Gstart - Gend) * i / n
            Bnew = Bend + (Bstart - Bend) * i / n
            self.colorSet(self.strip,Color(Rnew, Gnew, Bnew))
            self.strip.show()
            time.sleep(0.05)
        time.sleep(1)

    def run(self):
        while True:
            self.fade(0,0,150,85,70,200)

    def colorSet(self,strip, color):
        for i in range(self.strip.numPixels()):
            strip.setPixelColor(i, color)
        strip.show()

    def SCAN(self,strip):
        for i in range(self.strip.numPixels()):
            strip.setPixelColor(i,Color(0,0,150))
            time.sleep(1.2)
            strip.setPixelColor(i,Color(0,0,0))
            time.sleep(1.2)
	strip.show()

led=RgbLed()
led.start()
