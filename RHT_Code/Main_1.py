import board
import time
import busio
import am2320_my_code 
from am2320_my_code import *
import csv
import os.path
import datetime
import matplotlib
import schedule
import os
import stat
import shutil
import socket
import pickle
#from Server import *
# Socket Initialization, binding, message queue size, TCP format
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('0.0.0.0', 80))
server.listen(5)

#file_exists = os.path.isfile(filename)
fieldnames = (['Current Date', 'Current Time', 'Temperature(C)', 'Temperature(F)', 'Relative Humidity (%)'])  # list of keys for the dict

# Requesting for current time and date
my_date = datetime.datetime.now()

# Get Current Date Time Attributes in Python
my_hour = my_date.hour
my_minute = my_date.minute
my_second = my_date.second



#Reformat Date and time for the purpose of plotting
date_new = datetime.date.strftime(my_date, "%b %d %Y")
time_new = datetime.date.strftime(my_date, "%H:%M")


# convert current date into timestamp
time_timestamp = datetime.datetime.timestamp(my_date)


# # create the I2C shared bus
#i2c = busio.I2C(board.SCL, board.SDA)
def get_ctemp():
        temperature = sensor.temperature
        temperature = str(sensor.temperature)
        return(temperature)
    
def get_ftemp():
        fahrenheit = sensor.fahrenheit
        fahrenheit = str(sensor.fahrenheit)
        return(fahrenheit)
    
def get_humidity():
        humidity = sensor.humidity
        humidity = str(sensor.humidity)
        return(humidity)

#Create an object from the AM2320 class called "sensor"
sensor = am2320_my_code.AM2320()


#Do the following continuously:
while True:
    
    #Tell the sensor object to read data from the physical sensor
    sensor.get_data()
    #Print the temp. and humidity values now stored in the sensor object
    print(str(sensor.temperature) + "\xb0C")
    print(str(round(sensor.fahrenheit, 1)) + "F")
    print(str(sensor.humidity) + "%\n")
    
    conn, addr = server.accept()
    
    #Formatting my Date and time
    Date = datetime.date.strftime(my_date, "%m-%d-%Y")
    Time = datetime.date.strftime(my_date, "%H:%M:%S%p")
   
    #data = [Date, Time, get_ctemp(), get_ftemp(), get_humidity()]
    data = str(my_date) + "," + str(sensor.temperature)+ "," + str(round(sensor.fahrenheit, 1))+"," + str(sensor.humidity)
    #data = str(Date) + "," + str(Time) + "," + "ctemp:" + str(get_ctemp())+","+"ftemp:"+str(get_ftemp())+"," + "Humidity:"+ str(get_humidity())
    filename = '/home/pi/Work_Files/Project/Data_files/sensor_data_{}.csv'.format(Date)
    #print ('Got connection from', addr)
    socket_data= str(data).encode()
    #socket_data= pickle.dumps(data)
    conn.send(socket_data)
    conn.close()
        
 
#Exporting raw data sensor into csv files
#     with open(filename, mode = 'a', newline='') as ouput:
#         output_data = csv.writer(ouput, dialect = 'excel')
#         
#         if(os.stat(filename).st_size == 0):
#              output_data.writerow(fieldnames)
#         else:     
#              output_data.writerow(data)     
                  
    #process_new_file()     # does nothing if no new file               
#Delay before the next reading
    time.sleep(2.0)





