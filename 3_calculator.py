#A simple calculator in Python CMD

# Math functions

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

print("__________CALCULATOR__________")
print("")
def main():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        # Take input from the user
        choice = input("Enter choice (1/2/3/4): ")

        # Check if choice is one of the four options
        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print("Result:", add(num1, num2))

            elif choice == '2':
                print("Result:", subtract(num1, num2))

            elif choice == '3':
                print("Result:", multiply(num1, num2))

            elif choice == '4':
                print("Result:", divide(num1, num2))

            # Check if user wants another calculation
            while True:
                next_calculation = input("Do you want to do another calculation? (Y/N): ").upper()
                if next_calculation in ("Y", "N"):
                    if next_calculation == "Y":
                        main()
                    if next_calculation == "N":
                        input("Thank you! Press ENTER to exit.")
                        quit()
                else:
                    print("Invalid Input")
                    continue
        else:
            print("Invalid Input")

if __name__ == "__main__":
    main()