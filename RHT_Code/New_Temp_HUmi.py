import board
import adafruit_bus_device
from adafruit_bus_device.i2c_device import I2CDevice
import smbus2
from smbus2 import SMBus
import adafruit_am2320
import busio
#import smbus
import time

# Address of the sensor (AM2315)
address = 0x5c

# I2C Address of the device
SLA = 0xB8

#Create an interface to access the I2C bus
#I2C class specifies the clock line and data line pins
#<Object_name> = smbus.SMBus(I2C_Port_Number)
# bus = smbus2.SMBus(1)
# create the I2C shared bus
bus = busio.I2C(board.SCL, board.SDA)

#device = I2CDevice(i2c, 0x70)
sensor = adafruit_am2320.AM2320(bus)


#cancel sensor sleep
#try:
    #bus.writeto(address, buffer,*, start=0, end = len(buffer), stop=False)
    
 #   bus.writeto(address, buffer, stop=False)
#except:
 #   pass

time.sleep(0.003)
print('Humidity: {0}%'.format(sensor.relative_humidity))
time.sleep(0.0015)

print('Temperature: {0}C'.format(sensor.temperature))
       
       
#print("Humidity:", sensor.relative_humidity)
#print("Temperature:", sensor.temperature)
#time.sleep_ms(4000)

#time.sleep(0.003)
#bus.writeto(address, [0x03, 0x00, 0x04])


#Receive Data
#time.sleep(0.015)
#block = bus.readfrom(address, 6)

#Display Received Data
#print(block)
#while True:
#sensor.measure()


# Output data to screen
#print ("Relative Humidity is : %.2f %%" %humidity)
#print ("Temperature in Celsius is : %.2f C" %cTemp)
#print ("Temperature in Fahrenheit is : %.2f F" %fTemp)
