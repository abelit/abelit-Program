#!/usr/bin/env python3  
#coding: utf-8  
import smtplib
from email.mime.text import MIMEText  
from email.header import Header  
sender = 'ychenid@126.com'  
receiver = 'ychenid@hotmail.com'  
#subject = 'python email test'  
smtpserver = 'smtp.126.com'  
username = 'ychenid@126.com'  
password = '******'
def send_mail(towho,sub,content):
    msg = MIMEText('你好,hotmail','text','utf-8')#中文需参数‘utf-8’，单字节字符不需要  
    msg['Subject'] = Header(sub, 'utf-8')
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.login(username, password)
        smtp.sendmail(sender, towho, msg.as_string())
        smtp.quit()
        return True
    except Exception.e:
        print(str(e))
        return False
if __name__=='__main__':
    if send_mail(receiver,"Hello Chenying","This is the test mail for testing how to use python sending email."):
        print("发送成功")
    else:
        print("发送失败")
##        
###!/usr/bin/env python3
###coding: utf-8  
##import smtplib  
##from email.mime.text import MIMEText  
##from email.header import Header  
##sender = 'ychenid@126.com'  
##receiver = 'ychenid@hotmail.com'  
##subject = 'python email test'  
##smtpserver = 'smtp.126.com'  
##username = 'ychenid@126.com'  
##password = '******'  
##msg = MIMEText('你好,hotmail','text','utf-8')#中文需参数‘utf-8’，单字节字符不需要  
##msg['Subject'] = Header(subject, 'utf-8')   
##smtp = smtplib.SMTP()  
##smtp.connect('smtp.126.com')  
##smtp.login(username, password)  
##smtp.sendmail(sender, receiver, msg.as_string())  
##smtp.quit()  
##
##
##
### -*- coding: UTF-8 -*-
##'''
##发送txt文本邮件
##小五义：http://www.cnblogs.com/xiaowuyi
##'''
##import smtplib  
##from email.mime.text import MIMEText  
##mailto_list=[YYY@YYY.com] 
##mail_host="smtp.XXX.com"  #设置服务器
##mail_user="XXXX"    #用户名
##mail_pass="XXXXXX"   #口令 
##mail_postfix="XXX.com"  #发件箱的后缀
##  
##def send_mail(to_list,sub,content):  
##    me="hello"+"<"+mail_user+"@"+mail_postfix+">"  
##    msg = MIMEText(content,_subtype='plain',_charset='gb2312')  
##    msg['Subject'] = sub  
##    msg['From'] = me  
##    msg['To'] = ";".join(to_list)  
##    try:  
##        server = smtplib.SMTP()  
##        server.connect(mail_host)  
##        server.login(mail_user,mail_pass)  
##        server.sendmail(me, to_list, msg.as_string())  
##        server.close()  
##        return True  
##    except Exception, e:  
##        print str(e)  
##        return False  
##if __name__ == '__main__':  
##    if send_mail(mailto_list,"hello","hello world！"):  
##        print "发送成功"  
##    else:  
##        print "发送失败"
