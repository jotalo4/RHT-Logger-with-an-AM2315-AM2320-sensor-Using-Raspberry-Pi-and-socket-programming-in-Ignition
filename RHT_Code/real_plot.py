import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation 
from itertools import count
from matplotlib.figure import Figure

global anim


 
 # Creating the animation Method
def animate(i):
    
    filename = '/home/pi/Work_Files/Project/Data_files/sensor_data.csv'
    data_read = open(filename)
        
        
    Date = list()
    Time = list()
    ct = get_ctemp() 
    ft = get_ftemp()  
    humi = get_humidity() 
    
    
    for line in data_read:
        row = line.split(',')
        Date_now = row[0]
        time_now = row[1]
        temperature_now = row[2]
        fahrenheit_now = row[3]
        humidity_now = row[4]
        
        date_new = datetime.date.strftime(my_date, "%b %d %Y")
        time_new = datetime.date.strftime(my_date, "%H:%M")
        
 # Data Variables. Append values to keep graph dynamic
        try:
            Date.append(Date_now)
            Time.append(time_now)
            ct.append(float(temperature_now))
            ft.append(float(fahrenheit_now))
            humi.append(float(humidity_now))
        except:
            print("don't know")
     
        
        # Create a figure
        fig = plt.figure()  
        plt.style.use('fivethirtyeight')

        fig.add_subplot(3,1,1)
        plt.plot(Time, ct, 'bo', label = "Celsius")
        plt.ylabel("Temperature readings"), plt.title("Temperature Graph")
        plt.legend()

        fig.add_subplot(3,1,2)
        plt.plot(Time, ft, 'g-', label = "Fahrenheit")
        plt.ylabel("Fahrenheit readings"), plt.title("Fahrenheit Graph")
        plt.legend()

        fig.add_subplot(3,1,3)
        plt.plot(Time, humi, 'r-', label = "Humidity")
        plt.xlabel("Current Time"), plt.ylabel("Humidity readings"), plt.title("Humidity Graph")
        plt.legend()
        
    anim = FuncAnimation(fig, animate, interval=1000, blit=True)
    
plt.show()
   
 