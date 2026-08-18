contacts = {"Lebo": "0754269842",
            "Una": "0875695246",
            "Glen": "0654854842"}

name = input("Enter the name: ")

if name in contacts:
    print(f"Found! {name}'s number is {contacts[name]}")
else:
    print("Contact not found.")

range(1,11)

for char in 'HI':
    print(char)