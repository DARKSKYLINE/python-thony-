from machine import Pin, I2C, ADC
from ssd1306 import SSD1306_I2C
import framebuf,sys,time
from machine import Pin
from time import sleep
import dht
sensor = dht.DHT22(Pin(0))

pix_res_x  = 128 # SSD1306 horizontal resolution
pix_res_y = 64   # SSD1306 vertical resolution

i2c_dev = I2C(1,scl=Pin(27),sda=Pin(26),freq=200000)  # start I2C on I2C1 (GPIO 26/27)
i2c_addr = [hex(ii) for ii in i2c_dev.scan()] # get I2C address in hex format
if i2c_addr==[]:
    print('No I2C Display Found') 
    sys.exit() # exit routine if no dev found
else:
    print("I2C Address      : {}".format(i2c_addr[0])) # I2C device address
    print("I2C Configuration: {}".format(i2c_dev)) # print I2C params


oled = SSD1306_I2C(pix_res_x, pix_res_y, i2c_dev) # oled controller

#oled.write_cmd(0xc0) # flip display to place 0,0 at lower-left corner
adc_2 = machine.ADC(2) # ADC channel 2 for input

while True:
    oled.fill(0) # clear the display
    sensor.measure()
    temp = sensor.temperature() 
    hum = sensor.humidity()
    oled.text('Temp: {0} C '.format(temp, hum),0,0)
    oled.text('Hum: {1}% '.format(temp, hum),0,20)
    oled.show() # show the new text and image
    sleep(1)