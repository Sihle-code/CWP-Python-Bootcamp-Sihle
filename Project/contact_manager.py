# CONTACT MANAGER USING A DICTIONARY

contacts = {}

while True:
    print("\n--- Contact Manager ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Choose an option: ")

    # ADD CONTACT
    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")

        contacts[name] = phone
        print(f"{name} added successfully!")

    # VIEW CONTACTS
    elif choice == "2":
        if contacts:
            print("\nContacts List:")

            for name, phone in contacts.items():
                print(f"{name}: {phone}")
        else:
            print("No contacts found.")

    # SEARCH CONTACT
    elif choice == "3":
        search_name = input("Enter contact name to search: ")

        if search_name in contacts:
            print(f"{search_name}'s number is {contacts[search_name]}")
        else:
            print("Contact not found.")

    # DELETE CONTACT
    elif choice == "4":
        delete_name = input("Enter contact name to delete: ")

        if delete_name in contacts:
            del contacts[delete_name]
            print(f"{delete_name} deleted successfully.")
        else:
            print("Contact not found.")

    # EXIT PROGRAM
    elif choice == "5":
        print("Exiting Contact Manager...")
        break

    else:
        print("Invalid option. Please try again.")