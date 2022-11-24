# Sahil Mukesh Ambre
# CWID: 20015751


class Time:
    def __init__(self, hour, minute):
        """
        Args:
            
        Hour :     An attributer holding the hour in 24 hour clock format.
        minute :   An attribute holding minute.
        """
        assert (0 <= minute <= 59) and (0 <= hour <= 23),'Invalid Input'
        self.hour = hour
        self.minute = minute

    # Question 1: Verify the constructor and string methods work

    def __str__(self):
        """
        Returns:    Return a string with the hour and minute, 
                    formatted nicely to have exactly two digits places for the
                    hour and two digit places for the minute.
        """
        temp_min = str(self.minute)
        temp_hour = str(self.hour)

        if len(temp_min) == 1:
            temp_min = "0" + temp_min

        if len(temp_hour) == 1:
            temp_hour = "0" + temp_hour

        formatted_string = str(temp_hour) + ":" + str(temp_min)

        return formatted_string

    # Question 2: Create the equal operator 

    def __eq__(self, other):
        """
        Args:
            
        other :     Takes two parameters, hours and minutes and compares.

        Returns:    True or False depending upon the situation.
        """
        if other.minute == self.minute and other.hour == self.hour:
            return True
        else:
            return False

    # Question 3: Write an after noon function

    def isAfterNoon(self):
        """
        Returns:    True or False 
        """
        if (12 < self.hour < 24) and (0 < self.minute < 60):
            return True
        else:
            return False

    # Question 4: Write a before function

    def isBefore(self, d2):
        """
        Args:
        
        d2 :    Takes two parameters, hours and minutes and compares.

        Returns: True or False
        """
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
        """
        returns nothing but add one minute to the current time
        """
        if self.minute == 59 and self.hour < 23:
            self.hour += 1
            self.minute = 0
        elif self.minute == 59 and self.hour == 23:
            self.hour = 0
            self.minute = 0
        else:
            self.minute += 1

    # Question 6: Create a time apart function

    def shortTimeApart(self, other):
        """
        Args:
        other :     Takes two parameters, hours and minutes and compares.

        Returns:    The shorter amount of time between the calling object and other in a new Time object
        """
        #if self.hour >= other.hour:
        if other.hour < self.hour: 
            return Time(23 - self.hour + other.hour, 60 - self.minute + other.minute)
        else:
            #*
            return Time(23 - other.hour + self.hour, 60 - other.minute + self.minute)

    # Question 7: Create a different time apart function

    def longTimeApart(self, other):
        """
        Args:
        other :     Takes two parameters, hours and minutes and compares.

        Returns:    The longer amount of time between the calling object and other in a new Time object
        """
        if self.hour > other.hour:
            return Time(self.hour - other.hour, self.minute - other.minute)
        else:
            return Time(other.hour - self.hour, other.minute - self.minute)



