import random

# print("LOTTERY")
# print("=======")
# print("Easy to Play")
# print("---")
# print("The Jackpot is won by matching all five numbers!")
# print(" ")
# print("The numbers are from 1 to 42")
# print(" ")
# print("Good luck!")

# Create the main function that will create a list of 5 random numbers every day
# Create a function that will generate a user quick pick number and compare with winning numbers


# Lottery Simulator

ticket = 0
match2 = 0
match3 = 0
match4 = 0

def lotto(lotto_list):
    count = 0
    x = random.randint(1, 43)
    while count <= 4:
        lotto_list.insert(count, x)
        x = random.randint(1, 43)
        for i in lotto_list:
            if x == i:
                lotto_list.remove(i)
                count -= 1
                break
        count += 1
    return lotto_list.sort()


while True:
    ticket += 1
    winning_list = []
    player_list = []
    match_list = []
    lotto(winning_list)
    lotto(player_list)

    print(winning_list)
    print(player_list)
    if winning_list == player_list:
        print("$$$$$$$$$$ JACKPOT $$$$$$$$$$")
        print("Odds 1 in 962,598.0")
        print("You won ---")
        print(f"You played {ticket:,} times.")
        print(f"Match 2: {match2:,} times.")
        print(f"Match 3: {match3:,} times.")
        print(f"Match 4: {match4:,} times.")
        break
    else:         
        for i in winning_list:
            if i in player_list:
                match_list.append(i)
        if len(match_list) == 1:
            print("You've matched 1 number! Good luck next time.")
            winning_list = winning_list.clear()
            player_list = player_list.clear()
            continue
        if len(match_list) == 2:
            print("You've matched 2 numbers!")
            print("Odds 1 in 11.4")
            print("YOU WON $1.")
            match2 += 1
            winning_list = winning_list.clear()
            player_list = player_list.clear()
            continue
        if len(match_list) == 3:
            print("You've matched 3 numbers!")
            print("Odds 1 in 136.9")
            print("YOU WON $5.")
            match3 += 1
            winning_list = winning_list.clear()
            player_list = player_list.clear()
            continue
        if len(match_list) == 4:
            print("You've matched 4 numbers!")
            print("Odds 1 in 5,066.0")
            print("YOU WON $250.")
            match4 += 1
            winning_list = winning_list.clear()
            player_list = player_list.clear()
            continue          