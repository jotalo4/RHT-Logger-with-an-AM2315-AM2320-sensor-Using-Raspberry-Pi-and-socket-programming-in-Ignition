#matplotlib notebook

from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from random import randrange
from threading import Thread
import time
import matplotlib
import matplotlib.pyplot as plt

# Creating plot for the temperature Chart
fig = plt.figure()

#     # Draw Plot of selected datapoint
#     ax1 = axs.plot([time_new, get_ctemp()] , "-b", label = "Celsius") 
#     ax2 = axs.plot([time_new, get_ftemp()] , "-r", label = "fahrenheit")

data = np.genfromtxt("sensor_data.csv", delimiter=",", names=["time", "date", "celsius", "fahrenheit", "relative humidity"


# t, d, c, f, and h represents time, date, celsius, fahrenheit and relative humidity
#plt.plot(data)

# Clear Plot

# Layout Design
plt.tight_layout()

# PLot real time data
plt.plot(t, c, "-b", label = "Celsius")
plt.plot(t, f, "-r", label = "Fahrenheit")
plt.plot(t, h, "-bg", label = "Humidity")

# Configuring the plot
plt_configure(xlabel = 'Current Time', ylabel = 'Temperature Readings', title = 'Temperature Graph', legend = {'loc': 'upper right'}, grid = 'True')
plt_configure(xlabel = 'Current Time', ylabel = 'Fahrenheit Readings', title = 'Fahrenheit Graph', legend = {'loc': 'upper right'}, grid = 'True')
plt_configure(xlabel = 'Current Time', ylabel = 'Humidity Readings', title = 'Humidity Graph', legend = {'loc': 'upper right'}, grid = 'True')
 
 # # Draw the graph
plt.show()

    
     # axs.savefig("data.png")

    
  

#     # Creating plot for the Relative Humidity Chart
#     fig, ax  = plt.subplots(1,1)
#     # Draw Plot of selected datapoint
#     ax3 = ax.plot([time_new, get_humidity()] , "-b", label = "Celsius") 
#     ax.grid(True)
#     fig.suptitle('Relative Humidity Graph')
#     ax.set_xlabel('Current Time')
#     ax.set_ylabel('HUmidity Readings')


# # Format Plot for first Subplot
#  plt.xticks(rotation=45, ha='center')
#  plt.subplots_adjust(bottom=0.30)
 
