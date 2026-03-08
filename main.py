import Data
from Classes import Time

cycles = [Data.cycle21_obj, Data.cycle22_obj, Data.cycle23_obj]

###################################################################

def find_percent(v:int)->Time:
        for y in cycle.years:
            for m in cycle.years[y].months:
                fun=(((y-cycle.start_date)*12)+(Data.month_order[m]-1))/(cycle.duration_years * 12) * 100
                if abs(fun - v) <= .5:
                    return Time(y,m)





print("\n")
print("Interested in a polar flight but worried about radiation? Eger to learn about the solar cycle?")  # just talk

print("What would you like to know?")  # just talk
l1 = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov",
      "Dec"]  # list of months to check later
while True:
    initial = input("input: (polar flight) or (solar cycle):")  # a choice to pick one or the other within a loop
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
            if Time_months in l1 and Time_years >= 1976 and Time_years <= 2030:
                break
            else:
                print(
                    "Error 2:Month must be one of the 12 calendar months and Year must be between 1976 and 2030. Try again ")
        except ValueError:
            (
                print("Error 3: Not a valid input. Please try again"))



if initial == "solar cycle":
    while True:
        try:
            sunspot_y = int(input("input the year of inquiry between 1976 and 2030:"))
            sunspot_m = input("input month of year, Jan-Dec:")
            if sunspot_m in l1 and sunspot_y >= 1976 and sunspot_y <= 2008:  # read data already given
                for cycle in cycles:
                    if sunspot_y in cycle.years:
                        print("\n")
                        print(
                            "The solar cycle is an approximately 11-year cycle of magnetic activity in the Sun,during which its stormy behavior builds to a maximum,",
                            "\n", "its magnetic poles reverse, and it settles back to a minimum.", "\n")
                        print("cycle:", cycle.cycle_number)
                        print("Average sunspots in", sunspot_m, sunspot_y, "=",
                              cycle.years[sunspot_y].months[sunspot_m].avg_sunspots)
                        print("Radiation storm count in", sunspot_m, sunspot_y, "=",
                              cycle.years[sunspot_y].months[sunspot_m].storm_count)
                        print("Radiation storm max severity in", sunspot_m, sunspot_y, "=",
                              cycle.years[sunspot_y].months[sunspot_m].max_severity)
                        print("percent of solar cycle completed",
                              round((((sunspot_y - cycle.start_date) * 12) + (Data.month_order[sunspot_m] - 1)) / (
                                      cycle.duration_years * 12) * 100,2))
                        While_l = input("want to try another time?")
                        while True:
                            if While_l == "no":
                                break
                            elif While_l == "yes":
                                break
                            else:
                                print("Invalid input. Please input yes or no")
                                While_l = input("want to try another time?")
                        if While_l == "no":
                            break
                if While_l == "no":
                    break

            elif sunspot_m in l1 and sunspot_y > 2008 and sunspot_y <= 2030:  # predict values
                c_year = (sunspot_y - 2009) // 11 + 24
                print("The solar cycle is an approximately 11-year cycle of magnetic activity in the Sun,during which its stormy behavior builds to a maximum,",
                    "\n", "its magnetic poles reverse, and it settles back to a minimum.", "\n")
                print("cycle:", c_year)
                y_start = 2009 + 11 * (c_year - 24)
                print("percent of solar cycle completed",
                      round((((sunspot_y - y_start) * 12) + (Data.month_order[sunspot_m] - 1)) / (11 * 12) * 100,2))

                avg_sp = 0
                avg_storms=0
                for cycle in cycles:
                    def1=round((((sunspot_y - (2009 + 11 * (((sunspot_y - 2009) // 11 + 24) - 24))) * 12) + (Data.month_order[sunspot_m] - 1)) / (11 * 12) * 100,2)
                    t1=find_percent(def1)
                    avg_sp=avg_sp+cycle.years[t1.year].months[t1.month].avg_sunspots
                    avg_storms=avg_storms+cycle.years[t1.year].months[t1.month].storm_count
                avg_sp=avg_sp/3
                avg_storms = avg_storms / 3
                print("expected sunspot count",sunspot_m,sunspot_y,":",avg_sp)
                print("expected storm count ", sunspot_m, sunspot_y, ":", avg_storms)









                While_l = input("want to try another time?")
                while True:
                    if While_l == "no":
                        break
                    elif While_l == "yes":
                        break
                    else:
                        print("Invalid input. Please input yes or no")
                        While_l = input("want to try another time?")
                if While_l == "no":
                    break
            else:
                print(
                    "Error 5: Month must be one of the 12 calendar months and Year must be between 1976 and 2030. Try again ")
        except ValueError:
            print("Error 6:Not a valid input. Please try again")

        #
        # for cycle in cycles:
        #     if sunspot_y in cycle.years:
        #
        #         print("Average sunspots in", sunspot_m, sunspot_y, "=",
        #               cycle.years[sunspot_y].months[sunspot_m].avg_sunspots)
        #         print("Radiation storm count in", sunspot_m, sunspot_y, "=",
        #               cycle.years[sunspot_y].months[sunspot_m].storm_count)
        #         print("Radiation storm max severity in", sunspot_m, sunspot_y, "=",
        #               cycle.years[sunspot_y].months[sunspot_m].max_severity)
        #         print("percent of solar cycle completed",
        #               (((sunspot_y - ((sunspot_y-2008)//11)) * 12) + (Data.month_order[sunspot_m] - 1)) / (
        #                       cycle.duration_years * 12) * 100 // 1)





