hours_day_night = int(input())
day_week = input()

if 18 >= hours_day_night >= 10:
    if day_week == "Monday" or day_week == "Tuesday" or day_week == "Wednesday" or \
            day_week == "Thursday" or day_week == "Friday" or day_week == "Saturday":
        print("open")
    else:
        print("closed")
else:
    print("closed")
