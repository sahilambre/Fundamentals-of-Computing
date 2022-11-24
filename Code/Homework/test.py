# def shortStrings(L, n):
#     # x = len(L)
#     # return x
#     s = list(filter(lambda s: len(x) > s))
#     return s

# L = ['sahil', 'sahi', 'sah', 'sa', 's']
# n = 4


# print(shortStrings("sahasil"))


def doubleStrings(L):
    s = list(map(lambda k: k * 2, L))
    return s


L = ['aa', 'a', 'bbb']
print(doubleStrings(L))

def shortStrings(L, n):
    s = list(filter(lambda k: len(k) < n, L))
    return s

L = ['sahil', 'sahi', 'sah', 'sa', 's']
n = 3
print(shortStrings(L, n))


def pigLatin(s):
    first_char = s[0]
    remaining_string = s[1::]
    z = remaining_string + first_char + "ay"
    # u = "ay"
    #r = z.append(["ay"])
    #return z
    #print(z, Str(u))
    #print(list(z))
    return list(z)

print(pigLatin("Hello"))
print(pigLatin("Sahil"))

# 2b: Souble Strings 

def doubleString(L):
    return L + L

initial_string = ('a', 'aa', 'bbb')
doubled_string = map(doubleString, initial_string)
print(list(doubled_string))



#* HW4

# Sahil Mukesh Ambre
# CWID: 20015751


class Time:
    def __init__(self, hour, minute):
        assert (minute >= 0 and minute <= 59) and (hour >= 0 and hour <= 23), 'Invalid input'
        self.hour = hour
        self.minute = minute

    # Question 1: Verify the constructor and string methods work

    def __str__(self):
        self.minute = str(self.minute)
        self.hour = str(self.hour)

        if len(self.minute) == 1:
            self.minute = "0" + self.minute
        
        if len(self.hour) == 1:
            self.hour = "0" + self.hour

        formatted_string = str(self.hour) + ":" + str(self.minute)

        return formatted_string

    # Question 2: Create the equal operator 

    def __eq__(self,other):
        if other.minute == self.minute and other.hour == self.hour:
            return True
        else:
            return False

    # Question 3: Write an after noon function

    def isAfterNoon(self):
        if (self.hour > 12 and self.hour < 24) and (self.minute > 0 and self.minute < 60):
            return True
        else:
            return False

    # Question 4: Write a before function

    def isBefore(self, d2):
        if self.hour < d2.hour:
            return True
        if d2.hour == self.hour:
            if self.minute < d2.minute:
                return True
            else:
                return False
        else:
            return False

    # Question 5: Write a tick function

    def tick(self):
        if (self.minute == 59):
            self.hour += 1
        self.minute += 1
        
    # Question 6: Create a time apart function

    def longTimeApart(self, other):
       if self.hour > other.hour:
           return Time(self.hour - other.hour, self.minute - other.minute)
       else:
           return Time(other.hour - self.hour, other.minute - self.minute)

    # Question 7: Create a different time apart function

    def shortTimeApart(self, other):
       if self.hour > other.hour:
           return Time(23 - self.hour + other.hour, 60 - self.minute + other.minute)
       else:
           return Time(23 - other.hour + self.hour, 60 - other.minute + self.minute)




