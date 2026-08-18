bank_balance = 500

withdraw = int(input("How much do you want to withdraw? "))

if 0 < withdraw <= bank_balance:
    bank_balance -= withdraw
    print(f"Withdrawal successful! Remaining balance: R{bank_balance}")
elif withdraw <= 0:
    print("Invalid amount! You must withdraw more than R0")
else:
    print("Declined. Insuffcient funds")
