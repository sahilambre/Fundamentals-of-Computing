# Sahil Mukesh Ambre
# CWID: 20015751


class Time:
    def __init__(self, hour, minute):
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
        pass

    # Question 4: Write a before function


    # Question 5: Write a tick function


    # Question 6: Create a time apart function


    # Question 7: Create a different time apart function

  
# t1 = Time(1,1)
# t2 = Time(1,1)
# t3 = Time(1,2)
# print(t1 == t2)
# print(t2 == t3)
# print(t1)


