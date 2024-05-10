# град / продукт	coffee	water	beer	sweets	peanuts
# Sofia	              0.50	 0.80	1.20	1.45	1.60
# Plovdiv	          0.40	 0.70	1.15	1.30	1.50
# Varna	              0.45	 0.70	1.10	1.35	1.55
product = input()
name_city = input()
quantity = float(input())

result = 0.0

if name_city == "Sofia":
    if product == "coffee":
        result = 0.50
    elif product == "water":
        result = 0.80
    elif product == "beer":
        result = 1.20
    elif product == "sweets":
        result = 1.45
    elif product == "peanuts":
        result = 1.60
if name_city == "Plovdiv":
    if product == "coffee":
        result = 0.40
    elif product == "water":
        result = 0.70
    elif product == "beer":
        result = 1.15
    elif product == "sweets":
        result = 1.30
    elif product == "peanuts":
        result = 1.50
if name_city == "Varna":
    if product == "coffee":
        result = 0.45
    elif product == "water":
        result = 0.70
    elif product == "beer":
        result = 1.10
    elif product == "sweets":
        result = 1.35
    elif product == "peanuts":
        result = 1.55

print(result * quantity)
