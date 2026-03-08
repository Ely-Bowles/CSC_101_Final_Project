###Important: Outline and data was created by ChatGPT

month_order = {
    "Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4,
    "May": 5, "Jun": 6, "Jul": 7, "Aug": 8,
    "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12
}

def percent_complete(cycle, year, month):
    start_year = int(cycle.start_date)
    total_months = cycle.duration_years * 12

    months_passed = (year - start_year) * 12
    months_passed += (month_order[month] - 1)

    return round((months_passed / total_months) * 100, 2)

class MonthData:
    def __init__(self, month, avg_sunspots, storm_count, max_severity):
        self.month = month
        self.avg_sunspots = avg_sunspots
        self.storm_count = storm_count
        self.max_severity = max_severity


    def __repr__(self):
            return (f"MonthData(month={self.month!r}, avg_sunspots={self.avg_sunspots}, "
                    f"storm_count={self.storm_count}, max_severity={self.max_severity!r})")


class YearData:
    def __init__(self, year, months_dict):
        self.year = year
        # dict: "Jan" -> MonthData(...)
        self.months = {
            month: MonthData(month, data["avg_sunspots"], data["storm_count"], data["max_severity"])
            for month, data in months_dict.items()
        }

    def __repr__(self):
        return f"YearData(year={self.year}, months={list(self.months.keys())})"

class SolarCycle:
    def __init__(self, cycle_number, start_date, end_date, duration_years, years_dict):
        self.cycle_number = cycle_number
        self.start_date = start_date
        self.end_date = end_date
        self.duration_years = duration_years
        # dict: 1989 -> YearData(...)
        self.years = {
            year: YearData(year, months)
            for year, months in years_dict.items()
        }

    def __repr__(self):
        return (f"SolarCycle(cycle_number={self.cycle_number}, "f"years={min(self.years)}–{max(self.years)})")


def cycle_from_dict(d):
    return SolarCycle(
        d["cycle_number"],
        d["start_date"],
        d["end_date"],
        d["duration_years"],
        d["years"]
    )



