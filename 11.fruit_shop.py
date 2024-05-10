fruit = input()
day_week = input()
quantity = float(input())

price_fruit = 0.0

if day_week == "Monday" or day_week == "Tuesday" or day_week == "Wednesday" or \
        day_week == "Thursday" or day_week == "Friday":
    if fruit == "banana":
        price_fruit = 2.50
    elif fruit == "apple":
        price_fruit = 1.20
    elif fruit == "orange":
        price_fruit = 0.85
    elif fruit == "grapefruit":
        price_fruit = 1.45
    elif fruit == "kiwi":
        price_fruit = 2.70
    elif fruit == "pineapple":
        price_fruit = 5.50
    elif fruit == "grapes":
        price_fruit = 3.85
    else:
        print("error")
        exit()
elif day_week == "Saturday" or day_week == "Sunday":
    if fruit == "banana":
        price_fruit = 2.70
    elif fruit == "apple":
        price_fruit = 1.25
    elif fruit == "orange":
        price_fruit = 0.90
    elif fruit == "grapefruit":
        price_fruit = 1.60
    elif fruit == "kiwi":
        price_fruit = 3.00
    elif fruit == "pineapple":
        price_fruit = 5.60
    elif fruit == "grapes":
        price_fruit = 4.20
    else:
        print("error")
        exit()
else:
    print("error")
    exit()  # end execution code
print(f"{price_fruit * quantity:.2f}")
