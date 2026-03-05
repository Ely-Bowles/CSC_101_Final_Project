import Data
from Classes import Time

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

print("Interested in a polar flight but worried about radiation? Eger to learn about the solar cycle?")

print("What would you like to know?")
l1 = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
while True:
    initial=input("input: (polar flight) or (solar cycle)  :")
    if initial == "polar flight":
        break
    elif initial == "solar cycle":
        break
    else:
        print("please input polar flight or solar cycle")




if initial == "polar flight":
    while True:
        Time_years = input("input the year")
        Time_months = input("input month of year")
        try:
            int(Time_years)
            if Time_months in l1:
                print("45")
            else:
                print()
        except:
            print("Not a valid input.Year must be between 1976 and 2028. Month must be one of the 12 calendar months. Please try again")








if initial == "solar cycle":
    sunspot_y=input("input the year of inqury between 1997 and 2019:")
    sunspot_m= input("input month of year, Jan-Dec")



