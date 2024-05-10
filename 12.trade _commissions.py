name_city = input()
sales_volume = float(input())

trade_commission = 0.0

if name_city == "Sofia":
    if 0 <= sales_volume <= 500:
        trade_commission = 0.05
    elif 500 <= sales_volume <= 1000:
        trade_commission = 0.07
    elif 1000 <= sales_volume <= 10000:
        trade_commission = 0.08
    elif 10000 < sales_volume:
        trade_commission = 0.12
    else:
        sales_volume = "false"

elif name_city == "Varna":
    if 0 <= sales_volume <= 500:
        trade_commission = 0.045
    elif 500 <= sales_volume <= 1000:
        trade_commission = 0.075
    elif 1000 <= sales_volume <= 10000:
        trade_commission = 0.1
    elif 10000 < sales_volume:
        trade_commission = 0.13
    else:
        sales_volume = "false"

elif name_city == "Plovdiv":
    if 0 <= sales_volume <= 500:
        trade_commission = 0.055
    elif 500 <= sales_volume <= 1000:
        trade_commission = 0.08
    elif 1000 <= sales_volume <= 10000:
        trade_commission = 0.12
    elif 10000 < sales_volume:
        trade_commission = 0.145
    else:
        sales_volume = "false"
else:
    name_city = "false"

if name_city == "false" or sales_volume == "false":
    print("error")
else:
    print(f"{trade_commission * sales_volume:.2f}")
