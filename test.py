from enum import Enum
class day(Enum):
    day1=1
    @property
    def others(self):
        return day.day1

print(day.others)
