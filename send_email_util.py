import smtplib
from email.mime.text import MIMEText
from email.header import Header



class Sender():
        
    def __init__(self,mail_host,mail_pass,sender):
        self.mail_host=mail_host   #smtp host
        self.mail_pass=mail_pass   #password to SMTP service (may be different from login password, check with your email provider)
        self.sender=sender       #sender email
        
    
    
    def send(self,receivers,content='code finished',subject='code finished',FROM='sender',TO='receiver'):
        message=MIMEText(content,'plain','utf-8')
        message['From']=Header(FROM,'utf-8')
        message['To']=Header(TO,'utf-8')
        message['Subject']=Header(subject,'utf-8')
        smtpObj=smtplib.SMTP_SSL(self.mail_host, 465) 
        smtpObj.login(self.sender,self.mail_pass)  
        smtpObj.sendmail(self.sender,receivers,message.as_string())
        smtpObj.quit()