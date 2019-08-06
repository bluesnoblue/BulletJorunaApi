import time
import datetime
from datetime import timedelta


def get_day_start_timestamp(now_time):
    time_stamp = now_time
    time_array = time.localtime(time_stamp)
    zero_time = time.strftime("%Y-%m-%d 00:00:00", time_array)
    time_array_ex = time.strptime(zero_time, "%Y-%m-%d %H:%M:%S")
    return int(time.mktime(time_array_ex))


def get_day_end_timestamp(now_time):
    time_stamp = now_time
    time_array = time.localtime(time_stamp)
    zero_time = time.strftime("%Y-%m-%d 23:59:59", time_array)
    time_array_ex = time.strptime(zero_time, "%Y-%m-%d %H:%M:%S")
    return int(time.mktime(time_array_ex))


def get_week_start_timestamp(now_time):
    time_stamp = now_time
    now_datetime = datetime.datetime.fromtimestamp(time_stamp)
    monday = now_datetime - timedelta(days=now_datetime.weekday())
    monday_time = int(time.mktime(monday.timetuple()))
    return get_day_start_timestamp(monday_time)


def get_month_start_timestamp(now_time):
    time_stamp = now_time
    time_array = time.localtime(time_stamp)
    zero_time = time.strftime("%Y-%m-1 00:00:00", time_array)
    time_array_ex = time.strptime(zero_time, "%Y-%m-%d %H:%M:%S")
    return int(time.mktime(time_array_ex))


def get_year_start_timestamp(now_time):
    time_stamp = now_time
    time_array = time.localtime(time_stamp)
    zero_time = time.strftime("%Y-1-1 00:00:00", time_array)
    time_array_ex = time.strptime(zero_time, "%Y-%m-%d %H:%M:%S")
    return int(time.mktime(time_array_ex))


if __name__ == '__main__':
    pass

