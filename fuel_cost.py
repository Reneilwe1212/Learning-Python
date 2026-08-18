kilometers = float(input("How many kilometers do you want to drive? "))
price = float(input("How much is your petrol price per liter? "))

liters_needed = kilometers / 10

cost = liters_needed * price

print(f"Kilometers: {kilometers} km")
print(f"Litters needed: {liters_needed} L")
print(f"Total cost: R{round(cost, 2)} ")