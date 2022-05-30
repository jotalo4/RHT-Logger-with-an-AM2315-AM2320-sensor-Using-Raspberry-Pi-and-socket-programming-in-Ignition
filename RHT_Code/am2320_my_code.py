# This program is written by Orukotan, AYomikun Samuel
# First of all, construct your class as desired.

# Import necessary libraries
#import posix
import os
import fcntl
import time
from bme280pi.sensor import Sensor


class AM2320:
    
    """A driver for the AM2320 temperature and humidity sensor.

    :param i2c_bus: The `busio.I2C` object to use. This is the only required parameter.
    :param int address: (optional) The I2C address of the device.

    """
 # Constructor to set up the class
    def __init__(self):
        #Set the i2c address
        self.address = 0x5c
        
        # Set the i2c slave address (0xB8
        self.slave = 0x0703

        #Open the i2c bus in read/write mode as a file object
        self.fd = os.open("/dev/i2c-1", os.O_RDWR)
        fcntl.ioctl(self.fd, self.slave, self.address)

        #List for holding raw read data
        self.raw_data = [0,0,0,0]

        #Initial values for variables
        self.temperature = 0
        self.humidity = 0
        self.fahrenheit = 0

        #Initial value for CRC check
        self.CRC = 0xFFFF

#A function to read data from the sensor, calculate temperature and
# humidity and store in the variables in the object
    def get_data(self):

        #Reset the CRC variable
        self.CRC = 0xFFFF

#The AM2320 drops into sleep mode when not interacted
#with for a while.  It wakes up when poked across the i2c bus
#but doesn't return data immediately, so poke it to wake it
#and ignore the fact that no acknowledgement is recieved.
        try:
            os.write(self.fd, b'\0x00') 
        except:
            pass
        time.sleep(0.003)#Wait at least 0.8ms, at most 3ms
        
#Tell the sensor you want to read data (0x03), starting at register 0 
#(0x00), and that you want 4 bytes of sensor data.  This starts the read
#at the humidity most significant byte, passes through the humidity least
#significant and temperature most significant bytes and stops after
#reading the temperature least significant bit.
        os.write(self.fd, b'\x03\x00\x04') 

#Give the sensor a few microseconds to take measurements (if you don't it
#gives an I/O Error).  The value was arrived at by trial and error, it
#may need tweaking or may possibly be turned down a bit.
        time.sleep(0.0016) #Wait at least 1.5ms for result

# Read the data into the list called "raw_data".  Bytes 0 and 1 are the
# instructions given to the device (0x03 and 0x04), given to check that 
# what was read is what was asked for.  Bytes 2 and 3 are the
# humidity high and low bytes respectively.  Bytes 4 and 5 are the
# temperature high and low bytes respectively.  Bytes 6 and 7 are the CRC
# high and low bytes respectively (see below).

#Read out 8 bytes of result data
    # Byte 0: Should be Modbus function code (0x03)
    # Byte 1: Should be number of registers to read (0x04)
    # Byte 2: Humidity msb
    # Byte 3: Humidity lsb
    # Byte 4: Temperature msb
    # Byte 5: Temperature lsb
    # Byte 6: CRC lsb byte
    # Byte 7: CRC msb byte

        self.raw_data = bytearray(os.read(self.fd, 8))


#Do the Cyclic Redundancy Code (CRC) check.  This progressively combines
#the first 6 bytes recieved (raw_data bytes 0-5) with a variable of value
#0xFFFF in a way which should eventually result in a value which is equal
#to the combined CRC bytes.  If this check fails then something has been
#corrupted during transmission.
        
        for byte in self.raw_data[0:6]:
            self.CRC = self.CRC ^ byte
            for x in range (0,8):
                if (self.CRC & 0x0001 == 0x0001):
                    self.CRC = self.CRC >> 1
                    self.CRC = self.CRC ^ 0xA001
                else:
                    self.CRC = self.CRC >> 1
                    
#If raw_data 0 + 1 (the returned intruction codes) don't match 0x03 and
#0x04 (the instructions which were given) alert the user to the error
        if ((self.raw_data[0] != 0x03) or (self.raw_data[1] != 0x04)):
            print("ERROR: received bytes 0 and 1 corrupt")
        
#If the CRC bytes don't equal the calculated CRC code alert the user to
#the error.
        if (self.CRC != ((self.raw_data[7] << 8) + self.raw_data[6])):
            print("CRC error, data corrupt!")
        #Otherwise, everything is fine and calculate the temp/humidity values
        else:
            
            
# The following Information are retrieved from the AM2315 datasheet
# Bitshift the temperature most significant byte left by 8 bits
# and combine with the least significant byte.
# Temperature resolution is 16Bit, 
# temperature highest bit (Bit15) is equal to 1 indicates a
# negative temperature, the temperature highest bit (Bit15)
# is equal to 0 indicates a positive temperature; 
# temperature in addition to the most significant bit (Bit14 ~ Bit0)
# indicates the temperature sensor string value.
# Temperature sensor value is a string of 10 times the
# actual temperature value.
# If bit 15 is zero, the temperature
# is positive so just divide it by 10 to get the temperature in 
# degrees Celsius/

            self.temperature = ((self.raw_data[4] << 8)\
 + self.raw_data[5])
        if ((self.temperature & 0x8000) == 0x8000):
                self.temperature = self.temperature & 0x7FFF
                self.temperature = -self.temperature/10.0
        else:
                self.temperature = self.temperature / 10.0

# Convert the temperature to Fahrenheit
                self.fahrenheit = (9.0/5.0) * self.temperature + 32 

#Bitshift the humidity most significant byte left by 8 bits and add
#it to the least significant byte.  Divide this by 10 to give the
#humidity in % relative humidity, according to the datasheet.
                self.humidity = ((self.raw_data[2] << 8) \
 + self.raw_data[3])/10.0

        

#     def two_decimals(number ):
#         stry = "%.2f" % number
#         return (float(stry))
#     temperature =two_decimals(temperature)
#     fahrenheit=two_decimals(fahrenheit)
#     humidity=two_decimals(humidity)
#     #return(temperature, fahrenheit, humidity)
    
        