# Solar Cycle 21
cycle21 = {
    "cycle_number": 21,
    "start_date": 1976,   # official NOAA/SIDC timing
    "end_date": 1986,
    "duration_years": 11,
    "years": {
        1976: {
            "Jan": {"avg_sunspots": 11.9, "storm_count": 0, "max_severity": 0},
            "Feb": {"avg_sunspots": 6.4,  "storm_count": 0, "max_severity": 0},
            "Mar": {"avg_sunspots": 31.5, "storm_count": 0, "max_severity": 0},
            "Apr": {"avg_sunspots": 27.3, "storm_count": 1, "max_severity": "S1"},
            "May": {"avg_sunspots": 18.2, "storm_count": 1, "max_severity": "S1"},
            "Jun": {"avg_sunspots": 17.9, "storm_count": 0, "max_severity": 0},
            "Jul": {"avg_sunspots": 2.9,  "storm_count": 0, "max_severity": 0},
            "Aug": {"avg_sunspots": 24.1, "storm_count": 0, "max_severity": 0},
            "Sep": {"avg_sunspots": 20.0, "storm_count": 0, "max_severity": 0},
            "Oct": {"avg_sunspots": 29.7, "storm_count": 0, "max_severity": 0},
            "Nov": {"avg_sunspots": 7.9,  "storm_count": 0, "max_severity": 0},
            "Dec": {"avg_sunspots": 22.3, "storm_count": 0, "max_severity": 0},
        },
        1977: {
            "Jan": {"avg_sunspots": 23.8, "storm_count": 0, "max_severity": 0},
            "Feb": {"avg_sunspots": 33.3, "storm_count": 0, "max_severity": 0},
            "Mar": {"avg_sunspots": 13.0, "storm_count": 0, "max_severity": 0},
            "Apr": {"avg_sunspots": 19.0, "storm_count": 0, "max_severity": 0},
            "May": {"avg_sunspots": 27.0, "storm_count": 0, "max_severity": 0},
            "Jun": {"avg_sunspots": 54.9, "storm_count": 0, "max_severity": 0},
            "Jul": {"avg_sunspots": 30.6, "storm_count": 0, "max_severity": 0},
            "Aug": {"avg_sunspots": 43.0, "storm_count": 0, "max_severity": 0},
            "Sep": {"avg_sunspots": 62.4, "storm_count": 1, "max_severity": "S2"},
            "Oct": {"avg_sunspots": 62.1, "storm_count": 0, "max_severity": 0},
            "Nov": {"avg_sunspots": 41.6, "storm_count": 1, "max_severity": "S2"},
            "Dec": {"avg_sunspots": 61.4, "storm_count": 0, "max_severity": 0},
        },
        1978: {
            "Jan": {"avg_sunspots": 73.7, "storm_count": 0, "max_severity": 0},
            "Feb": {"avg_sunspots": 132.6, "storm_count": 1, "max_severity": "S3"},
            "Mar": {"avg_sunspots": 108.4, "storm_count": 0, "max_severity": 0},
            "Apr": {"avg_sunspots": 141.2, "storm_count": 2, "max_severity": "S3"},
            "May": {"avg_sunspots": 117.1, "storm_count": 1, "max_severity": "S3"},
            "Jun": {"avg_sunspots": 134.6, "storm_count": 2, "max_severity": "S1"},
            "Jul": {"avg_sunspots": 99.7, "storm_count": 1, "max_severity": "S1"},
            "Aug": {"avg_sunspots": 82.4, "storm_count": 0, "max_severity": 0},
            "Sep": {"avg_sunspots": 195.7, "storm_count": 1, "max_severity": "S3"},
            "Oct": {"avg_sunspots": 177.1, "storm_count": 0, "max_severity": 0},
            "Nov": {"avg_sunspots": 138.5, "storm_count": 1, "max_severity": "S1"},
            "Dec": {"avg_sunspots": 173.9, "storm_count": 0, "max_severity": 0},
        },
        1979: {
            "Jan": {"avg_sunspots": 235.9, "storm_count": 0, "max_severity": 0},
            "Feb": {"avg_sunspots": 194.7, "storm_count": 1, "max_severity": "S1"},
            "Mar": {"avg_sunspots": 195.3, "storm_count": 0, "max_severity": 0},
            "Apr": {"avg_sunspots": 143.7, "storm_count": 1, "max_severity": "S1"},
            "May": {"avg_sunspots": 190.3, "storm_count": 0, "max_severity": 0},
            "Jun": {"avg_sunspots": 211.7, "storm_count": 1, "max_severity": "S3"},
            "Jul": {"avg_sunspots": 225.7, "storm_count": 1, "max_severity": "S1"},
            "Aug": {"avg_sunspots": 201.4, "storm_count": 1, "max_severity": "S2"},
            "Sep": {"avg_sunspots": 266.9, "storm_count": 1, "max_severity": "S1"},
            "Oct": {"avg_sunspots": 263.6, "storm_count": 0, "max_severity": 0},
            "Nov": {"avg_sunspots": 259.5, "storm_count": 1, "max_severity": "S1"},
            "Dec": {"avg_sunspots": 249.6, "storm_count": 0, "max_severity": 0},
        },

        1980: {
            "Jan": {"avg_sunspots": 226.1, "storm_count": 0, "max_severity": 0},
            "Feb": {"avg_sunspots": 219.4, "storm_count": 1, "max_severity": "S1"},
            "Mar": {"avg_sunspots": 178.7, "storm_count": 0, "max_severity": 0},
            "Apr": {"avg_sunspots": 232.2, "storm_count": 3, "max_severity": "S1"},
            "May": {"avg_sunspots": 254.7, "storm_count": 4, "max_severity": "S2"},
            "Jun": {"avg_sunspots": 222.7, "storm_count": 1, "max_severity": "S1"},
            "Jul": {"avg_sunspots": 192.9, "storm_count": 1, "max_severity": "S2"},
            "Aug": {"avg_sunspots": 191.7, "storm_count": 0, "max_severity": 0},
            "Sep": {"avg_sunspots": 219.6, "storm_count": 0, "max_severity": 0},
            "Oct": {"avg_sunspots": 233.3, "storm_count": 0, "max_severity": 0},
            "Nov": {"avg_sunspots": 209.5, "storm_count": 0, "max_severity": 0},
            "Dec": {"avg_sunspots": 246.9, "storm_count": 0, "max_severity": 0},
        },
        1981: {
            "Jan": {"avg_sunspots": 156.6, "storm_count": 0, "max_severity": 0},
            "Feb": {"avg_sunspots": 189.9, "storm_count": 0, "max_severity": 0},
            "Mar": {"avg_sunspots": 196.6, "storm_count": 1, "max_severity": "S1"},
            "Apr": {"avg_sunspots": 225.3, "storm_count": 2, "max_severity": "S3"},
            "May": {"avg_sunspots": 194.7, "storm_count": 2, "max_severity": "S2"},
            "Jun": {"avg_sunspots": 131.6, "storm_count": 0, "max_severity": 0},
            "Jul": {"avg_sunspots": 205.3, "storm_count": 2, "max_severity": "S1"},
            "Aug": {"avg_sunspots": 242.5, "storm_count": 1, "max_severity": "S1"},
            "Sep": {"avg_sunspots": 245.3, "storm_count": 0, "max_severity": 0},
            "Oct": {"avg_sunspots": 216.2, "storm_count": 1, "max_severity": "S3"},
            "Nov": {"avg_sunspots": 186.0, "storm_count": 0, "max_severity": 0},
            "Dec": {"avg_sunspots": 195.4, "storm_count": 1, "max_severity": "S1"},
        },

        1982: {
            "Jan": {"avg_sunspots": 252.9, "storm_count": 1, "max_severity": "S2"},
            "Feb": {"avg_sunspots": 149.4, "storm_count": 0, "max_severity": 0},
            "Mar": {"avg_sunspots": 210.1, "storm_count": 0, "max_severity": 0},
            "Apr": {"avg_sunspots": 195.9, "storm_count": 0, "max_severity": 0},
            "May": {"avg_sunspots": 187.7, "storm_count": 0, "max_severity": 0},
            "Jun": {"avg_sunspots": 169.4, "storm_count": 2, "max_severity": "S1"},
            "Jul": {"avg_sunspots": 153.9, "storm_count": 2, "max_severity": "S3"},
            "Aug": {"avg_sunspots": 122.0, "storm_count": 0, "max_severity": 0},
            "Sep": {"avg_sunspots": 108.4, "storm_count": 1, "max_severity": "S1"},
            "Oct": {"avg_sunspots": 168.8, "storm_count": 0, "max_severity": 0},
            "Nov": {"avg_sunspots": 216.4, "storm_count": 2, "max_severity": "S1"},
            "Dec": {"avg_sunspots": 196.3, "storm_count": 4, "max_severity": "S3"},
        },
        1983: {
            "Jan": {"avg_sunspots": 190.1, "storm_count": 0, "max_severity": 0},
            "Feb": {"avg_sunspots": 203.3, "storm_count": 1, "max_severity": "S2"},
            "Mar": {"avg_sunspots": 145.1, "storm_count": 0, "max_severity": 0},
            "Apr": {"avg_sunspots": 154.3, "storm_count": 0, "max_severity": 0},
            "May": {"avg_sunspots": 170.3, "storm_count": 0, "max_severity": 0},
            "Jun": {"avg_sunspots": 162.4, "storm_count": 1, "max_severity": "S1"},
            "Jul": {"avg_sunspots": 104.1, "storm_count": 0, "max_severity": 0},
            "Aug": {"avg_sunspots": 76.8,  "storm_count": 0, "max_severity": 0},
            "Sep": {"avg_sunspots": 71.5,  "storm_count": 0, "max_severity": 0},
            "Oct": {"avg_sunspots": 82.3,  "storm_count": 0, "max_severity": 0},
            "Nov": {"avg_sunspots": 61.1,  "storm_count": 0, "max_severity": 0},
            "Dec": {"avg_sunspots": 65.3,  "storm_count": 0, "max_severity": 0},
        },
        1984: {
            "Jan": {"avg_sunspots": 70.2,  "storm_count": 0, "max_severity": 0},
            "Feb": {"avg_sunspots": 99.1,  "storm_count": 2, "max_severity": "S2"},
            "Mar": {"avg_sunspots": 71.1,  "storm_count": 2, "max_severity": "S2"},
            "Apr": {"avg_sunspots": 124.5, "storm_count": 1, "max_severity": "S3"},
            "May": {"avg_sunspots": 100.6, "storm_count": 2, "max_severity": "S1"},
            "Jun": {"avg_sunspots": 66.3,  "storm_count": 0, "max_severity": 0},
            "Jul": {"avg_sunspots": 43.7,  "storm_count": 0, "max_severity": 0},
            "Aug": {"avg_sunspots": 30.7,  "storm_count": 0, "max_severity": 0},
            "Sep": {"avg_sunspots": 52.1,  "storm_count": 0, "max_severity": 0},
            "Oct": {"avg_sunspots": 35.9,  "storm_count": 0, "max_severity": 0},
            "Nov": {"avg_sunspots": 55.5,  "storm_count": 0, "max_severity": 0},
            "Dec": {"avg_sunspots": 25.7,  "storm_count": 0, "max_severity": 0},
        },

        1985: {
            "Jan": {"avg_sunspots": 34.5, "storm_count": 1, "max_severity": "S1"},
            "Feb": {"avg_sunspots": 16.2, "storm_count": 0, "max_severity": 0},
            "Mar": {"avg_sunspots": 21.3, "storm_count": 0, "max_severity": 0},
            "Apr": {"avg_sunspots": 16.6, "storm_count": 1, "max_severity": "S2"},
            "May": {"avg_sunspots": 18.0, "storm_count": 0, "max_severity": 0},
            "Jun": {"avg_sunspots": 14.9, "storm_count": 0, "max_severity": 0},
            "Jul": {"avg_sunspots": 18.2, "storm_count": 1, "max_severity": "S2"},
            "Aug": {"avg_sunspots": 9.3, "storm_count": 0, "max_severity": 0},
            "Sep": {"avg_sunspots": 16.2, "storm_count": 0, "max_severity": 0},
            "Oct": {"avg_sunspots": 14.7, "storm_count": 0, "max_severity": 0},
            "Nov": {"avg_sunspots": 14.9, "storm_count": 0, "max_severity": 0},
            "Dec": {"avg_sunspots": 25.9, "storm_count": 0, "max_severity": 0},
        },
        1986: {
            "Jan": {"avg_sunspots": 13.4, "storm_count": 0, "max_severity": 0},
            "Feb": {"avg_sunspots": 17.0, "storm_count": 3, "max_severity": "S2"},
            "Mar": {"avg_sunspots": 13.9, "storm_count": 1, "max_severity": "S1"},
            "Apr": {"avg_sunspots": 6.8, "storm_count": 0, "max_severity": 0},
            "May": {"avg_sunspots": 12.9, "storm_count": 1, "max_severity": "S1"},
            "Jun": {"avg_sunspots": 9.2, "storm_count": 0, "max_severity": 0},
            "Jul": {"avg_sunspots": 8.2, "storm_count": 0, "max_severity": 0},
            "Aug": {"avg_sunspots": 6.7, "storm_count": 0, "max_severity": 0},
            "Sep": {"avg_sunspots": 9.4, "storm_count": 0, "max_severity": 0},
            "Oct": {"avg_sunspots": 12.2, "storm_count": 0, "max_severity": 0},
            "Nov": {"avg_sunspots": 15.5, "storm_count": 0, "max_severity": 0},
            "Dec": {"avg_sunspots": 16.6, "storm_count": 0, "max_severity": 0},

        }}}
