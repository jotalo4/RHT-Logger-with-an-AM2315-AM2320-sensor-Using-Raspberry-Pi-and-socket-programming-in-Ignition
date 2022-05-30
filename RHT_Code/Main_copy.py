import board
import time
import busio
import am2320_my_code 
from am2320_my_code import *
import csv
import os.path
import datetime
import matplotlib
import matplotlib.pyplot as plt

#import LiveGraph


filename = '/home/pi/Work_Files/Project/Data_files/sensor_data.csv'
file_name = '/home/pi/Work_Files/Project/Data_files/readabledata.csv'
file_exists = os.path.isfile(filename)
fieldnames = (['Current Date', 'Current Time', 'Temperature(C)', 'Temperature(F)', 'Relative Humidity (%)'])  # list of keys for the dict

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

        
# Requesting for current time and date
my_date = datetime.datetime.now()

#Formatting my Date and time
Date = datetime.date.strftime(my_date, "%m-%d-%Y")
Time = datetime.date.strftime(my_date, "%H:%M:%S%p")

#Reformat Date and time for the purpose of plotting
date_new = datetime.date.strftime(my_date, "%b %d %Y")
time_new = datetime.date.strftime(my_date, "%H:%M")


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
    
 
#Exporting raw data sensor into csv files
    with open(filename, mode = 'a',  newline = '') as ouput:
       #with open(file_name, newline = '') as csv_file: 
         output_data = csv.writer(ouput, dialect = 'excel')
         #data = csv.reader(csv_file, dialect = 'excel')
         #data_list = list(data)
         line_num = 0 
# Determining the header row)
      
         for row in data:
             
            
             d.append(date_new)
             t.append(time_new)
             c.append(get_ctemp())
             f.append(get_ftemp())
             h.append(get_humidity())
                 
             if line_num == 0:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
                    output_data.writerow(row)
                   #print("This is the header row")    
                    line_num += 1
             else:
                    output_data.writerow(row)
        #              
                    line_num += 1
             #print("This row contains data")
         
         output_data.writerow([Date, time_new, get_ctemp(), get_ftemp(), get_humidity()])
         
       plt.plot(t, c, "-b", label = "Celsius")
                   
# Plot real time data
#     plt.plot(time_new, get_ctemp(), "-b", label = "Celsius")
#     plt.plot(t, c, "-b", label = "Celsius")
#     plt.plot(t, f, "-r", label = "Fahrenheit")
#     plt.plot(t, h, "-g", label = "Humidity")
# 
#     plt.draw()             

        

#         # PLot real time data
#          plt.plot(t, c, "-b", label = "Celsius")
#          plt.plot(t, f, "-r", label = "Fahrenheit")
#          plt.plot(t, h, "-g", label = "Humidity")

#         # Configuring the plot
#          plt_configure(xlabel = 'Current Time', ylabel = 'Temperature Readings', title = 'Temperature Graph', legend = {'loc': 'upper right'}, grid = 'True')
#          plt_configure(xlabel = 'Current Time', ylabel = 'Fahrenheit Readings', title = 'Fahrenheit Graph', legend = {'loc': 'upper right'}, grid = 'True')
#          plt_configure(xlabel = 'Current Time', ylabel = 'Humidity Readings', title = 'Humidity Graph', legend = {'loc': 'upper right'}, grid = 'True')
#          
        #          # # Draw the graph
        #          plt.show()
   
#Delay before the next reading
    time.sleep(2.0)
    






