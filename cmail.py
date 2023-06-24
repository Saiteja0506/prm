import smtplib
from email.message import EmailMessage
#from smtplib import SMTP_SSL
def sendmail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('saitejabajinku@gmail.com','hmvznooggxyswtem')
    msg=EmailMessage()
    msg['From']='saitejabajinku@gmail.com'
    msg['Subject']=subject
    msg['To']=to
    msg.set_content(body)
    server.send_message(msg)
    server.quit()