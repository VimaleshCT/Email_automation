import smtplib
from datetime import datetime

# Email configuration
Sender = 'sender@gmail.com'
Password = 'password'  # Replace with your Gmail password or App Password

# List of names and emails
names = ['Name1', 'Name2']
emails = ['name1@gmail.com', 'nam2@gmail.com']

# Get the current date
now = datetime.now()
current_date = (now.day, now.month)

# SMTP server configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 587

# Iterate through the list of emails and send messages
with smtplib.SMTP(smtp_server, smtp_port) as connect_server:
    connect_server.starttls()
    connect_server.login(Sender, Password)

    for item in range(len(emails)):
        name = names[item]
        email = emails[item]
        
        # Create the email message
        message = f"Subject: White Friday Discount Offer\n\nHi {name},\n\nDon't wait and buy now."
        
        if current_date == (2, 11):  # November 2nd
            message = f"Subject: White Friday Discount Offer\n\nHi {name},\n\nDon't wait and buy now."
        
        connect_server.sendmail(Sender, [email], message)

print('Emails sent successfully!')