cycle22 = {
    "cycle_number": 22,
    "start_date":1987,   # official NOAA/SIDC timing
    "end_date":1996,
    "duration_years": 10,
    "years": {
        1987: {
            "Jan": {"avg_sunspots": 9.8, "storm_count": 0, "max_severity": 0},
            "Feb": {"avg_sunspots": 3.4, "storm_count": 0, "max_severity": 0},
            "Mar": {"avg_sunspots": 17.4, "storm_count": 0, "max_severity": 0},
            "Apr": {"avg_sunspots": 46.0, "storm_count": 0, "max_severity": 0},
            "May": {"avg_sunspots": 39.1, "storm_count": 0, "max_severity": 0},
            "Jun": {"avg_sunspots": 18.8, "storm_count": 0, "max_severity": 0},
            "Jul": {"avg_sunspots": 38.2, "storm_count": 0, "max_severity": 0},
            "Aug": {"avg_sunspots": 47.9, "storm_count": 0, "max_severity": 0},
            "Sep": {"avg_sunspots": 42.2, "storm_count": 0, "max_severity": 0},
            "Oct": {"avg_sunspots": 63.4, "storm_count": 0, "max_severity": 0},
            "Nov": {"avg_sunspots": 48.8, "storm_count": 1, "max_severity": "S1"},
            "Dec": {"avg_sunspots": 29.1, "storm_count": 0, "max_severity": 0},
        },
        1988: {
            "Jan": {"avg_sunspots": 70.5, "storm_count": 1, "max_severity": "S1"},
            "Feb": {"avg_sunspots": 45.4, "storm_count": 0, "max_severity": 0},
            "Mar": {"avg_sunspots": 91.2, "storm_count": 1, "max_severity": "S1"},
            "Apr": {"avg_sunspots": 108.8, "storm_count": 0, "max_severity": 0},
            "May": {"avg_sunspots": 74.2, "storm_count": 0, "max_severity": 0},
            "Jun": {"avg_sunspots": 124.3, "storm_count": 1, "max_severity": "S1"},
            "Jul": {"avg_sunspots": 131.4, "storm_count": 0, "max_severity": 0},
            "Aug": {"avg_sunspots": 139.4, "storm_count": 1, "max_severity": "S1"},
            "Sep": {"avg_sunspots": 142.7, "storm_count": 0, "max_severity": 0},
            "Oct": {"avg_sunspots": 156.5, "storm_count": 1, "max_severity": "S1"},
            "Nov": {"avg_sunspots": 156.8, "storm_count": 2, "max_severity": "S1"},
            "Dec": {"avg_sunspots": 231.2, "storm_count": 1, "max_severity": "S1"},
        },
        1989: {
            "Jan": {"avg_sunspots": 210.1, "storm_count": 1, "max_severity": "S1"},
            "Feb": {"avg_sunspots": 208.7, "storm_count": 0, "max_severity": 0},
            "Mar": {"avg_sunspots": 170.4, "storm_count": 3, "max_severity": "S4"},
            "Apr": {"avg_sunspots": 166.3, "storm_count": 1, "max_severity": "S1"},
            "May": {"avg_sunspots": 195.4, "storm_count": 2, "max_severity": "S2"},
            "Jun": {"avg_sunspots": 284.5, "storm_count": 2, "max_severity": "S1"},
            "Jul": {"avg_sunspots": 180.5, "storm_count": 1, "max_severity": "S1"},
            "Aug": {"avg_sunspots": 232.0, "storm_count": 4, "max_severity": "S4"},
            "Sep": {"avg_sunspots": 225.1, "storm_count": 3, "max_severity": "S3"},
            "Oct": {"avg_sunspots": 212.2, "storm_count": 4, "max_severity": "S4"},
            "Nov": {"avg_sunspots": 238.2, "storm_count": 3, "max_severity": "S3"},
            "Dec": {"avg_sunspots": 211.4, "storm_count": 1, "max_severity": "S3"},
        },
        1990: {
            "Jan": {"avg_sunspots": 227.4, "storm_count": 0, "max_severity": 0},
            "Feb": {"avg_sunspots": 171.8, "storm_count": 0, "max_severity": 0},
            "Mar": {"avg_sunspots": 191.7, "storm_count": 2, "max_severity": "S3"},
            "Apr": {"avg_sunspots": 189.7, "storm_count": 3, "max_severity": "S1"},
            "May": {"avg_sunspots": 175.2, "storm_count": 4, "max_severity": "S3"},
            "Jun": {"avg_sunspots": 153.3, "storm_count": 1, "max_severity": "S1"},
            "Jul": {"avg_sunspots": 191.1, "storm_count": 1, "max_severity": "S1"},
            "Aug": {"avg_sunspots": 252.1, "storm_count": 1, "max_severity": "S2"},
            "Sep": {"avg_sunspots": 169.1, "storm_count": 0, "max_severity": 0},
            "Oct": {"avg_sunspots": 199.4, "storm_count": 0, "max_severity": 0},
            "Nov": {"avg_sunspots": 178.8, "storm_count": 0, "max_severity": 0},
            "Dec": {"avg_sunspots": 197.1, "storm_count": 0, "max_severity": 0},
        },
        1991: {
            "Jan": {"avg_sunspots": 195.3, "storm_count": 1, "max_severity": "S2"},
            "Feb": {"avg_sunspots": 240.3, "storm_count": 1, "max_severity": "S1"},
            "Mar": {"avg_sunspots": 197.0, "storm_count": 2, "max_severity": "S4"},
            "Apr": {"avg_sunspots": 197.6, "storm_count": 1, "max_severity": "S1"},
            "May": {"avg_sunspots": 166.9, "storm_count": 2, "max_severity": "S2"},
            "Jun": {"avg_sunspots": 224.7, "storm_count": 3, "max_severity": "S3"},
            "Jul": {"avg_sunspots": 240.2, "storm_count": 2, "max_severity": "S3"},
            "Aug": {"avg_sunspots": 240.8, "storm_count": 1, "max_severity": "S2"},
            "Sep": {"avg_sunspots": 168.9, "storm_count": 0, "max_severity": 0},
            "Oct": {"avg_sunspots": 197.1, "storm_count": 2, "max_severity": "S2"},
            "Nov": {"avg_sunspots": 159.5, "storm_count": 0, "max_severity": 0},
            "Dec": {"avg_sunspots": 212.6, "storm_count": 1, "max_severity": "S2"},
    },
        1992: {
            "Jan": {"avg_sunspots": 198.3, "storm_count": 0, "max_severity": 0},
            "Feb": {"avg_sunspots": 230.7, "storm_count": 1, "max_severity": "S1"},
            "Mar": {"avg_sunspots": 151.0, "storm_count": 1, "max_severity": "S3"},
            "Apr": {"avg_sunspots": 142.2, "storm_count": 0, "max_severity": 0},
            "May": {"avg_sunspots": 94.3,  "storm_count": 1, "max_severity": "S3"},
            "Jun": {"avg_sunspots": 98.5,  "storm_count": 2, "max_severity": "S2"},
            "Jul": {"avg_sunspots": 114.2, "storm_count": 0, "max_severity": 0},
            "Aug": {"avg_sunspots": 91.9,  "storm_count": 1, "max_severity": "S1"},
            "Sep": {"avg_sunspots": 94.0,  "storm_count": 0, "max_severity": 0},
            "Oct": {"avg_sunspots": 133.4, "storm_count": 1, "max_severity": "S3"},
            "Nov": {"avg_sunspots": 129.6, "storm_count": 1, "max_severity": "S3"},
            "Dec": {"avg_sunspots": 122.0, "storm_count": 0, "max_severity": 0},
    },
        1993: {
            "Jan": {"avg_sunspots": 81.4,  "storm_count": 0, "max_severity": 0},
            "Feb": {"avg_sunspots": 127.8, "storm_count": 0, "max_severity": 0},
            "Mar": {"avg_sunspots": 102.4, "storm_count": 1, "max_severity": "S1"},
            "Apr": {"avg_sunspots": 94.4,  "storm_count": 0, "max_severity": 0},
            "May": {"avg_sunspots": 78.8,  "storm_count": 0, "max_severity": 0},
            "Jun": {"avg_sunspots": 69.6,  "storm_count": 0, "max_severity": 0},
            "Jul": {"avg_sunspots": 80.4,  "storm_count": 0, "max_severity": 0},
            "Aug": {"avg_sunspots": 62.5,  "storm_count": 0, "max_severity": 0},
            "Sep": {"avg_sunspots": 31.2,  "storm_count": 0, "max_severity": 0},
            "Oct": {"avg_sunspots": 71.1,  "storm_count": 0, "max_severity": 0},
            "Nov": {"avg_sunspots": 48.2,  "storm_count": 0, "max_severity": 0},
            "Dec": {"avg_sunspots": 68.4,  "storm_count": 0, "max_severity": 0},
    },
        1994: {
            "Jan": {"avg_sunspots": 84.9,  "storm_count": 0, "max_severity": 0},
            "Feb": {"avg_sunspots": 54.9,  "storm_count": 0, "max_severity": 0},
            "Mar": {"avg_sunspots": 47.5,  "storm_count": 0, "max_severity": 0},
            "Apr": {"avg_sunspots": 27.4,  "storm_count": 0, "max_severity": 0},
            "May": {"avg_sunspots": 29.8,  "storm_count": 0, "max_severity": 0},
            "Jun": {"avg_sunspots": 39.7,  "storm_count": 0, "max_severity": 0},
            "Jul": {"avg_sunspots": 50.6,  "storm_count": 0, "max_severity": 0},
            "Aug": {"avg_sunspots": 34.3,  "storm_count": 0, "max_severity": 0},
            "Sep": {"avg_sunspots": 40.5,  "storm_count": 0, "max_severity": 0},
            "Oct": {"avg_sunspots": 67.1,  "storm_count": 1, "max_severity": "S2"},
            "Nov": {"avg_sunspots": 29.5,  "storm_count": 0, "max_severity": 0},
            "Dec": {"avg_sunspots": 32.2,  "storm_count": 0, "max_severity": 0},
        },
        1995: {
            "Jan": {"avg_sunspots": 32.6, "storm_count": 0, "max_severity": 0},
            "Feb": {"avg_sunspots": 45.8, "storm_count": 0, "max_severity": 0},
            "Mar": {"avg_sunspots": 46.3, "storm_count": 0, "max_severity": 0},
            "Apr": {"avg_sunspots": 21.6, "storm_count": 0, "max_severity": 0},
            "May": {"avg_sunspots": 19.4, "storm_count": 0, "max_severity": 0},
            "Jun": {"avg_sunspots": 22.5, "storm_count": 0, "max_severity": 0},
            "Jul": {"avg_sunspots": 20.4, "storm_count": 0, "max_severity": 0},
            "Aug": {"avg_sunspots": 18.2, "storm_count": 0, "max_severity": 0},
            "Sep": {"avg_sunspots": 15.7, "storm_count": 0, "max_severity": 0},
            "Oct": {"avg_sunspots": 30.6, "storm_count": 1, "max_severity": "S1"},
            "Nov": {"avg_sunspots": 14.0, "storm_count": 0, "max_severity": 0},
            "Dec": {"avg_sunspots": 14.9, "storm_count": 0, "max_severity": 0},
        },
        1996: {
            "Jan": {"avg_sunspots": 13.3, "storm_count": 0, "max_severity": 0},
            "Feb": {"avg_sunspots": 7.7,  "storm_count": 0, "max_severity": 0},
            "Mar": {"avg_sunspots": 12.6, "storm_count": 0, "max_severity": 0},
            "Apr": {"avg_sunspots": 6.8,  "storm_count": 0, "max_severity": 0},
            "May": {"avg_sunspots": 7.6,  "storm_count": 0, "max_severity": 0},
            "Jun": {"avg_sunspots": 16.5, "storm_count": 0, "max_severity": 0},
            "Jul": {"avg_sunspots": 11.8, "storm_count": 0, "max_severity": 0},
            "Aug": {"avg_sunspots": 19.7, "storm_count": 0, "max_severity": 0},
            "Sep": {"avg_sunspots": 3.0,  "storm_count": 0, "max_severity": 0},
            "Oct": {"avg_sunspots": 0.7,  "storm_count": 0, "max_severity": 0},
            "Nov": {"avg_sunspots": 24.9, "storm_count": 0, "max_severity": 0},
            "Dec": {"avg_sunspots": 14.0, "storm_count": 0, "max_severity": 0},
        }}}

