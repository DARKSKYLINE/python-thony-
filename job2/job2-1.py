from machine import Pin
import time

p18 = Pin(18,Pin.OUT)

while(1):
    p18.on()
    time.sleep_ms(100)
    p18.off()
    time.sleep_ms(50)