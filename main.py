import smtplib
from email.message import EmailMessage

# Generate Gmail App Password and enter the email id and generated password below

# Steps to Generate Gmail App Password
#     Generate app password for Gmail inbox
#     Go to Google Account Security.
#     Click on "App passwords" under "Signing in to Google" section in the security page.
#     Select Mail app, select a device and click on "GENERATE". Use the generated password to configure IMAP/SMTP.

def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = "senderemail@gmail.com"
    msg['from'] = user
    password = ""

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)

    server.quit()

email_alert("Subject","Body", "receiveremail@gmail.com")