import requests
import smtplib
from bs4 import BeautifulSoup
from email.message import EmailMessage

#Create a automation that scrap NC lottery Website and get the Jackpot daily
#and send an e-mail when Jackpot is over 300.000

def get_price():
    #To get information:
    url = "https://nclottery.com/cash5"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    #Use soup.find to get the element
    element = soup.find(id="ctl00_MainContent_HeaderCash5_JackpotCash5_lblC5Prize")
    data_text = element.text.strip() # type: ignore
    
    #Check if the value is over 300
    jackpot = int(data_text[1:4])
    return jackpot

#send e-mail
def send_email():
    try:
        #Sender, receiver information
        sender_email = "mathmota.sender@gmail.com"
        password = "szhovdixyrnvngit"
        
        #E-mail text
        msg = EmailMessage()
        msg["Subject"] = "Cash5 - PLAY TODAY"
        msg["From"] = "mathmota.sender@gmail.com"
        msg["To"] = "matheusmota450@hotmail.com"
        msg.set_content("Cash5 NC Lottery gets over $300.000, time to play!")
        
        #Connect with server
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, password)
            server.send_message(msg)
    except Exception as e:
        print(f"Error: {e}")

#Main function, need to use task manager
def main():
    result = get_price()
    #Check if the value is over 300:
    if result >= 300:
        send_email()
    else:
        print(result)
    
if __name__ == "__main__":
    main()