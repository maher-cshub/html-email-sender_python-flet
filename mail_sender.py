import smtplib,time
from secret_file import SENDER_NAME,SENDER_EMAIL,PASSWORD
import smtplib, ssl
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart # New line


##email body
html_file = "./index.html"


# Creating a SMTP session | use 587 with TLS, 465 SSL and 25
server = smtplib.SMTP('smtp.gmail.com', 587)
# Encrypts the email
context = ssl.create_default_context()
server.starttls(context=context)
# We log in into our Google account
server.login(SENDER_EMAIL, PASSWORD)

# Try to log in to server and send email

def SendEmail(sender_email,company_email,email_content):
    try:
        # Sending email from sender, to receiver with the email body
        server.sendmail(sender_email, company_email, email_content.as_string())
        print(f'Email sent! to {company_email}')
    except Exception as e:
        print(f'Oh no! Something bad happened!\n {e}')


def main(reciever_email,reciever_name,email_subject,file_path,):
    email_content = ""
    with open(file_path,mode="r",encoding="utf-8") as f:
        email_content = f.read()
        print(f"....Sending email to {reciever_email}")
        email = MIMEMultipart()
        email['To'] = formataddr((reciever_name, reciever_email))
        email['From'] = formataddr((SENDER_NAME, SENDER_EMAIL))
        email['Subject'] = email_subject
        email.attach(MIMEText(email_content, 'html'))
        SendEmail(SENDER_EMAIL,reciever_email,email)
    print("Closing Server")
    server.quit()



