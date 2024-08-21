def is_year_leap(year):
    if year % 4 == 0:
        return "True"
    else:
        return "False"
year = "2025"
year_leap = is_year_leap(int(year))
print("год " + year + ": " + year_leap)