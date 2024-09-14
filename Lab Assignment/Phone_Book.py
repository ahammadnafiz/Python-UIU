import os

contact_file = 'contacts.txt'

def load_contacts():
    contacts = [] # For the whole code we are working with this list of dictionary
    if os.path.exists(contact_file):
        with open(contact_file, 'r') as data:
            for line in data: # this loop work for the 1st time when we execute the programe
                contact = eval(line.strip())  # Using eval to convert the string to a dictionary
                # But in the meantime when we read the string dictionary from the file we have to
                # convert it into dictionary bcz in the later code we are playing with the dictonary
                contacts.append(contact)
    return contacts # 1st it returns a empty list


def save_contacts(contacts):
    with open(contact_file, 'w') as data:
        for contact in contacts:
            data.write(f'{contact}\n')  # Convert dictionary to string and write to file
            # Because we can't write dictionary into a file


def get_non_empty_value(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        else:
            print("Name or Number cannot be empty. Please enter a valid description.")


def add_new_contact(contacts):
    contact_name = get_non_empty_value("Enter the contact's name: ")
    contact_number = get_non_empty_value("Enter the contact number: ")

    # Create a dictionary for the new contact
    new_contact = {'name': contact_name, 'number': contact_number}

    # Append the new contact to the list of contacts
    contacts.append(new_contact)

    # Save the updated contacts to the file
    save_contacts(contacts)
    print('Contact Added')
    

def show_contacts(contacts):
    print("Phone Book:")
    for index, contact in enumerate(contacts, start=1):
        print(f"{index}. Name: {contact['name']}, Number: {contact['number']}")
    print()


def remove_contact(contacts):
    show_contacts(contacts)
    
    if not contacts:
        print("No contacts to remove.")
        return
    try:
        index = int(input("Enter the number of the contact to remove: ")) - 1
        if 0 <= index < len(contacts):
            removed_contact = contacts.pop(index)
            print(f"Contact '{removed_contact['name']}' removed.")
            save_contacts(contacts)
        else:
            print("Invalid index. Please enter a valid index.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")


def search_contacts(contacts):
    search_term = input("Enter the name or number to search: ").strip().lower()
    results = []

    for contact in contacts:
        if search_term in contact['name'].lower() or search_term in contact['number']:
            results.append(contact)

    if results:
        print("Search Results:")
        for index, result in enumerate(results, start=1):
            print(f"{index}. Name: {result['name']}, Number: {result['number']}")
    else:
        print("No matching contacts found.")
        
        
# Main function
def main():
    contacts = load_contacts()

    while True:
        print("Choose an action:")
        print("1. Add a new contact")
        print("2. View all contacts")
        print("3. Search for a contact")
        print("4. Remove contact")
        print("5. Exit the program")

        choice = input("Enter choice: ")

        if choice == "1":
            add_new_contact(contacts)
        elif choice == "2":
            show_contacts(contacts)
        elif choice == '3':
            search_contacts(contacts)
        elif choice == '4':
            remove_contact(contacts)
        elif choice == "5":
            print("Goodbye!")
            save_contacts(contacts)
            break
        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()
