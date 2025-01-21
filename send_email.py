import smtplib,ssl
import os
host="smtp.gmail.com"
port=465
username="subbu.venkat86@gmail.com"
paswword="eoux uydp pwzb pmhp"

receiver_email="subbu.venkat86@gmail.com"
context = ssl.create_default_context()


def send_email(Message):
    

    with smtplib.SMTP_SSL(host,port,context=context) as server:
        server.login(username,paswword)
        server.sendmail(username,receiver_email,Message)
