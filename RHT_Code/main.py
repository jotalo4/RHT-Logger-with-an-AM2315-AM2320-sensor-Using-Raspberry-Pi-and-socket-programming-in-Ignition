#this is the main class in the app. 
#It extends the tkinker Frame.
#It manages unser interface, timer, logging data to file, and it reads data from sensors over I2C

from random import randint
from chart import *
from bme280pi.sensor import Sensor
from perpetualTimer import perpetualTimer
from Environmental_data_logger import Environmental_data_logger
import os.path
import am2320_my_code

class THP_Logger(Frame):

    def __init__(self, title, master=None):
        Frame.__init__(self, master )
        self.grid(row = 50, column = 50, sticky = W)
        self.master.title(title)
        self.label = Label(self, text='Hello')
        self.createWidgets()
        self.Measurment_number =0
        self.isLogToFile=False
        self.LogIntervalSconds=10
        self.form_base_title = "Smithfield TH Logger"
        self.winfo_toplevel().title(self.form_base_title)
        self.data_logger = Environmental_data_logger(file_path="log.csv")


    def createWidgets(self):
        padding =5
        
        #Instantiation of the temperature chart on the main form 
        self.chrtTemperature = Chart(self,bg="white" , width=1000, height=200)
        self.chrtTemperature.set_title("Temperature (C)")
        self.chrtTemperature.set_number_of_data_point(1000)
        self.chrtTemperature.grid(row=1, column=1, columnspan=10 ,padx=padding , pady=padding)
        self.chrtTemperature.draw()

        #Instantiation of the humidity chart on the main form
        self.chrtHumidity = Chart(self, bg="white", width=1000, height=200)
        self.chrtHumidity.set_title("Relative Humidity (%)")
        self.chrtHumidity.set_number_of_data_point(1000)
        self.chrtHumidity.grid(row=3, column=1,columnspan=10 ,padx=padding , pady=padding)
        self.chrtHumidity.draw()

        #Instantiation of the temperature chart in fahrenheit on the main form
        self.chrtFahrenheit = Chart(self, bg="white", width=1000, height=200)
        self.chrtFahrenheit.set_title("Temperature (F)")
        self.chrtFahrenheit.set_number_of_data_point(1000)
        self.chrtFahrenheit.grid(row=5, column=1 , columnspan=10 ,padx=padding , pady=padding)
        self.chrtFahrenheit.draw()

        #Instantiation of the start/stop button
        self.btnStartStop = Button(self , text="Start" , command=self.__btnStartStop_clicked)
        self.btnStartStop.grid(row=0, column=1)

        #Instantiation of the exit button 
        self.btnExit = Button(self, text="Exit" )
        self.btnExit.bind("<Button-1>", self.__btnExit_clicked)
        self.btnExit.grid(row=0, column=2)

        #Instantiation of the clear button 
        self.btnClear = Button(self, text="Clear" )
        self.btnClear.bind("<Button-1>", self.__btnClear_clicked)
        self.btnClear.grid(row=0, column=3)

        #Instantiation of the log to file button, it is also used to disable looging to file
        self.btnLogToFile = Button(self, text="Enable Logging")
        self.btnLogToFile.bind("<Button-1>", self.__btnLogToFile_clicked)
        self.btnLogToFile.grid(row=0, column=4)

        #Instantiation Label 
        self.lblLogInterval= Label(self, text="Interval(S)")
        self.lblLogInterval.grid(row=0, column=5)

        #Instantiation of the spinbox that provides a selection of measurment intervals in seconds
        self.spnLogInterval = Spinbox(self, values=(5,10,20,40,60,90,120,300,600))
        self.spnLogInterval.grid(row=0, column=6)


    def __btnLogToFile_clicked(self, event):
        print("log to file clicked")
        if self.btnLogToFile['text'] == "Enable Logging":
            self.btnLogToFile['text'] = "Disable Logging"
            self.isLogToFile= True
        else:
            self.isLogToFile = False
            self.btnLogToFile['text'] = "Enable Logging"


    def __btnClear_clicked(self , event):

        #clear all the charts from data
        self.chrtTemperature.clear_data()
        self.chrtHumidity.clear_data()
        self.chrtFahrenheit.clear_data()


    def __btnStartStop_clicked(self):
        if self.btnStartStop['text']=="Start":
            self.btnStartStop['text']="Stop"
            self.__start_acquiring()

        else:
            self.btnStartStop['text']="Start"
            self.__stop_acquiring()


    def __start_acquiring(self):
        self.log_entry_index =0
        self.LogIntervalSconds = int(self.spnLogInterval.get())
        self.__t = perpetualTimer(self.LogIntervalSconds , self.timer_call_back)
        self.__t.start()
        self.btnLogToFile.config(state=DISABLED)
        self.spnLogInterval.config(state=DISABLED)
        if self.isLogToFile == True:
            self.log_file_path = self.get_log_file_name()
            self.data_logger = Environmental_data_logger( file_path = self.log_file_path)
            title = "%s , logging data into file: %s" %( self.form_base_title , self.log_file_path)
            self.winfo_toplevel().title(title)
        #run the call back function once, it will later on be called by the timer.
        self.timer_call_back()

    def __stop_acquiring(self):
        self.__t.cancel()
        self.btnLogToFile.config(state=NORMAL)
        self.spnLogInterval.config(state=NORMAL)
        self.winfo_toplevel().title(self.form_base_title)

    def __btnExit_clicked(self , event):
        try:
            self.__t.cancel()
        except:
            print("exiting")

        print("exiting")
        self.destroy()
        exit()


    #this function is executed by a timer, repeatably, it reads data displays it and log it to file is needed
    def timer_call_back(self):

        #incremenat the index
        self.Measurment_number+=1
        x=self.Measurment_number

        #get the data from rando number generator if you are debugging the program
        #_temperature =randint(27, 31)
        #_humidity =randint(31, 42)
        #_pressure =randint(31, 32)

        #get real data from the sensors over I2C bus
        (temperature, fahrenheit,  humidity) = am2320_my_code.AM2320()
        sensor.temperature = temperature, sensor.humidity = humidity, sensor.fahrenheit = fahrenheit

        #update user interface
        self.chrtTemperature.add_point(x, temperature)
        self.chrtFahrenheit.add_point(x, fahrenheit)
        self.chrtHumidity.add_point(x, humidity)
        

        #log data to csv file if logging is enabled
        if self.isLogToFile:
            _index = self.log_entry_index
            self.data_logger.log(entry_index, temperature, fahrenheit, humidity)

        # increments the index to reflect seconds since start of acquisition
        self.log_entry_index+=self.LogIntervalSconds

    
    #this function gererates the csv log file name, it finds a file name that doesn't already exist. 
    def get_log_file_name(self):

        i = 1
        file_path_stem = "log_file"
        file_path = "%s_%s_.csv" %( file_path_stem , str(i))
        while os.path.isfile(str(file_path)):
            i+=1
            file_path = "%s_%s_.csv" % (file_path_stem, str(i))

        return file_path


#running the program starts here, main entry point
if __name__ == '__main__':
    root = THP_Logger(title="Main Form" )
    root.createWidgets()
    root.mainloop()


