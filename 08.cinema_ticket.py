day_week = input()

price_ticket_cinema = 0

if day_week == "Monday" or day_week == "Tuesday" or day_week =="Friday":
    print(12)
elif day_week == "Wednesday" or day_week == "Thursday":
    print(14)
elif day_week == "Saturday" or day_week == "Sunday":
    print(16)
