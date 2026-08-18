first_name = input("My name is : ")
surname = input("My surname is : ")
age = int(input("I am : "))
favorite_number = float(input("My favorite number is : "))

full_name = f"{first_name} {surname}"
#print(f"Welcome, [{first_name.upper()} {surname}]!")
print(f"Welcome, [{full_name.upper()}]!")
print("The title is " + full_name.title())

age_in_months = (age) * 12
print(f"My age in Months :{age_in_months}")

decimal_number = round(favorite_number, 2)
print(f"Favorite number to the nearest 2 decimal : {decimal_number}")

#Data types
print("/nData types")
print("First name : ",type(first_name))
print("surname : ", type(surname))
print("Age : ",type(age))
print("Favorite number : ",type(favorite_number))
