import smtplib
import requests
import random
import yfinance as yf
from email.message import EmailMessage 
from bs4 import BeautifulSoup
from datetime import date

# Define the today's date
today_date = date.today()

# Define an end date
target_date = date(2024, 11, 20)

# Calculate the difference between the end date and start date
delta = target_date - today_date

delta.days

print(f"Time left until {target_date}: {delta.days} days.")

print(delta.days)

def get_btc_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    return data['bitcoin']['usd']


#Send daily E-mail 

# #Use yfinance to get BTC info
# btc = yf.Ticker("BTC-USD")
# btc1 = btc.info["description"]
# btc2 = btc.info["circulatingSupply"]

# #Get Weather information - requests and BeautifulSoup
# url = "https://forecast.weather.gov/MapClick.php?lat=35.2237867&lon=-80.8411413"
# page = requests.get(url)
# soup = BeautifulSoup(page.content, "html.parser")
# mostly1 = soup.find(class_="myforecast-current")
# temperature1 = soup.find(class_="myforecast-current-lrg")
# mostly = mostly1.text.strip()
# temperature = temperature1.text.strip()

#Lottery Simulator

# match2 = 0
# match3 = 0
# match4 = 0

# def lotto(lotto_list):
#     count = 0
#     x = random.randint(1, 43)
#     while count <= 4:
#         lotto_list.insert(count, x)
#         x = random.randint(1, 43)
#         for i in lotto_list:
#             if x == i:
#                 lotto_list.remove(i)
#                 count -= 1
#                 break
#         count += 1
#     return lotto_list.sort()

# winning_list = []
# lotto_numbers = []
# match_list = []

# lotto(winning_list)
# lotto(lotto_numbers)
# print("The daily winning numbers are: ", winning_list)
# print("Your lottery numbers are: ", lotto_numbers)

# if winning_list == lotto_numbers:
#     print("$$$$$$$$$$ JACKPOT $$$$$$$$$$")
#     print("Odds 1 in 962,598.0")
#     print("You won ---")
#     print(f"Match 2: {match2:,} times.")
#     print(f"Match 3: {match3:,} times.")
#     print(f"Match 4: {match4:,} times.")
# else:         
#     for i in winning_list:
#         if i in lotto_numbers:
#             match_list.append(i)
#     if len(match_list) == 1:
#         print("You've matched 1 number! Good luck next time.")
#         winning_list = winning_list.clear()
#         lotto_numbers = lotto_numbers.clear()
#     if len(match_list) == 2:
#         print("You've matched 2 numbers!")
#         print("Odds 1 in 11.4")
#         print("YOU WON $1.")
#         match2 += 1
#         winning_list = winning_list.clear()
#         lotto_numbers = lotto_numbers.clear()
#     if len(match_list) == 3:
#         print("You've matched 3 numbers!")
#         print("Odds 1 in 136.9")
#         print("YOU WON $5.")
#         match3 += 1
#         winning_list = winning_list.clear()
#         lotto_numbers = lotto_numbers.clear()
#     if len(match_list) == 4:
#         print("You've matched 4 numbers!")
#         print("Odds 1 in 5,066.0")
#         print("YOU WON $250.")
#         match4 += 1
#         winning_list = winning_list.clear()
#         lotto_numbers = lotto_numbers.clear()
            

# #Load data from .txt file
# def load():
#         with open("daily.txt", "r") as file:
#             data = file.read()
#         return data
        
# #Save data to.txt file
# def save(data):
#     try:
#         data = int(data)
#         data_save = data - 1
#         data_save = str(data_save)
#         with open("daily.txt", "w") as file:
#             file.write(data_save)
            
#     except Exception as e:
#         print(f"Error: {e}")

# def send_email(receiver, subject, text):
#     try:
#         #Sender, receiver information
#         sender_email = "mathmota.sender@gmail.com"
#         password = "szhovdixyrnvngit"
        
#         #E-mail text
#         msg = EmailMessage()
#         msg["Subject"] = subject
#         msg["From"] = "mathmota.sender@gmail.com"
#         msg["To"] = receiver
#         msg.set_content(text)
        
#         #Connect with server
#         with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
#             server.login(sender_email, password)
#             server.send_message(msg)
#     except Exception as e:
#         print(f"Error: {e}")

# #Main function
# def main():
#     try:
#         print("Start time.")
#         data = load()
#         print("Data loaded.")
#         receiver = "matheusmota450@hotmail.com"
#         receiver2 = "uinny10@hotmail.com"
#         subject = "Daily"
#         text = f"""
#         Ashley arrives in {data} days!
            
#         ###############################
            
#         Current Weather
#         Charlotte - NC
#         {temperature}
#         {mostly}
            
#         ###############################
            
#         {btc1}
            
#         Bitcoin Circulating supply: {btc2:,} BTC
            
#         ###############################
            
#         @motamath
#         {date_time} UTC TimeZone
#         """ 
#         send_email(receiver, subject, text)
#         send_email(receiver2, subject, text)
#         print("E-mail sent.")
#         save(data)
#         print("Data saved.")
#         print(" ") 
#     except Exception as e:
#         print(f"Error: {e}")
    
# if __name__ == "__main__":
#     main()
    
#Implement:
# from datetime import datetime

# # Step 1: Get the current date
# current_date = datetime.now()

# # Step 2: Define November 30 of the current year
# november_30 = datetime(current_date.year, 11, 30)

# # Step 3: Calculate the difference
# days_left = (november_30 - current_date).days

# # Step 4: Print the result
# print(f"Days left until November 30: {days_left}")

# ----
#
# HTML stile e-mail