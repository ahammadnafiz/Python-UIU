# timeproperties.py
'''Class time with read-write properties'''

class Time:
    """Class Time with read-write properties
    """
    
    def __init__(self, hour=0, minute=0, second=0) -> None:
        """Initialize each attribute
        """
        
        self.hour = hour
        self.minute =  minute
        self.second = second
    
    @property
    def hour(self):

        return  self._hour
    
    @hour.setter
    def hour(self, hour):
        
        if not (0 <= hour < 24):
            raise ValueError(f"Hour {hour} must be 0-23")
        
        self._hour = hour
    
    @property
    def minute(self):
        return self._minute
    
    @minute.setter
    def minute(self, minute):
        self._minute = minute
    
    @property
    def second(self):
        return self._second
    
    @second.setter
    def second(self, second):
        self._second = second
        
    def set_time(self, hour = 0, minute = 0, second = 0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __repr__(self) -> str:
        return (f'Time(hour={self.hour}, minute={self.minute}, ' + f'second={self.second})')

time = Time(12,15,30)
print(time)
time.second = 0
print(time)