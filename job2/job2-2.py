from machine import Pin
import time

p18 = Pin(18,Pin.OUT)
p19 = Pin(19,Pin.OUT)
p20 = Pin(20,Pin.OUT)

while(1):
    p18.on()
    time.sleep_ms(100)
    p18.off()
    time.sleep_ms(1)
    p19.on()
    time.sleep_ms(100)
    p19.off()
    time.sleep_ms(1)
    p20.on()
    time.sleep_ms(100)
    p20.off()
    time.sleep_ms(1)