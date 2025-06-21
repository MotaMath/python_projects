import keyboard
import random
import time
import os

#----------------------------------------------------------------
#The time needed to find a random number

adding = 0

#Randomly generate a number
def find():
    rand = random.randint(0, 12345)
    return rand 

#Return the processing time
def tm():
    total = stop_time - s_time
    if total > 60:
        minute = total / 60
        seconds = total % 60
        if minute == 1:
            return print(f"Time to find: {int(minute)} minute and {int(seconds)} seconds.")
        else:
            return print(f"Time to find: {int(minute)} minutes and {int(seconds)} seconds.")
    else:
        return print(f"Time to find: {total:.1f} seconds.")


#Main loop
rand = find()
s_time = time.time()

print("----------------\nF1 and F2 to quit\n---------------")
print("Finding a number between 0 and 123456789")
print(f"The number is: {rand:,}")
print(" ")
print("Initializing in 5 seconds")  
time.sleep(5)

while True:
    adding += 1
    print(f"{adding:,}") #To print a number with ","
    if adding == rand:
        print(f"Number found: {adding:,}")
        stop_time = time.time()
        tm()
        break    
    #Keyboard.is_pressed(" ") to program hot keys
    if keyboard.is_pressed("f1") and keyboard.is_pressed("f2"):
        quit()    
        
