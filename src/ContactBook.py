from Contact import Contact

class ContactBook:

    contacts = []

    def add_contact():
        print("Please enter contact information")
        first_name = input("First name: ")
        last_name = input("Last name: ")
        phone = input("Phone: ")
        email = input("Email: ")

        new_contact = Contact(first_name, last_name, phone, email)

        contacts.append(new_contact)

    def display_contacts():
        for contact in contacts:
            info = contact.get_info()

            print("**********")
            print(contact.get_name())
            print("**********")

            print("ID: " + info.id)
            print("First name: " + info.first_name)
            print("Last name: " + info.last_name)
            print("Phone: " + info.phone)
            print("Email: " + info.email)

            print("============================")