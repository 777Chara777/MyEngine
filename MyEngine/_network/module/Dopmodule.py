
class TimeFormat:
    def __init__(self, value: int) -> None:
        def time(sec: int):

            minute = sec // 60
            hour = minute // 60
            day = hour // 24

            sec = sec % 60
            minute = minute % 60
            hour = hour % 24
                
            return (day, hour, minute, sec)
        
        self.value = time(int(value))
    
    def __str__(self) -> str:
        return "<TimeFormat {day=%s, hour=%2d, min=%2d, sec=%2d}>" % self.value

    def get_time(self) -> tuple:
        return self.value
    
    def day(self) -> int:
        return self.value[0]
    
    def hour(self) -> int:
        return self.value[1]
    
    def min(self) -> int:
        return self.value[2]

    def sec(self) -> int:
        return self.value[3]
    