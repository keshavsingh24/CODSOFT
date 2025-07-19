def print_menu():
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def add_contact(contacts):
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    contacts.append({
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    })
    print("Contact added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    print("\nContact List:")
    for idx, contact in enumerate(contacts, 1):
        print(f"{idx}. {contact['name']} | {contact['phone']}")

def search_contact(contacts):
    keyword = input("Enter name or phone number to search: ").lower()
    found = False
    for contact in contacts:
        if keyword in contact['name'].lower() or keyword in contact['phone']:
            print("\nContact Found:")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            found = True
    if not found:
        print("No matching contact found.")

def update_contact(contacts):
    keyword = input("Enter name or phone number of the contact to update: ").lower()
    for contact in contacts:
        if keyword in contact['name'].lower() or keyword in contact['phone']:
            print("Leave field blank to keep current value.")
            name = input(f"New Name [{contact['name']}]: ") or contact['name']
            phone = input(f"New Phone [{contact['phone']}]: ") or contact['phone']
            email = input(f"New Email [{contact['email']}]: ") or contact['email']
            address = input(f"New Address [{contact['address']}]: ") or contact['address']
            contact.update({'name': name, 'phone': phone, 'email': email, 'address': address})
            print("Contact updated successfully!")
            return
    print("Contact not found.")

def delete_contact(contacts):
    keyword = input("Enter name or phone number of the contact to delete: ").lower()
    for i, contact in enumerate(contacts):
        if keyword in contact['name'].lower() or keyword in contact['phone']:
            confirm = input(f"Are you sure you want to delete {contact['name']}? (y/n): ")
            if confirm.lower() == 'y':
                contacts.pop(i)
                print("Contact deleted.")
            else:
                print("Deletion cancelled.")
            return
    print("Contact not found.")

def main():
    contacts = []
    print("Welcome to the Contact Book!")
    while True:
        print_menu()
        choice = input("Choose an option (1-6): ")
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
