def month_to_season(month):
    if month < 1:
        month = 1
    if month > 12:
        month = 12

    if month <= 2 or month == 12:
        print("Зима")
    elif month <= 5 and month > 2:
        print("Весна")
    elif month <= 8 and month > 5:
        print("Лето")
    else:
        print("Осень")
month_to_season(10)
