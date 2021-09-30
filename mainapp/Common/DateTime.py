from datetime import datetime
import pytz
import time

def get_current_YmdHMS():
    """
    Get current time format yyyy/MM/dd hh:mm:ss
    trunganhvu 2021/08/29
    """
    tz_NY = pytz.timezone('Asia/Saigon')
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
def get_current_microsecond():
    """
    Get current time format yyyy + Microsecond
    trunganhvu 2021/08/29
    """
    tz_NY = pytz.timezone('Asia/Saigon')
    date = datetime.now()
    year = date.year
    day_of_year = date.timetuple().tm_yday
    microsecond = date.microsecond
    return str(year) + str(day_of_year) + str(microsecond) 

def current_milli_time():
    return round(time.time() * 1000)
