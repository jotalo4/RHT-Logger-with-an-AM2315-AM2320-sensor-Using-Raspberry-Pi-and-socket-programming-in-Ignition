import csv
import time
import datetime

filename = '/home/pi/Work_Files/Project/Data_files/sensor_data.csv'
file_name = '/home/pi/Work_Files/Project/Data_files/readabledata.csv'
fields = ("Temperature(C), Temperature(F), Relative Humidity (%)" + " \n")

with open(filename, mode = 'w') as ouput:
    with open(file_name) as csv_file:
         output_data = csv.writer(ouput, delimiter = ',')
         data = csv.reader(csv_file, delimiter = ',')
         line_count == 0
         
         for row in data:
             print(type(row))
             if line_count == 0:
                 print("The values are %s"%(row))
                 output_data.writerow(row)
                 line_count += 1
             else:
                 print("The values are %s"%(row))
                 output_data.writerow(row)
                 line_count += 1

        print("The number of rows processed is %d"%(line_count))

reading_time = datetime.datetime.now()
fahrenheit = sensor.fahrenheit
humidity = sensor.humidity
temperature = sensor.temperature
x = f.writerow([reading_time, temperature, fahrenheit, humidity])
