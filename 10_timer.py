import time
import datetime

# Timer

date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

bar_total = 0
def start_timer(seconds):
    """Countdown timer that starts from a given number of seconds."""
    while seconds:
        mins, secs = divmod(seconds, 60)
        time_format = '{:02d}:{:02d}'.format(mins, secs)
        print(time_format, end='\r') # Print the countdown in the same line
        time.sleep(1)
        seconds -= 1
    bar(10)
    print("Time's up!")
    

def bar(bar_total):  # Total number of characters in the progress bar (10% per character)
    for x in range(1, bar_total + 1):  # From 1 to 10, representing 10% to 100%
        bar = '##' * x + '  ' * (bar_total - x)  # Create the progress bar string
        print(f"[{bar}]", end='\r')  # Display the progress bar in the same line
        time.sleep(0.2)  # Wait for 5 seconds

    print("\nProgress completed.")  # Move to the next line when done

        
def main():
    try:
        user_input = input("Enter time in seconds or 'MM:SS' format: ")
        
        if ':' in user_input:
            # If the user provides time in MM:SS format
            mins, secs = map(int, user_input.split(':'))
            total_seconds = mins * 60 + secs
        else:
            # If the user provides time in seconds
            total_seconds = int(user_input)
        
        print("Timer started!")
        start_timer(total_seconds)
    
    except ValueError:
        print("Invalid input. Please enter time in the correct format.")


if __name__ == "__main__":
    main()