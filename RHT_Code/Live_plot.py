"""
=========================
Plotting data from a file
=========================

Plotting data from a file is actually a two-step process.

1. Interpreting the file and loading the data.
2. Creating the actual plot.

`.pyplot.plotfile` tried to do both at once. But each of the steps has so many
possible variations and parameters that it does not make sense to squeeze both
into a single function. Therefore, `.pyplot.plotfile` has been deprecated.

The recommended way of plotting data from a file is therefore to use dedicated
functions such as `numpy.loadtxt` or `pandas.read_csv` to read the data. These
are more powerful and faster. Then plot the obtained data using matplotlib.

Note that `pandas.DataFrame.plot` is a convenient wrapper around Matplotlib
to create simple plots.
"""
import datetime
import matplotlib
# matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

import numpy as np
import pandas as pd
from matplotlib.animation import FuncAnimation

###############################################################################
# Using pandas
# ============
# When working with dates, additionally call
# # `pandas.plotting.register_matplotlib_converters` and use the ``parse_dates``
# # argument of `pandas.read_csv`::
#

# Requesting for current time and date
my_date = datetime.datetime.now()
# 
# 
# #Formatting my Date and time
Date = datetime.date.strftime(my_date, "%m-%d-%Y")
Time = datetime.date.strftime(my_date, "%H:%M:%S%p")
filename = '/home/pi/Work_Files/Project/Data_files/sensor_data_{}.csv'.format(Date)

pd.plotting.register_matplotlib_converters()

sd_df = pd.read_csv(filename,
            index_col='Date',
            parse_dates=['Date'],
            infer_datetime_format=['Time'],
            header=0,
            names=['Date', 'Time', 'var_1','var_2', 'var_3'])
# debug
print(sd_df)


# Data Variables. Append values to keep graph dynamic
# Define data'
x = sd_df.iloc[:, 0].values
y1 = sd_df.iloc[:, 1].values
y2 = sd_df.iloc[:, 2].values
y3 = sd_df.iloc[:, 3].values

# Set up empty Figure, Axes and Line objects

fig, axs = plt.subplots(3, sharex=True)
                             
# Draw a blank line
line1, = axs[0].plot(x, y1, 'b')
line2, = axs[1].plot(x, y2, 'r')
line3, = axs[2].plot(x, y3, 'k')


def init():
    line1.set_data([], [])
    line2.set_data([], [])
    line3.set_data([], [])

    return line1, line2, line3



#Animation
# Define animate function
def animate(i):
    line1.set_data(x[0:i], y1[0:i])
    line2.set_data(x[0:i], y2[0:i])
    line3.set_data(x[0:i], y3[0:i])

    # Format plot
    axs[0].set_title('Daily Sensor Data')
    axs[0].set(ylabel='$f(t)=var_1$')
    axs[1].set(ylabel='$f(t)=var_2$')
    axs[2].set(ylabel='$f(t)=var_3$')
    fig.autofmt_xdate(rotation=45)

    return line1, line2, line3


# Pass to FuncAnimation
# update every 30ms
sd_anim = FuncAnimation(fig, animate, init_func=init, interval=30, blit=True)
plt.show()
# Save in the data directory,
#sd_anim.save('data/sd_animated.gif')



