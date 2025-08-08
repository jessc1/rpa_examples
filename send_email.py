from email.message import EmailMessage
import ssl as obj_ssl
import smtplib
str_sender =  'mmariajessica@gmail.com'
str_receiver = 'mmariajessica@gmail.com'
str_password = 'aqbr gutj itvk morc'

str_subject = 'To Watch Chinese Movie List'
str_body = '1 - Better Days 2020'
obj_email = EmailMessage()
obj_email['From'] = str_sender
obj_email['To'] = str_receiver
obj_email['Subject'] = str_subject
obj_email.set_content(str_body)

obj_context = obj_ssl.create_default_context()
obj_smtp = smtplib.SMTP_SSL('smtp.gmail.com',465,context=obj_context)
obj_smtp.login(str_sender, str_password)
obj_smtp.sendmail(str_sender, str_receiver, obj_email.as_string())
