import os, sys
import os.path
#from pathlib import Path
import csv
import DateTime
import math
import re
import sys
from time import altzone
from time import daylight
from time import gmtime
from time import localtime
from time import time
from time import timezone
from time import tzname
from datetime import datetime

from zope.interface import implementer

from DateTime.interfaces import IDateTime
from DateTime.interfaces import DateTimeError
from DateTime.interfaces import SyntaxError
from DateTime.interfaces import DateError
from DateTime.interfaces import TimeError
from DateTime.pytz_support import PytzCache


#class Environmental_data_logger(object):
@implementer(IDateTime)
class DateTime(object):
    def __init__(file_name):
         file_name = ("/home/pi/Work_Files/Project/Data_files/sensor_data.csv")
         return()
    
    def entry_index():
        Index = str(entry_index)
        return(Index)
    
    def get_ctemp():
        temperature = sensor.temperature
        temperature = round((temperature), 2)
        temperature = str(temperature)
        return(temperature)
    
    def get_ftemp():
        fahrenheit= sensor.fahrenheit
        fahrenheit = round((fahrenheit), 2)
        fahrenheit = str(fahrenheit)
        return(fahrenheit)
    
    def get_humidity():
        humidity = sensor.humidity
        humidity = round((humidity), 2)
        humidity = str(humidity)
        return(humidity)
    
    def Time(self):
        now = datetime.datetime.now().strftime("%H:%M:%S")
        now = str(now)
        return(now)
    
    def Date(self):
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        today = str(today)
        return(today)
    
#     def get():
#         now = time_now()
#         today = date_now()
#     def get_sensor_data():
#         sensor = am2320_my_code.AM2320()
#         for x in range(1, 10000):
#             sensor_data = sensor
#             time.sleep(0.5)
#             sensor_rounded = round(sensor_data, 2)
#             sensor_str = str(sensor_rounded)
#             return(sensor_str)
#             
    def write_to_csv(self):
        
        file_name = ('/home/pi/Work_Files/Project/Data_files/sensor_data.csv')
        with open(file_name, mode = 'w') as sensor_readings:
            sensor_write = csv.writer(sensor_readings, delimiter = '|')
            write_to_log = sensor_write.writerow([Date(), Time(), get_ctemp(), get_ftemp(), get_humidity()])
            return(write_to_log)
        
    
#    