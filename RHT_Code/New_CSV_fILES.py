import pandas as pd
import datetime
from dateutil.relativedelta import relativedelta
from random import randint
import os
import stat
import shutil


INCOMING = '/home/pi/Work_Files/Project/Data_files'
PROCESSED = '/home/pi/Work_Files/Project/Data_files/processed/files/'
TIME_WITH_NO_WRITES = 600  # 10 minutes


def check_for_new_file(directory=INCOMING, Data_files={}):
    for file in os.listdir(directory):
        if file in Data_files:
            break
        size = os.stat(file)[stat.ST_SIZE]
        Data_files[file] = (datetime.time.now(), size)
    now = datetime.datetime.now()
    for file, last_time, last_size in files.items():
        current_size = os.stat(file)[stat.ST_SIZE]
        if current_size != last_size:
            files[file] = (now, current_size)
            continue
        if now - last_time <= TIME_WITH_NO_WRITES:
            return file
    raise NoneReady()



def process_new_file():
    try:
        filename = check_for_new_file()   # raises ValueError if no file ready
    except NoneReady:
        return
    in_file = open(filename, 'rb')
    csv_file_in = csv.reader(in_file)
    out_file = open(MASTER_CSV, 'rb+')
    csv_file_out = csv.writer(out_file)
    for row in csv_file_in:
        csv_file_out.write(row)
    csv_file_out.close()
    csv_file_in.close()
    shutil.move(filename, PROCESSED)