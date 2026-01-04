import csv

class Contact:
    def __init__(self, name, phone_number):
        if not phone_number.isdigit():
            raise ValueError("Phone number must contain only digits")
        self.name = name
        self.phone_number = phone_number

class PhoneBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone):
        contact = Contact(name, phone)
        self.contacts.append(contact)

    def save_to_csv(self, filename):
        try:
            with open(filename, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["name", "phone_number"])
                for c in self.contacts:
                    writer.writerow([c.name, c.phone_number])
        except PermissionError:
            print("Error: You don't have permission to write to this file!")

    def load_from_csv(self, filename):
        try:
            with open(filename, "r", newline="", encoding="utf-8") as file:
                reader = csv.reader(file)
                next(reader)  
                for row in reader:
                    try:
                        self.add_contact(row[0], row[1])
                    except ValueError:
                        print(f"Invalid contact skipped: {row}")
        except FileNotFoundError:
            print("File not found, contact list is empty")
        except Exception:
            print("Error reading file, it may be corrupted")


phonebook = PhoneBook()
phonebook.load_from_csv("contacts.csv")

while True:
    print("\nMain Menu:")
    print("1. Add contact")
    print("2. Show all")
    print("3. Save and exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a number")
        continue

    if choice == 1:
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        try:
            phonebook.add_contact(name, phone)
            print(" Contact added successfully")
        except ValueError:
            print(" Invalid phone number format, try again")
    elif choice == 2:
        print("\n📋 Contact list:")
        for c in phonebook.contacts:
            print(f"{c.name} - {c.phone_number}")
    elif choice == 3:
        phonebook.save_to_csv("contacts.csv")
        print(" Saved. Goodbye!")
        break
    else:
        print(" Invalid choice, please enter 1 to 3")