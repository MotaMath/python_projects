import smtplib
import yfinance as yf
from email.message import EmailMessage

print("Starting")

# #to get current price
# aapl = yf.Ticker("AAPL")
# aapl_current = aapl.info["currentPrice"]
# print(aapl.info["currentPrice"])
# print(aapl)

# msft = yf.Ticker("MSFT")
# msft1 = print(msft.analyst_price_targets)

# #to get day high and day low
# btc = yf.Ticker("BTC-USD")
# btc1 = btc.info["description"]
# btc2 = btc.info["circulatingSupply"]
# print(btc1)
# print(btc2)

spy = yf.Ticker("^GSPC")
spy1 = spy.info["previousClose"]
print(spy1)

# print(btc.info["dayLow"])
# print(btc.info["dayHigh"])
# print(btc)

#To send email

# def send_email(subject, text):
#     try:
#         #Sender, receiver information
#         sender_email = "mathmota.sender@gmail.com"
#         receiver_email = "matheusmota450@hotmail.com"
#         password = "szhovdixyrnvngit"
        
#         #E-mail text
#         msg = EmailMessage()
#         msg["Subject"] = subject
#         msg["From"] = "mathmota.sender@gmail.com"
#         msg["To"] = "matheusmota450@hotmail.com"
#         msg.set_content(text)
        
#         #Connect with server
#         with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
#             server.login(sender_email, password)
#             server.send_message(msg)
#     except Exception as e:
#         print(f"Error: {e}")

# #Main function, need to use task manager
# def main():
#     subject = "Apple Inc."
#     text = f"Current Apple Stock Price Today: {aapl_current}" 
#     send_email(subject, text)
    
# if __name__ == "__main__":
#     main()