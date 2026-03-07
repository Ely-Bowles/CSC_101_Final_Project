

# Class assigns the year and month for user input to run through program
class Time:
    def __init__(self,year,month):
        self.year = year
        self.month = month

    def __repr__(self):
        return "Time({}, {})".format(self.year, self.month)
    def __eq__(self,other):
        return (self.year,self.month) == (other.year,other.month)



