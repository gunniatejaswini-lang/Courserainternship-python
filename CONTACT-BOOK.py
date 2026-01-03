# Contact Book Application

contacts = {}

def show_menu():
    print("\n====== CONTACT BOOK ======")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    print("==========================")

def add_contact():
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email: ").strip()
    address = input("Enter Address: ").strip()

    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts available.")
        return

    print("\nContact List:")
    print("-------------------------")
    for name, details in contacts.items():
        print(f"Name: {name} | Phone: {details['phone']}")

def search_contact():
    search = input("Enter Name or Phone Number to search: ").strip()

    found = False
    for name, details in contacts.items():
        if search.lower() == name.lower() or search == details["phone"]:
            print("\nContact Found:")
            print(f"Name    : {name}")
            print(f"Phone   : {details['phone']}")
            print(f"Email   : {details['email']}")
            print(f"Address : {details['address']}")
            found = True
            break

    if not found:
        print("Contact not found.")

def update_contact():
    name = input("Enter contact name to update: ").strip()

    if name in contacts:
        print("Enter new details (leave blank to keep old value)")
        phone = input("New Phone Number: ").strip()
        email = input("New Email: ").strip()
        address = input("New Address: ").strip()

        if phone:
            contacts[name]["phone"] = phone
        if email:
            contacts[name]["email"] = email
        if address:
            contacts[name]["address"] = address

        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter contact name to delete: ").strip()

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

# Main Program
while True:
    show_menu()
    choice = input("Choose an option (1-6): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")

