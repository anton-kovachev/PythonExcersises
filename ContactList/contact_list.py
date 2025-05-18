import json


CONTACT_FILE_PATH = "contacts.json"

class Contact:
    def __init__(self, first_name, last_name, mobile_phone = None, home_phone = None, email_address = None, address = None):
        self.first_name = first_name
        self.last_name = last_name
        self.mobile_phone = mobile_phone
        self.home_phone = home_phone
        self.email_address = email_address
        self.address = address 
        
    def __eq__(self, other):
        return self.first_name == other.first_name and self.last_name == other.last_name
    
    def __str__(self):
        return f"First Name: {self.first_name} Last Name: {self.last_name}\n    Mobile: {self.mobile_phone}\n    Email: {self.email_address}"
    
    def toJSON(self):
        return json.dumps(self, default=lambda x: x.__dict__, sort_keys=True, indent=4)


def read_contacts(file_path):
    try:
        with open(file_path, 'r') as f:
            contacts = [Contact(**c) for c in json.load(f)['contacts']]
    except FileNotFoundError:
        contacts = []
    except json.JSONDecodeError:
        contacts = []

    return contacts


def write_contacts(file_path, contacts):
    with open(file_path, 'w') as f:
        contacts = {"contacts": contacts}
        json.dump(contacts, f, default=vars)


def verify_email_address(email):
    if "@" not in email:
        return False

    split_email = email.split("@")
    identifier = "".join(split_email[:-1])
    domain = split_email[-1]

    if len(identifier) < 1:
        return False

    if "." not in domain:
        return False

    split_domain = domain.split(".")

    for section in split_domain:
        if len(section) == 0:
            return False

    return True


def add_contact(contacts):
    contact_list = read_contacts(CONTACT_FILE_PATH)
    contact_list.extend(contacts)
    write_contacts(CONTACT_FILE_PATH, contact_list)
        


def search_for_contact(contact):
    contacts = read_contacts(CONTACT_FILE_PATH)
    return list(filter(lambda x: contact.first_name in x.first_name and contact.last_name in contact.last_name, contacts))

def delete_contact(contact):
    contacts = read_contacts(CONTACT_FILE_PATH)
    contacts.remove(contact)
    write_contacts(CONTACT_FILE_PATH, contacts)

def find_contact(contact_to_delete):
    contacts = read_contacts(CONTACT_FILE_PATH)
    idx = -1
    
    try:
        idx = contacts.index(contact_to_delete)
    except ValueError:
        return None    
   
    if idx >= 0:
        return contacts[idx] 
    
    return None


def list_contacts(contacts):
    contact_list = read_contacts(CONTACT_FILE_PATH)
    for contact in contact_list:
        print(str(contact))


def enter_command():
    command = input("Type a command: ")

    if command == "add":
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        mobile_phone_number = input("Mobile Phone Number: ")
        home_phone_number = input("Home Phone Number: ")
        email_address = input("Email Address: ")
        address = input("Address: ")

        if first_name is None or first_name == "":
            print("First Name is required!")
            enter_command()

        if last_name is None or last_name == "":
            print("Last Name is required!")
            enter_command()
            
        if mobile_phone_number is not None and mobile_phone_number is not "" and not mobile_phone_number.isdigit():
            print("Please enter a valid mobile phone number!")
            enter_command()
            
        if home_phone_number is not None and home_phone_number is not "" and not home_phone_number.isdigit():
            print("Please enter a valid home phone number!")
            enter_command()

        new_contact = Contact(first_name, last_name, mobile_phone_number, home_phone_number, email_address, address)
        print(new_contact.__dict__)
        add_contact([new_contact])   
    elif command == "delete":
        first_name = input("First Name: ")
        last_name = input("Last Name: ")

        if first_name is None or first_name == "":
            print("First Name is required!")
            enter_command()

        if last_name is None or last_name == "":
            print("Last Name is required!")
            enter_command()
            
        contact_to_delete = Contact(first_name, last_name)            
        contact_to_delete = find_contact(contact_to_delete)

        if contact_to_delete is None:
            print("No contact with this name exists")
        else:
            confirmation = input("Are you sure you want to delete this contact Y/N: ")
            if confirmation.lower() == "y":
                delete_contact(contact_to_delete)
                print("Contact is deleted!")
    elif command == "search":
        first_name = input("First Name: ")
        last_name = input("Last Name: ")

        if (first_name is None or first_name == "") or (last_name is None or last_name == ""):
            print("First Name or Last Name is required!")
            enter_command()
        
        contact_to_search_for = Contact(first_name if first_name is not None else "", last_name if last_name is not None else "")           
        found_contacts = search_for_contact(contact_to_search_for)
        
        print(f"Found {len(found_contacts)} contacts")
        for c in found_contacts:
            print(c)
            
    elif command == "list":
        list_contacts([])
    elif command == "q":
        print("Bye")
        return
    else:
        print("Please enter a valid command!")
    
    enter_command()
        


def main(contacts_path):
    print("Welcome to your contact list!")
    print("The following is a list of useable commands:")
    print("\"add\": Adds a contact.")
    print("\"delete\": Deletes a contact.")
    print("\"list\": List all contacts.")
    print("\search\": Search all contacts.")
    print("\"q\": Quits the program and save the contact list.")
    enter_command()

if __name__ == "__main__":
    main(CONTACT_FILE_PATH)
