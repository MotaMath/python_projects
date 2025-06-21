import time
import login



print("Welcome to Password Manager")
print(" ")
print("Save your passwords here.")
print(
    """
    __________________SAFE__________________
    """
)
time.sleep(1)

#To check if file exist, if not, create one.
try:
    file = open("bit.txt", 'r')
    file.close()
    print("File already exist.")
except:
    file = open("bit.txt", "a")
    file.close()
    print('File was successfully created.')

#Function to add new line to file
def add():
    login = input("Add new login: ")
    password = input("Add new password: ")
    date = time.ctime()
    file = open("bit.txt", "a")
    file.write("Login: " + login + " | " + " Password: " + password + " | " + date + "\n")
    file.close()

#Function to read the file
def read():
    file = open("bit.txt", "r")
    print(file.read())
    time.sleep(2)
    file.close()

#Menu
def main():
    login.menu_login()
    while True:
        time.sleep(1)
        print(
            """
            ----------MENU----------

            1 - ADD new Login/Password
            2 - READ Login/Password
            3 - Exit
            """
        )
        question = input("Choose one option (1/2/3): ")
        if question == "1":
            print(" ")
            add()
        elif question == "2":
            print(" ")
            read()
        elif question == "3":
            print("Thank you!")
            print(" ")
            print("Automatically saved!")
            print(" ")
            input("Press ENTER to Exit ")
            quit()
        else:
            print(" ")
            print("Invalid option, try again (1/2/3)")
            print(" ")

if __name__ == "__main__":
    main()
    

# #Move a file (import os)
# source = "text.txt"
# destination = "C:\\Users\\mathe\\text.txt"
# try:
#     if os.path.exists(destination):
#         print("File is there")
#     else:
#         os.replace(source, destination)
#         print("Moved")
# except:
#     print(source + "was not found")