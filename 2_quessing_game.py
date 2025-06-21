import random

# Guess the Number Game

print("Welcome!")
print(" ")
print("Guess the Number Game")
print("_____________________")
print(" ")
print("Good luck!")
print(" ")

#Function that asks if player wants to play again
def again():
    while True:
        again = input("Do you want to play again? (Y/N)? ")
        again = again.lower()
        if again in ("y", "n"):
            if again == "y":
                print("OK!")
                print(" ")
                main()
                continue
            if again == "n":
                print("OK! Thank you for playing.")
                input("Bye-bye ")
                quit()
        else:
            print("You need to type 'Y' or 'N' to continue.")
            continue

#Function that gets a random number, ask a number until player guess the right number
def main():
    while True:
        number = random.randint(0, 100)

        guess = 1


        while True:
            try:
                question = input("Guess a number from 0 to 100: ")
                question = int(question)
                if question == number:
                    print(" ")
                    print("Good job, you guessed the correct number.")
                    print(" ")
                    print("You guessed in {} turns."   .format(guess))
                    print("Good job!")
                    print(" ")
                    again()
                    break
                elif question < number:
                    guess += 1
                    print("Wrong number, too low, try another one.")
                    print(" ")
                    continue
                elif question > number:
                    guess += 1
                    print("Wrong number, too high, try another one.")
                    print(" ")
                    continue
            except ValueError:
                print("Only type numbers from 0 to 100.")
                continue

if __name__ == "__main__":
    main()