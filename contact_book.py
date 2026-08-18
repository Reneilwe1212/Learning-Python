#contact = [{'name':'Rere','phone':'0724635219', 'email': 'khanyilwe@gmail.com'},{'name':'leredi','phone':'0724685219', 'email': 'khanyi524@gmail.com'}, {'name':'Zirast','phone':'0728955219', 'email': 'lebo58@gmail.com'}, {'name':'Mosa','phone':'0758962145', 'email': 'kmosae@gmail.com'}, {'name':'Lilo','phone':'0724635259', 'email': 'Nuna@gmail.com'}]
contacts = []
#add contact
# More practice
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)
    print(f"{name} added successfully!\n")


def search_contact(name):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            return contact
        
        return None


def delete_contact(name):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            print(f"{name} deleted successfully! \n")
            return
    print("Contact not found!\n")


def view_all():
    if not contacts:
        print("No contacts available.\n")
        return
    print("\n======Contact List=========")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    print()


def menu():
    while True:
        print("=== Contact Book======")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. View All Contacts")
        print("5. Exit")


        choice = input("Choose an option (1-5):")


        if choice == "1":
            add_contact()
        elif choice == "2":
            name = input("Enter name to search: ")
            contact = search_contact(name)
            if contact:
                print(f"Found: Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}\n")
            else:
                print("Contact not found.\n")
        elif choice == "3":
            name = input("Enter name to delete: ")
            delete_contact(name)
        elif choice == "4":
            view_all()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    menu()