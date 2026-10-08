# Task-04 : Contact Book

contacts = {
    "Ravi": "9876543210",
    "Arun": "9876543211",
    "Priya": "9876543212"
}

# Display contacts
for name, phone in contacts.items():
    print(name, ":", phone)

# Search
name = input("Enter name to search: ")

if name in contacts:
    print("Phone:", contacts[name])
else:
    print("Contact not found")

# Add contact
new_name = input("Enter new contact name: ")
new_phone = input("Enter phone number: ")

contacts[new_name] = new_phone

print("Contact added.")

# Update contact
update_name = input("Enter name to update: ")

if update_name in contacts:
    new_phone = input("Enter new phone number: ")
    contacts[update_name] = new_phone
    print("Contact updated.")
else:
    print("Contact not found")

# Delete contact
delete_name = input("Enter name to delete: ")

if delete_name in contacts:
    del contacts[delete_name]
    print("Contact deleted.")
else:
    print("Contact not found")