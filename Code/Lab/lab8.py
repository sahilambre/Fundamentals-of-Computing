'''
#Define a Time class, and make a constructor which takes in
#Hours and minutes
#If hours < 0 or hours > 23 -> AssertionError
#If minutes < 0 or minutes > 59 -> AssertionError
#And a str function which prints the time in the format HH:MM in 24 hour format
#Please name the attributes hours and minutes, for hours and minutes respectively
#EX: t = Time(11,23)
#print(t) -> 11:23
#t2 = Time(23,51)
#print(t2) -> 23:51
#t3 = Time(1,41)
#print(t3) -> 01:41a

'''
# Sahil Mukesh Ambre
class Time:
    def __init__(self, hours, minutes):
        assert (hours > 0 and hours < 24) and ( minutes > 0 and minutes < 59)
        #assert (h < 0 or h > 23) or ( m > 0 or m < 59)
        self.hours = hours
        self.minutes = minutes

    def __str__(self):
        if self.hours < 10 and self.minutes > 10:
            return f'0{self.hours}:{self.minutes}'
        if self.minutes < 10 and self.hours > 10:
            return f'0{self.hours}:0{self.minutes}'
        if self.minutes < 10 and self.hours < 10:
            return f'0{self.hours}:{self.minutes}'
        return f'{self.hours}:{self.minutes}'

s = Time(11,23)
r = Time(23,51)
q = Time(1,41)
# print(s)
# print(r)
print(q)