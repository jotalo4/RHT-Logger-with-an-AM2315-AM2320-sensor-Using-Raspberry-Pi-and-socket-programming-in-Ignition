import matplotlib
import ast
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation 
from itertools import count
from matplotlib.figure import Figure
import am2320_my_code 
from am2320_my_code import *
import datetime
import numpy as np
import csv
#from Main import *

global anim

filename = '/home/pi/Work_Files/Project/Data_files/sensor_data.csv'

sensor = am2320_my_code.AM2320()

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
    
date_new = datetime.date.strftime(my_date, "%b %d %Y")
time_new = datetime.date.strftime(my_date, "%H:%M")


with open(filename, mode = 'r') as data_read:
    updated_data = (csv.reader(data_read, delimiter = ','))
    
#Extracting data

Date = updated_data[0]
Time = updated_data[1]
ct = updated_data[2]
ft = updated_data[3]
humi = updated_data[4]


def animate(i):

    lines = updated_data.split(',')
    
    
    for row in lines:
        if len(row) > 1:
           [Date_now, time_now, temperature_now, fahrenheit_now, humidity_now] = row.strip().split(',')
            

    Date.append(Date_now)
    Time.append(time_now)
    ct.append(float(temperature_now))
    ft.append(float(fahrenheit_now))
    humi.append(float(humidity_now))
      
    
# Create a figure
fig = plt.figure(figsize=(20,20))
fig.tight_layout()
plt.style.use('fivethirtyeight')

fig.add_subplot(3,1,1)
plot1 = plt.plot(Time, ct, 'bo', label = "Celsius")
plt.ylabel("Temperature readings"), plt.title("Temperature Graph")
plt.legend()


fig.add_subplot(3,1,2)
plot2 = plt.plot(Time, ft, 'g-', label = "Fahrenheit")
plt.ylabel("Fahrenheit readings"), plt.title("Fahrenheit Graph")
plt.legend()

fig.add_subplot(3,1,3)
plot3 = plt.plot(Time, humi, 'r-', label = "Humidity")
plt.xlabel("Current Time"), plt.ylabel("Humidity readings"), plt.title("Humidity Graph")
plt.legend()

    
anim = FuncAnimation(fig, animate, interval=1000)
plt.show()
   
 
