import os
import sys


class Contact:
    def __init__(self, name: str, phone: str):
        self.name = name
        self.phone = phone

    def __str__(self):
        return f'{self.name} : {self.phone}'

    def get_name(self):
        return self.name

    def get_phone(self):
        return self.phone

    def set_name(self, name: str):
        self.name = name

    def set_phone(self, phone: str):
        self.phone = phone


class ContactManager:
    @staticmethod
    def add_contact(contacts: list, contact: Contact) -> list:
        """
        Append a new contact to a supplied list of contacts
        """
        contacts.append(contact)
        return contacts

    @staticmethod
    def get_contact(contacts: list, name: str) -> Contact:
        """
        Search a list of contacts by contact name and return the contact if found
        """
        for contact in contacts:
            if contact.name == name:
                return contact

    @staticmethod
    def delete_contact(contacts, name: str) -> Contact:
        """
        Delete a contact from a list of contacts and return the popped contact if found
        """
        i = 0
        for contact in contacts:
            if contact.name == name:
                return contacts.pop(i)
            i += 1


def clear_screen():
    """
    Clear the console
    """
    user_os = sys.platform
    if user_os == 'win32':
        os.system('cls')
    else:
        os.system('clear')


def menu():
    """
    Display the menu system
    """
    print('======================')
    print('| 1: Add Contact     |')
    print('| 2: Search Contact  |')
    print('| 3: Delete Contact  |')
    print('| 4: Print Contacts  |')
    print('| 5: Quit            |')
    print('======================')


def main():
    is_running = True
    contacts: list = []
    cm = ContactManager()

    while is_running:
        menu()
        command = input('Make Selection: ')
        match command:
            # ADD A CONTACT
            case '1':
                clear_screen()
                name = input('Enter name: ')
                phone = input('Enter phone: ')
                contacts = cm.add_contact(contacts, Contact(name, phone))
                clear_screen()
                print('Contact Added\n')
            # CONTACT SEARCH
            case '2':
                clear_screen()
                name = input('Enter name to find: ')
                contact = cm.get_contact(contacts, name)
                clear_screen()
                if contact is not None:
                    print(contact)
                    print()
                else:
                    print('Contact not found\n')
            # DELETE CONTACT
            case '3':
                clear_screen()
                name = input('Enter name to delete: ')
                clear_screen()
                popped_contact = cm.delete_contact(contacts, name)
                if popped_contact is not None:
                    print(f'{popped_contact} was deleted\n')
                else:
                    print('Contact was not found\n')
            # PRINT CONTACTS
            case '4':
                clear_screen()
                if len(contacts) == 0:
                    clear_screen()
                    print('There are no contacts')
                else:
                    for contact in contacts:
                        print(contact)
                print()
            # QUITE APPLICATION
            case '5':
                clear_screen()
                print('GoodBye')
                is_running = False


main()