cycle23 = {
    "cycle_number": 23,
    "start_date":1997,   # official NOAA/SIDC timing
    "end_date":2008,
    "duration_years": 12,
    "years": {
        1997: {
            "Jan": {"avg_sunspots": 7.4,  "storm_count": 0, "max_severity": 0},
            "Feb": {"avg_sunspots": 11.0, "storm_count": 0, "max_severity": 0},
            "Mar": {"avg_sunspots": 12.1, "storm_count": 0, "max_severity": 0},
            "Apr": {"avg_sunspots": 23.0, "storm_count": 0, "max_severity": 0},
            "May": {"avg_sunspots": 25.4, "storm_count": 0, "max_severity": 0},
            "Jun": {"avg_sunspots": 20.8, "storm_count": 0, "max_severity": 0},
            "Jul": {"avg_sunspots": 12.9, "storm_count": 0, "max_severity": 0},
            "Aug": {"avg_sunspots": 35.7, "storm_count": 0, "max_severity": 0},
            "Sep": {"avg_sunspots": 59.7, "storm_count": 0, "max_severity": 0},
            "Oct": {"avg_sunspots": 32.8, "storm_count": 0, "max_severity": 0},
            "Nov": {"avg_sunspots": 50.4, "storm_count": 2, "max_severity": "S2"},
            "Dec": {"avg_sunspots": 55.5, "storm_count": 0, "max_severity": 0},
        },
        1998: {
            "Jan": {"avg_sunspots": 44.5, "storm_count": 0, "max_severity": 0},
            "Feb": {"avg_sunspots": 50.2, "storm_count": 0, "max_severity": 0},
            "Mar": {"avg_sunspots": 82.0, "storm_count": 0, "max_severity": 0},
            "Apr": {"avg_sunspots": 70.6, "storm_count": 1, "max_severity": "S1"},
            "May": {"avg_sunspots": 74.0, "storm_count": 3, "max_severity": "S2"},
            "Jun": {"avg_sunspots": 90.5, "storm_count": 0, "max_severity": 0},
            "Jul": {"avg_sunspots": 96.7, "storm_count": 0, "max_severity": 0},
            "Aug": {"avg_sunspots": 121.1, "storm_count": 1, "max_severity": "S2"},
            "Sep": {"avg_sunspots": 132.0, "storm_count": 2, "max_severity": "S2"},
            "Oct": {"avg_sunspots": 78.5, "storm_count": 0, "max_severity": 0},
            "Nov": {"avg_sunspots": 97.3, "storm_count": 1, "max_severity": "S1"},
            "Dec": {"avg_sunspots": 119.2, "storm_count": 0, "max_severity": 0},
        },
        1999: {
            "Jan": {"avg_sunspots": 86.0, "storm_count": 0, "max_severity": 0},
            "Feb": {"avg_sunspots": 98.0, "storm_count": 0, "max_severity": 0},
            "Mar": {"avg_sunspots": 103.5, "storm_count": 0, "max_severity": 0},
            "Apr": {"avg_sunspots": 93.6, "storm_count": 1, "max_severity": "S1"},
            "May": {"avg_sunspots": 149.6, "storm_count": 1, "max_severity": "S1"},
            "Jun": {"avg_sunspots": 207.2, "storm_count": 2, "max_severity": "S1"},
            "Jul": {"avg_sunspots": 173.5, "storm_count": 0, "max_severity": 0},
            "Aug": {"avg_sunspots": 142.3, "storm_count": 0, "max_severity": 0},
            "Sep": {"avg_sunspots": 106.3, "storm_count": 0, "max_severity": 0},
            "Oct": {"avg_sunspots": 168.7, "storm_count": 0, "max_severity": 0},
            "Nov": {"avg_sunspots": 188.3, "storm_count": 0, "max_severity": 0},
            "Dec": {"avg_sunspots": 116.8, "storm_count": 0, "max_severity": 0},
        },
        2000: {
            "Jan": {"avg_sunspots": 133.1,"storm_count": 0, "max_severity": 0},
            "Feb": {"avg_sunspots": 165.7,"storm_count": 1, "max_severity": "S1"},
            "Mar": {"avg_sunspots": 217.7,"storm_count": 0, "max_severity": 0},
            "Apr": {"avg_sunspots": 191.5,"storm_count": 1, "max_severity": "S1"},
            "May": {"avg_sunspots": 165.9,"storm_count": 3, "max_severity": "S2"},
            "Jun": {"avg_sunspots": 188.0,"storm_count": 2, "max_severity": "S1"},
            "Jul": {"avg_sunspots": 244.3,"storm_count": 3, "max_severity": "S4"},
            "Aug": {"avg_sunspots": 180.5,"storm_count": 1, "max_severity": "S1"},
            "Sep": {"avg_sunspots": 156.0,"storm_count": 1, "max_severity": "S1"},
            "Oct": {"avg_sunspots": 141.6,"storm_count": 1, "max_severity": "S1"},
            "Nov": {"avg_sunspots": 158.1,"storm_count": 3, "max_severity": "S3"},
            "Dec": {"avg_sunspots": 143.3,"storm_count": 0, "max_severity": 0},
        },
        2001: {
            "Jan": {"avg_sunspots": 142.6, "storm_count": 0, "max_severity": 0},
            "Feb": {"avg_sunspots": 121.5, "storm_count": 0, "max_severity": 0},
            "Mar": {"avg_sunspots": 165.8, "storm_count": 0, "max_severity": 0},
            "Apr": {"avg_sunspots": 161.7, "storm_count": 2, "max_severity": "S1"},
            "May": {"avg_sunspots": 142.1, "storm_count": 0, "max_severity": 0},
            "Jun": {"avg_sunspots": 202.9, "storm_count": 1, "max_severity": "S1"},
            "Jul": {"avg_sunspots": 123.0, "storm_count": 0, "max_severity": 0},
            "Aug": {"avg_sunspots": 161.5, "storm_count": 1, "max_severity": "S2"},
            "Sep": {"avg_sunspots": 238.2, "storm_count": 1, "max_severity": "S3"},
            "Oct": {"avg_sunspots": 194.1, "storm_count": 1, "max_severity": "S2"},
            "Nov": {"avg_sunspots": 176.6, "storm_count": 2, "max_severity": "S3"},
            "Dec": {"avg_sunspots": 213.4, "storm_count": 2, "max_severity": "S2"},
        },
        2002: {
            "Jan": {"avg_sunspots": 184.6,"storm_count": 2, "max_severity": "S1"},
            "Feb": {"avg_sunspots": 170.2,"storm_count": 1, "max_severity": "S1"},
            "Mar": {"avg_sunspots": 147.1,"storm_count": 4, "max_severity": "S1"},
            "Apr": {"avg_sunspots": 186.9,"storm_count": 2, "max_severity": "S2"},
            "May": {"avg_sunspots": 187.5,"storm_count": 1, "max_severity": "S2"},
            "Jun": {"avg_sunspots": 128.8,"storm_count": 0, "max_severity": 0},
            "Jul": {"avg_sunspots": 112.0, "storm_count": 3, "max_severity": "S2"},
            "Aug": {"avg_sunspots": 100.0, "storm_count": 3, "max_severity": "S2"},
            "Sep": {"avg_sunspots": 83.9, "storm_count": 1, "max_severity": "S1"},
            "Oct": {"avg_sunspots": 104.0, "storm_count": 0, "max_severity": 0},
            "Nov": {"avg_sunspots": 110.6, "storm_count": 1, "max_severity": "S2"},
            "Dec": {"avg_sunspots": 104.5, "storm_count": 0, "max_severity": 0},
        },
        2003: {
            "Jan": {"avg_sunspots": 98.8,  "storm_count": 0, "max_severity": 0},
            "Feb": {"avg_sunspots": 57.4,  "storm_count": 0, "max_severity": 0},
            "Mar": {"avg_sunspots": 74.5,  "storm_count": 0, "max_severity": 0},
            "Apr": {"avg_sunspots": 62.7,  "storm_count": 0, "max_severity": 0},
            "May": {"avg_sunspots": 72.1,  "storm_count": 2, "max_severity": "S2"},
            "Jun": {"avg_sunspots": 68.5,  "storm_count": 1, "max_severity": "S1"},
            "Jul": {"avg_sunspots": 56.0,  "storm_count": 0, "max_severity": 0},
            "Aug": {"avg_sunspots": 55.5,  "storm_count": 0, "max_severity": 0},
            "Sep": {"avg_sunspots": 53.4,  "storm_count": 0, "max_severity": 0},
            "Oct": {"avg_sunspots": 67.0,  "storm_count": 3, "max_severity": "S4"},
            "Nov": {"avg_sunspots": 99.4,  "storm_count": 3, "max_severity": "S3"},
            "Dec": {"avg_sunspots": 73.4,  "storm_count": 1, "max_severity": "S1"},
        },
        2004: {
            "Jan": {"avg_sunspots": 52.9, "storm_count": 0, "max_severity": 0},
            "Feb": {"avg_sunspots": 47.9, "storm_count": 0, "max_severity": 0},
            "Mar": {"avg_sunspots": 49.9, "storm_count": 0, "max_severity": 0},
            "Apr": {"avg_sunspots": 58.1, "storm_count": 1, "max_severity": "S1"},
            "May": {"avg_sunspots": 44.1, "storm_count": 0, "max_severity": 0},
            "Jun": {"avg_sunspots": 38.2, "storm_count": 0, "max_severity": 0},
            "Jul": {"avg_sunspots": 47.5, "storm_count": 1, "max_severity": "S3"},
            "Aug": {"avg_sunspots": 38.4, "storm_count": 0, "max_severity": 0},
            "Sep": {"avg_sunspots": 45.3, "storm_count": 1, "max_severity": "S1"},
            "Oct": {"avg_sunspots": 41.7, "storm_count": 0, "max_severity": 0},
            "Nov": {"avg_sunspots": 40.0, "storm_count": 3, "max_severity": "S2"},
            "Dec": {"avg_sunspots": 28.9, "storm_count": 0, "max_severity": 0},
        },
        2005: {
            "Jan": {"avg_sunspots": 44.7, "storm_count": 1, "max_severity": "S3"},
            "Feb": {"avg_sunspots": 42.7, "storm_count": 0, "max_severity": 0},
            "Mar": {"avg_sunspots": 23.3, "storm_count": 0, "max_severity": 0},
            "Apr": {"avg_sunspots": 30.0, "storm_count": 0, "max_severity": 0},
            "May": {"avg_sunspots": 31.2, "storm_count": 1, "max_severity": "S3"},
            "Jun": {"avg_sunspots": 28.1, "storm_count": 1, "max_severity": "S1"},
            "Jul": {"avg_sunspots": 37.1, "storm_count": 2, "max_severity": "S2"},
            "Aug": {"avg_sunspots": 36.6, "storm_count": 1, "max_severity": "S2"},
            "Sep": {"avg_sunspots": 26.3, "storm_count": 1, "max_severity": "S3"},
            "Oct": {"avg_sunspots": 24.8, "storm_count": 0, "max_severity": 0},
            "Nov": {"avg_sunspots": 24.7, "storm_count": 0, "max_severity": 0},
            "Dec": {"avg_sunspots": 20.2, "storm_count": 0, "max_severity": 0},
        },
        2006: {
            "Jan": {"avg_sunspots": 15.4, "storm_count": 0, "max_severity": 0},
            "Feb": {"avg_sunspots": 22.5, "storm_count": 0, "max_severity": 0},
            "Mar": {"avg_sunspots": 22.7, "storm_count": 0, "max_severity": 0},
            "Apr": {"avg_sunspots": 21.9, "storm_count": 0, "max_severity": 0},
            "May": {"avg_sunspots": 22.5, "storm_count": 0, "max_severity": 0},
            "Jun": {"avg_sunspots": 19.5, "storm_count": 0, "max_severity": 0},
            "Jul": {"avg_sunspots": 12.7, "storm_count": 0, "max_severity": 0},
            "Aug": {"avg_sunspots": 12.6, "storm_count": 0, "max_severity": 0},
            "Sep": {"avg_sunspots": 12.2, "storm_count": 0, "max_severity": 0},
            "Oct": {"avg_sunspots": 14.4, "storm_count": 0, "max_severity": 0},
            "Nov": {"avg_sunspots": 15.6, "storm_count": 0, "max_severity": 0},
            "Dec": {"avg_sunspots": 13.6, "storm_count": 2, "max_severity": "S3"},
        },
        2007: {
            "Jan": {"avg_sunspots": 12.5, "storm_count": 0, "max_severity": 0},
            "Feb": {"avg_sunspots": 9.6, "storm_count": 0, "max_severity": 0},
            "Mar": {"avg_sunspots": 5.9, "storm_count": 0, "max_severity": 0},
            "Apr": {"avg_sunspots": 5.6, "storm_count": 0, "max_severity": 0},
            "May": {"avg_sunspots": 5.5, "storm_count": 0, "max_severity": 0},
            "Jun": {"avg_sunspots": 7.1, "storm_count": 0, "max_severity": 0},
            "Jul": {"avg_sunspots": 6.0, "storm_count": 0, "max_severity": 0},
            "Aug": {"avg_sunspots": 4.6, "storm_count": 0, "max_severity": 0},
            "Sep": {"avg_sunspots": 1.7, "storm_count": 0, "max_severity": 0},
            "Oct": {"avg_sunspots": 0.4, "storm_count": 0, "max_severity": 0},
            "Nov": {"avg_sunspots": 0.8, "storm_count": 0, "max_severity": 0},
            "Dec": {"avg_sunspots": 4.2, "storm_count": 0, "max_severity": 0},
        },

        2008: {
            "Jan": {"avg_sunspots": 3.4, "storm_count": 0, "max_severity": 0},
            "Feb": {"avg_sunspots": 0.9, "storm_count": 0, "max_severity": 0},
            "Mar": {"avg_sunspots": 2.9, "storm_count": 0, "max_severity": 0},
            "Apr": {"avg_sunspots": 4.1, "storm_count": 0, "max_severity": 0},
            "May": {"avg_sunspots": 2.7, "storm_count": 0, "max_severity": 0},
            "Jun": {"avg_sunspots": 3.7, "storm_count": 0, "max_severity": 0},
            "Jul": {"avg_sunspots": 0.6, "storm_count": 0, "max_severity": 0},
            "Aug": {"avg_sunspots": 0.3, "storm_count": 0, "max_severity": 0},
            "Sep": {"avg_sunspots": 1.2, "storm_count": 0, "max_severity": 0},
            "Oct": {"avg_sunspots": 4.2, "storm_count": 0, "max_severity": 0},
            "Nov": {"avg_sunspots": 6.6, "storm_count": 0, "max_severity": 0},
            "Dec": {"avg_sunspots": 1.0, "storm_count": 0, "max_severity": 0},
        }}}
cycle21_obj = cycle_from_dict(cycle21)
cycle22_obj = cycle_from_dict(cycle22)
cycle23_obj = cycle_from_dict(cycle23)


