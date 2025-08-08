import time
import pandas as pd
import datetime
from email.message import EmailMessage
import ssl as obj_ssl
import smtplib

df = pd.read_excel("Data.xlsx")
today = datetime.datetime.now().strftime("%m-%d")
str_sender = 'mmariajessica@gmail.com'
str_password =  'aqbr gutj itvk morc'
str_subject = 'Happy Birthday!'
str_body = "Wish you a very happy birthday"
str_receiver = 'mmariajessica@gmail.com'

# Looping through every row of the table
i = 0
for row in df['Birthday']:
    birthday = row.strftime("%m-%d")
    # checking
    if birthday == today:
       obj_email = EmailMessage()
       obj_email['From'] = str_sender
       obj_email['To'] = str_receiver
       obj_email['Subject'] = str_subject
       obj_email.set_content(str_body)
       obj_context = obj_ssl.create_default_context()
       obj_smtp = smtplib.SMTP_SSL('smtp.gmail.com',465, context=obj_context)
       obj_smtp.login(str_sender, str_password)
       obj_smtp.sendmail(str_sender, str_receiver, obj_email.as_string())
    i+=1
                      
             
        

                                         
