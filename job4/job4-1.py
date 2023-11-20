from machine import Pin
from time import sleep
import dht
sensor = dht.DHT22(Pin(0))
while True:
    sensor.measure()
    temp = sensor.temperature() 
    hum = sensor.humidity()
    print("Temperature: {0}°C Humidity: {1}% ".format(temp, hum))
    sleep(2)