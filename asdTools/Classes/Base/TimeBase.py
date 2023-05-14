from datetime import datetime
import time


class TimeBase():
    def __init__(self, **kwargs) -> None:
        pass

    @staticmethod
    def get_time(forFile:bool=False, timestamp:float=-1) -> str:
        if timestamp == -1:
            time = datetime.now()
        else:
            time = datetime.fromtimestamp(0)
        if forFile:
            time = time.strftime(f"%Y-%m-%d_%H-%M-%S")
        else:
            time = time.strftime(f"%Y-%m-%d %H:%M:%S")
        return time

    @staticmethod
    def get_timestamp(time:datetime=None) -> float:
        # wait for improvement
        if time == None:
            time = datetime.now()
        timestamp = time.timestamp()
        return timestamp

    @staticmethod
    def get_time_diff(time1:str, time2:str) -> float:
        time_formats = ("%Y-%m-%d_%H-%M-%S", 
                        "%Y-%m-%d %H:%M:%S")
        for time_format in time_formats:
            try:
                time1 = datetime.strptime(time1, time_format)
                time2 = datetime.strptime(time2, time_format)
                time_diff = time2 - time1
                time_diff = time_diff.total_seconds()
                return time_diff
            except ValueError:
                pass
        raise ValueError("Invalid time format")

    @staticmethod
    def sleep(time_sleep):
        time.sleep(time_sleep)