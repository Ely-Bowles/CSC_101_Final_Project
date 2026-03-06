import Data
from Classes import Time
cycles = [Data.cycle21_obj, Data.cycle22_obj, Data.cycle23_obj]

# #################################################################
# #function should be given a year and should return a cycle number
# def year(age:Time)->int:
#     year_start=1979
#     current_cycle=0
#     if age.year>=1979:
#         current_cycle=
#     return current_cycle
#
# input1=2020,3
# test= year(1986)
# print(test)
#
#
# #number of sunspots
# def sunspots(month:int)->int:
#
#
# #area of sunspots in month



# print(Data.cycle22_obj.years[1989].months["May"].avg_sunspots)

print("\n","Interested in a polar flight but worried about radiation? Eger to learn about the solar cycle?") #just talk

print("What would you like to know?")                                                               #just talk
l1 = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]           #list of months to check later
while True:
    initial=input("input: (polar flight) or (solar cycle)  :")                                      #a choice to pick one or the other within a loop
    if initial == "polar flight":
        break
    elif initial == "solar cycle":
        break
    else:
        print("Error 1: please input polar flight or solar cycle")


Time_years = 0
Time_months = 0
if initial == "polar flight":
    while True:
        try:
            Time_years = int(input("input the year"))
            Time_months = input("input month of year")
            if Time_months in l1 and Time_years >= 1976 and Time_years <= 2028:
                break
            else:
                print("Error 2:Month must be one of the 12 calendar months and Year must be between 1976 and 2028. Try again ")
        except ValueError:(
                    print("Error 3: Not a valid input. Please try again"))


    if Time_months in l1 and Time_years >= 1976 and Time_years <= 2028:
        print("remove this its just for example")

    else:
        print("Error 4:Month must be one of the 12 calendar months and Year must be between 1976 and 2028. Try again ")







if initial == "solar cycle":
    try:
        sunspot_y=int(input("input the year of inquiry between 1976 and 2028 :"))
        sunspot_m= input("input month of year, Jan-Dec  :")
        if sunspot_m in l1 and sunspot_y >= 1976 and sunspot_y <= 2008:           #read data already given
            for cycle in cycles:
                if sunspot_y in cycle.years:
                    print("\n")
                    print("The solar cycle is an approximately 11-year cycle of magnetic activity in the Sun,during which its stormy behavior builds to a maximum,","\n","its magnetic poles reverse, and it settles back to a minimum","\n")
                    print("Average sunspots in", sunspot_m,sunspot_y, "=", cycle.years[sunspot_y].months[sunspot_m].avg_sunspots,"\n")
                    print("Radiation storm count in", sunspot_m,sunspot_y, "=", cycle.years[sunspot_y].months[sunspot_m].storm_count,"\n")
                    print("Radiation storm max severity in", sunspot_m, sunspot_y, "=", cycle.years[sunspot_y].months[sunspot_m].max_severity,"\n")

                    print("percent of solar cycle completed", sunspot_y-cycle.start_date*12+month_index/total_months*12*100)



        elif sunspot_m in l1 and sunspot_y > 2008 and sunspot_y <= 2028:             #predect values
            print("remove me")

        else:
            print("Error 5: Month must be one of the 12 calendar months and Year must be between 1976 and 2028. Try again ")
    except ValueError:
        print("Error 6:Not a valid input. Please try again")






