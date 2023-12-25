from machine import Pin
from time import sleep

ledG = Pin(27, Pin.OUT)
ledY = Pin(26, Pin.OUT)
ledR = Pin(25, Pin.OUT)

while True:
  ledG.value(1)
  sleep(0.1)
  ledG.value(0)
  sleep(0.1)
  ledY.value(1)
  sleep(0.1)
  ledY.value(0)
  sleep(0.1)
  ledR.value(1)
  sleep(0.1)
  ledR.value(0)
  sleep(0.1)
