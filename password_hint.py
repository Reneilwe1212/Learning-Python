#1
password = input("Enter your password: ")
#2
password = password.strip()
#3
first_letter = password[0]
last_letter = password[-1]
#4
print(f"Your password starts with {first_letter.upper()} and it end with {last_letter.upper()}.")


