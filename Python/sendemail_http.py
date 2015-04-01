#!/usr/bin/env python3  
#coding: utf-8  
import smtplib  
from email.mime.text import MIMEText  
  
sender = 'ychenid@126.com'  
receiver = 'chenyingzju@126.com'  
subject = 'python email test'  
smtpserver = 'smtp.126.com'  
username = 'ychenid@126.com'  
password = '******'  
 
msg = MIMEText('<html><h1>你好,我是陈英。</h1></html>','html','utf-8')  
 
msg['Subject'] = subject  
 
smtp = smtplib.SMTP()  
smtp.connect('smtp.126.com')  
smtp.login(username, password)  
smtp.sendmail(sender, receiver, msg.as_string())  
smtp.quit() 
