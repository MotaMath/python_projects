#import hashlib

user_main = "admin"
pwd_main = "admin"

def log_in():
    user_login = input("Enter username: ")
    pwd_login = input("Enter password: ")
    try:
        if user_main == user_login and pwd_main == pwd_login:
            print("Logged in Successfully!")
            #Access the program here!
            input("press any key to continue...")
        else:
            print("Login failed! \n")
            quit()
    except:
        print("authorized user only.\n")
        quit()

def menu_login():
    print("For security reasons, you need to log in to use this program. \n")
    print("ENTER your credentials to continue. \n")
    log_in()
    