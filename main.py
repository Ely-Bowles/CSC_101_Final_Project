#function should be given a year and should retuen a cycle number
def year(Year:int)->int:
    year_start=1979
    current_cycle=0
    if Year>=1979:
        current_cycle=(Year-year_start)//11
    return current_cycle


input1=2020,3
test= year(1986)
print(test)



#number of sunspots
def sunspots(mounth:int)->int:




#area of susnpots in mounth