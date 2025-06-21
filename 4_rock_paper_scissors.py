import random

# Player VS computer - Rock, Paper, Scissors Game

print("Welcome to Rock, Paper, Scissors Game.")
print("______________________________________")
print(" ")
print(" ")


def main():
    user_points = 0
    computer_points = 0
    while True:
        question = input("Type Rock / Paper / Scissors, or Exit to end the game: ")
        question = question.lower()
        if question == "exit":
            print(" ")
            break
        
        if question not in ("rock", "paper", "scissors"):
            if question == "exit":
                print(" ")
                break
            else:
                print("Invalid, Try again.")
                print(" ")
                continue
        
        options = ["0", "rock", "paper", "scissors"]
        random1 = random.randint(1, 3)
        computer = options[random1]
        
        if question == "rock" and computer == "scissors":
            print("You play Rock and the computer plays Scissors")
            print("You WON!")
            print(" ")
            user_points += 1
            continue
        elif question == "paper" and computer == "rock":
            print("You play Paper and the computer plays Rock")
            print("You WON!")
            print(" ")
            user_points += 1
            continue
        elif question == "scissors" and computer == "paper":
            print("You play Scissors and the computer plays Paper")
            print("You WON!")
            print(" ")
            user_points += 1
            continue
        else:
            print("Computer plays {}.".format(computer))
            print("You LOST!")
            print(" ")
            computer_points += 1
            continue
        
    print("You won {} times.".format(user_points))
    print("The computer won {} times.".format(computer_points))

if __name__ == "__main__":
    main()

print(" ")
print("Thank you for playing!")
input("Press ENTER to Exit!")
quit()