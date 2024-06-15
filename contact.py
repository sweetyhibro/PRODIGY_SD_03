# Function to add a new contact
def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    print("Contact added successfully!")

# Function to view all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        for idx, contact in enumerate(contacts):
            print(str(idx + 1) + ". Name: " + contact['name'] + ", Phone: " + contact['phone'] + ", Email: " + contact['email'])

# Function to edit an existing contact
def edit_contact(contacts):
    view_contacts(contacts)
    if contacts:
        try:
            index = int(input("Enter the number of the contact to edit: ")) - 1
            if 0 <= index < len(contacts):
                print("Enter new name (current: {})".format(contacts[index]['name']))
                contacts[index]['name'] = input()
                print("Enter new phone number (current: {})".format(contacts[index]['phone']))
                contacts[index]['phone'] = input()
                print("Enter new email address (current: {})".format(contacts[index]['email']))
                contacts[index]['email'] = input()
                print("Contact updated successfully!")
            else:
                print("Invalid contact number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Function to delete a contact
def delete_contact(contacts):
    view_contacts(contacts)
    if contacts:
        try:
            index = int(input("Enter the number of the contact to delete: ")) - 1
            if 0 <= index < len(contacts):
                contacts.pop(index)
                print("Contact deleted successfully!")
            else:
                print("Invalid contact number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Main function to run the contact management program
def main():
    contacts = []
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
