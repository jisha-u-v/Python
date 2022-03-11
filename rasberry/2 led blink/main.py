from machine import Pin
import utime

led1 = Pin(15, Pin.OUT)
led2 = Pin(14, Pin.OUT)

while True:
  led1.toggle()
  utime.sleep(2)
  led2.toggle()
