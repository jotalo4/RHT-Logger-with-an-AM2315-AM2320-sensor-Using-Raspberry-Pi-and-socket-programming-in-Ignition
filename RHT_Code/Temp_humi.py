import time
import board
import busio
import adafruit_am2320
#import I2C
# import smbus

# Address of the sensor
address = 0x5c

#Create an interface to access the I2C bus
#I2C class specifies the clock line and data line pins
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_am2320.AM2320(i2c, address)

#i2c = smbus.SMBus(1)

# I2C Address
SLA = 0xB8


#cancel sensor sleep
try:
    i2c.writeto(SLA,[])
except:
    pass

time.sleep(1)
#Read temperature and humidity command
i2c.writeto(SLA, bytes([0x04]), stop=False)


#Receive Data
time.sleep(2)
result = bytearray(2)
i2c.readfrom_into(SLA, result)

#Display Received Data
print(result)
#sensor.write_byte(0x5c)
#time.sleep(0.5)

# SHT25 address, 0x40(64)
# Read data back, 2 bytes
# Temp MSB, Temp LSB
#data0 = sensor.read_byte(0x5c)
#data1 = sensor.read_byte(0x5c)

# Convert the data
#temp = data0 * 256 + data1
#cTemp= -46.85 + ((temp * 175.72) / 65536.0)
#fTemp = cTemp * 1.8 + 32

# SHT25 address, 0x40(64)
# Send humidity measurement command
# 0xF5(245)   NO HOLD master
#sensor.write_byte(0x5c)
#time.sleep(0.5)

# SHT25 address, 0x40(64)
# Read data back, 2 bytes
# Humidity MSB, Humidity LSB
#data0 = sensor.read_byte(0x5c)
#data1 = sensor.read_byte(0x5c)

# Convert the data
#humidity = data0 * 256 + data1
#humidity = -6 + ((humidity * 125.0) / 65536.0)


print("Humidity:", sensor.relative_humidity)
print("Temperature:", sensor.temperature)

# Output data to screen
#print ("Relative Humidity is : %.2f %%" %humidity)
#print ("Temperature in Celsius is : %.2f C" %cTemp)
#print ("Temperature in Fahrenheit is : %.2f F" %fTemp)
