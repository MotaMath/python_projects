# Simple English Grammar Test

print("Welcome to English Grammar Level Test")
print("_____________________________________")
print(" ")
print("There are 10 questions in this grammar test.")
print(" ")
print("_____________________________________")
print(" ")

#Function that defines the questions:
def main():
    while True:
        start = input("Do you want to start? Answer (Y/N): ")
        start = start.lower()
        if start == "y":
            print(" ")
            print("OK! Let's start.")
            print("Read the question and select the correct answer. (1/2/3/4)")
            print("Answer all the questions and get your result at the end.")
            print(" ")
            break
        if start == "n":
            print(" ")
            print("Ok. Bye!!")
            input(" ")
            quit()
        else:
            print(" ")
            print("You need to type 'Y' or 'N' to continue")
            print(" ")
            continue

    test = 0

    print("Question 1")
    print(" ")
    print("Where______he work?")
    print(" ")
    print("1 - is")
    print("2 - does")
    print("3 - do")
    print("4 - don't")
    print(" ")

    question1 = input("Your answer. (1/2/3/4): ")
    if question1 == "2":
        print("Next question!")
        print(" ")
        test += 1
    else:
        print("Next question!")
        print(" ")


    print("Question 2")
    print(" ")
    print("I spend too much time_____. I'd like_____more time to myself and my family.")
    print(" ")
    print("1 - working ... having")
    print("2 - to work ... having")
    print("3 - working ... to have")
    print("4 - to work .. to have")
    print(" ")

    question2 = input("Your answer. (1/2/3/4): ")
    if question2 == "3":
        print("Next question!")
        print(" ")
        test += 1
    else:
        print("Next question!")
        print(" ")


    print("Question 3")
    print(" ")
    print("I_____to Germany last year.")
    print(" ")
    print("1 - went")
    print("2 - gone")
    print("3 - go to")
    print("4 - go")
    print(" ")

    question3 = input("Your answer. (1/2/3/4): ")
    if question3 == "1":
        print("Next question!")
        print(" ")
        test += 1
    else:
        print("Next question!")
        print(" ")


    print("Question 4")
    print(" ")
    print("That smells good! What_____.")
    print(" ")
    print("1 - are you cook?")
    print("2 - do you cook?")
    print("3 - are you cooking?")
    print("4 - do you cooking?")
    print(" ")

    question4 = input("Your answer. (1/2/3/4): ")
    if question4 == "3":
        print("Next question!")
        print(" ")
        test += 1
    else:
        print("Next question!")
        print(" ")


    print("Question 5")
    print(" ")
    print("He drives quite____, but his brother drives really____.")
    print(" ")
    print("1 - slowly ... fastly")
    print("2 - slow ... fastly")
    print("3 - slow ... fast")
    print("4 - slowly ... fast")
    print(" ")

    question5 = input("Your answer. (1/2/3/4): ")
    if question5 == "4":
        print("Next question!")
        print(" ")
        test += 1
    else:
        print("Next question!")
        print(" ")


    print("Question 6")
    print(" ")
    print("Put___bag on____table, then give me____apple and____bar of chocolate.")
    print(" ")
    print("1 - the ... the ... a ... a")
    print("2 - a ... the ... an ... the")
    print("3 - a ... a ... the ... the")
    print("4 - the ... the ... an ... a")
    print(" ")

    question6 = input("Your answer. (1/2/3/4): ")
    if question6 == "4":
        print("Next question!")
        print(" ")
        test += 1
    else:
        print("Next question!")
        print(" ")


    print("Question 7")
    print(" ")
    print("How long have they____there?")
    print(" ")
    print("1 - been waiting")
    print("2 - been waited")
    print("3 - waited")
    print("4 - waiting")
    print(" ")

    question7 = input("Your answer. (1/2/3/4): ")
    if question7 == "1":
        print("Next question!")
        print(" ")
        test += 1
    else:
        print("Next question!")
        print(" ")


    print("Question 8")
    print(" ")
    print("Do you think it's____rain tomorrow?")
    print(" ")
    print("1 - to")
    print("2 - will")
    print("3 - going to")
    print("4 - going")
    print(" ")

    question8 = input("Your answer. (1/2/3/4): ")
    if question8 == "3":
        print("Next question!")
        print(" ")
        test += 1
    else:
        print("Next question!")
        print(" ")


    print("Question 9")
    print(" ")
    print("I_____like getting up early.")
    print(" ")
    print("1 - not")
    print("2 - am not")
    print("3 - doesn't")
    print("4 - don't")
    print(" ")

    question9 = input("Your answer. (1/2/3/4): ")
    if question9 == "4":
        print("Next question!")
        print(" ")
        test += 1
    else:
        print("Next question!")
        print(" ")


    print("Question 10")
    print(" ")
    print("I____been hit by a car, but luckily I just managed to get out of the way.")
    print(" ")
    print("1 - must have")
    print("2 - could have")
    print("3 - should have")
    print("4 - can have")
    print(" ")

    question10 = input("Your answer. (1/2/3/4): ")
    if question10 == "2":
        print(" ")
        test += 1
    else:
        print(" ")

    total = (test/10) * 100

    print("Well done. You have finished this test.")
    print(" ")
    print("{} of 10 questions answered correctly. ({}%)".format(test, total))
    print(" ")

    if total == 100:
        print("Excellent! Your level is C2 (Proficient)")
    elif total >= 70 and total <= 99:
        print("Great! Your level is C1 (Advanced)!")
    elif total >= 30 and total <= 69:
        print("Ok! Your level is A2 (Intermediate)")
    else:
        print("Too bad! Your level is A1 (Elementary)")


#Call the game:
if __name__ == "__main__":
    main()

#Repeat the game
while True:
    print("__________________________________________")
    again = input("Do you wish to start the test again? (Y/N) ")
    again = again.lower()
    print(" ")
    if again == "y":
        print(" ")
        main()
    if again == "n":
        print(" ")
        print("Ok. Bye!")
        input(" ")
        quit()
    else:
        print(" ")
        print("You need to type 'Y' or 'N' to continue")
        print(" ")
        continue