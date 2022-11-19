# Sahil Mukesh Ambre
#CWID: 20015751



class Date:
    def __init__(self, month, day, year):
        #assert (month > 0 and month < 13) and (day > 0 and day < 32) and (year > 1900 and year < 3000)
        self.month = month
        self.day = day
        self.year = year

    # Question 1: Verify the constructor and string methods work

    def __str__(self):
        
        self.day = str(self.day)
        self.month = str(self.month)
       
        if len(self.day) == 1:
            self.day = '0' + self.day

        if len(self.month) == 1:
            self.month = '0' + self.month

        formatted = str(self.month) + '/' + str(self.day) + '/' + str(self.year)
        
        return formatted

    # Question 2: Create the equal operator

    def __eq__(self, other):
    
        if other.month == self.month and other.year == self.year and other.day == self.day:
            return True
        else:
            return False

    # Question 3: Write a leap year function

    def isLeapYear(self):
        if self.year % 100 != 0 and self.year % 4 == 0:
            return True
        
        if self.year % 100 == 0 and self.year % 400 == 0:
            return True
        else:
            return False

    # Question 4: Write a before function

    def isBefore(self, d2):
        if self.year < d2.year:
            return True
        if d2.year == self.year:
            if self.month < d2.month:
                return True
            if d2.month == self.month:
                if self.day < d2.day:
                    return True
                else:
                   return False
            else:
                return False
        
        else:
            return False


    # Question 5: Create a days apart function

    def daysApart(self, other):
        a = self.year - other.year
        b = a * 365.25

        c = 12 - other.month
        d = other.month - 1

        e = c + d

        f = 365.25 // 12 * e

        ans = b + f 

        return ans













# input = Date(1,2,2000)
# print(input.isLeapYear())

# d1 = Date(1, 1, 2000)
# d2 = Date(1, 1, 2001)

# print(d1 == d2)

# d1 = Date(2,1,2000)
# d2 = Date(1,1,2000)
# print(d1.isBefore(d2))