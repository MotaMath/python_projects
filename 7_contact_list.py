import os
import json
import time

# Create a list of contacts:
# Option to add, delete, view, save and load 

# Create a dictionary of contacts with keys as name and phone as values

contacts = {}

def clear(): #Function to clear the screen
    os.system("cls" if os.name == "nt" else "clear")


print("-"*20 + "CONTACTS" + "-"*20)
print(" ")
print("Phone Book")
print(" ")

def create(): # Function that asks contact name and phone, store name as key and phone as value
    create_contact = input("Name: ")
    create_phone = input("Phone: ")
    len_size = len(create_phone)
    if len_size == 10:
        create_phone = create_phone[:3] + "-" + create_phone[3:6] + "-" + create_phone[6:10]
        contacts[create_contact] = create_phone
    else:
        contacts[create_contact] = create_phone
    print(" ")
    print("New contact added!")
    print(" ")
    print("Name: {}".format(create_contact))
    print("Phone: {}".format(create_phone))
    print(" ")
    

def delete(list_name): # Use function del to delete a name from the dictionary
    if list_name in contacts:
        del contacts[list_name]
        print("Name: {} Deleted.".format(list_name))
    else:
        print("Name: {} does not exist.".format(list_name))


def view(): # For loop to print all contacts in the dictionary. sorted(contacts.items()) to sort
    print(" ")
    print("Contact list:")
    print(" ")
    for key, value in sorted(contacts.items()):
        print("Name: {}".format(key))
        print("Phone: {}".format(value))
        print(" ")


def save(): # To save the contacts dictionary in a json file
    print("Saving...")
    with open("contact_list.json", "w") as file:
        json.dump(contacts, file)
    time.sleep(2)
    print(" ")

def load(): # To load the contacts dictionary from a json file at the beginning of the program
    print("Loading...")
    with open("contact_list.json", "r") as file:
        load = json.load(file)
    contacts.update(load)
    print(" ")

def main():
    try: # Define if the json file exists
        if os.path.exists("contact_list.json"):
            load()
            print("Load completed.")
        else: # If the json file does not exist, create a new json file
            location = "C:\\Users\\mathe\\Documents\\Dev\\Python\\Python_Projects\\contact_list.json"
            json.dump(contacts, open(location, "w"))
            print("New contact list created.")
            print("Welcome to the program!")
            print(" ")
    except Exception as e:
        print(f"Error: {e}\n")
    while True:
        try:
            print(
                """
                ----------MENU----------
                
                1 - View the contact list
                2 - Create a new contact
                3 - Delete a contact
                4 - Save and Exit
                """
            )
            print("Options (1, 2, 3, 4)")
            menu = input("Select an option: ")
            if menu == "1":
                print("View the contact list selected")
                view()
            elif menu == "2":
                print("Create a new contact selected")
                create()
            elif menu == "3":
                print("Delete a contact selected")
                list_name = input("Name: ")
                delete(list_name)
            elif menu == "4":
                print("Save and Exit selected")
                print(" ")
                save()
                print("Automatically saved!")
                print(" ")
                input("Press ENTER to Exit ")
                quit()
            else:
                print(" ")
                print("Invalid option, try again (1/2/3/4)")
                print(" ")
        except Exception as e:
            print(e)
            continue
            
            

if __name__ == "__main__":
    main()
