import time
import os

def clear(): #Function to clear the screen
    os.system("cls" if os.name == "nt" else "clear")

def bar_left(count, clock):
    #Arguments 
    #count: number of characters in the progress bar
    #clock: time between each character
    bar = "#"
    space = " "
    empty = 2

    while True:
        time.sleep(clock)
        print(f"[{bar * count}{space * empty}]",end='\r')
        count -= 2
        empty += 2
        if count == 0:
            clear()
            print("Done!")
            break
    

def bar_right(plus, clock):
    #Arguments
    #plus: number of characters in the progress bar
    #clock: time between each character
    bar = "#"
    count = 2
    space = " "

    while True:
        time.sleep(clock)
        print(f"[{bar * count}{space * plus}]",end='\r')
        count += 2
        plus -= 2
        if count == 90:
            clear()
            print("Done!")
            break

bar_left(100, 0.1)
print("Next")
bar_right(100, 0.1)