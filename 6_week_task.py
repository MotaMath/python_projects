import json
import os
import time

# Week tasks
# Print the 7 days
# Create a menu to add, delete for each day
# Add to a database
# Save and load options

print(
"""


__________WEEK TASK__________


"""
)

# Define the week dictionary
week = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": [], "Saturday": [], "Sunday": []}

def clear(): # Function to clear the screen
    os.system("cls" if os.name == "nt" else "clear")
    
def create():
    print(
    """
    1 - Monday
    2 - Tuesday
    3 - Wednesday
    4 - Thursday
    5 - Friday
    6 - Saturday
    7 - Sunday    
    """
    )
    while True:
        day = input("Select the day: ")
        if day in ("1", "2", "3", "4", "5", "6", "7"):
            task = input("What is the task?: ")
            if day == "1":
                week["Monday"].append(task) #Add a new item in list, inside week dictionary
                print(" ")
                print("New task Added!")
                break
            elif day == "2":
                week["Tuesday"].append(task)
                print(" ")
                print("New task Added!")
                break
            elif day == "3":
                week["Wednesday"].append(task)
                print(" ")
                print("New task Added!")
                break
            elif day == "4":
                week["Thursday"].append(task)
                print(" ")
                print("New task Added!")
                break
            elif day == "5":
                week["Friday"].append(task)
                print(" ")
                print("New task Added!")
                break
            elif day == "6":
                week["Saturday"].append(task)
                print(" ")
                print("New task Added!")
                break
            elif day == "7":
                week["Sunday"].append(task)
                print(" ")
                print("New task Added!")
                break
        else:
            print("Invalid input! (1, 2, 3, 4, 5, 6, 7)")

def delete():
    clear()
    print(
    """
    1 - Monday
    2 - Tuesday
    3 - Wednesday
    4 - Thursday
    5 - Friday
    6 - Saturday
    7 - Sunday    
    """
    )
    while True:
        # Select delete all days or just each day
        complete = input("Do you want to delete all tasks? (Y/N): ").lower()
        if complete == "y":
            week["Monday"].clear()
            week["Tuesday"].clear()
            week["Wednesday"].clear()
            week["Thursday"].clear()
            week["Friday"].clear()
            week["Saturday"].clear()
            week["Sunday"].clear()
            time.sleep(1)
            print("All tasks removed!")
            break
        else:
            if complete == "n":
                remove = input("Which day do you want to delete?: ")
                if remove in ("1", "2", "3", "4", "5", "6", "7"):
                    if remove == "1":
                        week["Monday"].clear()
                        break
                    elif remove == "2":
                        week["Tuesday"].clear()
                        break
                    elif remove == "3":
                        week["Wednesday"].clear()
                        break
                    elif remove == "4":
                        week["Thursday"].clear()
                        break
                    elif remove == "5":
                        week["Friday"].clear()
                        break
                    elif remove == "6":
                        week["Saturday"].clear()
                        break
                    elif remove == "7":
                        week["Sunday"].clear()
                        break
                    print("Tasks removed!")
                else:
                    print("Invalid input! (1, 2, 3, 4, 5, 6, 7)")
            else:
                print("Invalid input! (Y/N)")
                continue

def view_task():
    clear()
    print("((((((((((((((((((()))))))))))))))))))\n")
    # Print the days
    for i,t in enumerate(week, start=1):
        print(f"{i} - {t}")
        for i,t in enumerate(week[t], start=1):
            print(f"     # {t}")

def save():
    # To save the week task in a json file
    print("Saving...")
    with open("week.json", "w") as file:
        json.dump(week, file)
    time.sleep(2)
    print("Saved!")

def load():
    # To load the week task from a json file at the beginning of the program
    print("Loading...")
    with open("week.json", "r") as file:
        loaded = json.load(file)
    week.update(loaded)
    print("OK!!!")
    print(" ")

def main():
    try: # Define if the json file exists
        if os.path.exists("week.json"):
            load()
            print("Load completed.")
        else:
            location = "C:\\Users\\mathe\\Documents\\Dev\\Python\\Python_Projects\\week.json"
            json.dump(week, open(location, "w"))
            print("Welcome to the program!")
            print(" ")
    except Exception as e:
        print(f"Error: {e}\n")
        
    while True:
            print(
"""

-----------------MENU-----------------

1 - View tasks
2 - Create new task
3 - Delete tasks
4 - Exit and Save
"""
            )
            menu = input("Select: ")
            if menu == "1":
                print("View tasks selected")
                view_task()
            if menu == "2":
                print("Create new task selected")
                create()
            if menu == "3":
                print("Delete tasks selected")
                delete()
            if menu == "4":
                print(" ")
                print("OK!!!")
                print("Thanks for using the program!")
                save()
                input("Press ENTER Exit: ")
                quit()

        
if __name__ == "__main__":
    main()