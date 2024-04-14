import copy
class Date:
    def __init__(self,day,month,year):
        self.day=day
        self.month=month
        self.year=year
    def __str__(self):
        return f"{self.day}/{self.month}/{self.year}"
    def copy(self):
        return copy.deepcopy(self)
class Period:
    def __init__(self,start,end):
        self.start = start.copy()
        self.end=end.copy()
    def __str__(self):
        return f"{self.start}-{self.end}"
d1 = Date(31,1,2024)
d2 = Date(31,5,2024)
p = Period(d1,d2)
d1.year=2025
print()
print(p)
