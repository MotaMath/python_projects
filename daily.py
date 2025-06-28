import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import date


    # Define the today's date
today_date = date.today()

# Define an end date
target_date = date(2024, 11, 27)

# Calculate the difference between the end date and start date
delta = target_date - today_date


def send_email(receiver_email, html):
    sender_email = "mathmota.sender@gmail.com"
    password = "szhovdixyrnvngit"

    message = MIMEMultipart("alternative")
    message["Subject"] = "Daily"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = """\
    Hi,
    
    Reply to this email if you have problems with the content of this email.
    
    Best,
    
    @ Mota
    
    """

    # Turn these into plain/html MIMEText objects
    email_plain = MIMEText(text, "plain")
    email_html = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(email_plain)
    message.attach(email_html)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )


# Email content        
html = """
<html>
<style>
    body {
        font-family: Arial, sans-serif;
    }
    
    .p1 {
    	text-align: center;
        border: 2px solid DodgerBlue;   
        border-radius: 12px;
  		padding: 5px;
    }
</style>
<body>
    <p class="p1">
        <b>Plane arrives in """ + str(delta.days) + """ days!</b>
    </p>
    <br>
    <p><b>Confirmation Code: ZP4Y2K</b></p>
	<br>
    <p>Date: November 27, 2024</p>
    <p>Charlotte - NC</p>
    <p>5:51 PM</p>

</body>
</html>
"""

# Main

try:
    send_email("random@hotmail.com", html)
    print("E-mail sent.")
except Exception as e:
    print(f"Error: {e}")