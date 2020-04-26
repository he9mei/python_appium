'''
报错
'''
import smtplib
from email.mime.text import MIMEText
from email.header import Header

#邮件主题
subject="pyhton email test"

#编写HTML类型的邮件正文
msg=MIMEText('<html><hl>你好啊</hl></html>','html','utf-8')
msg['Subject']=Header(subject,'utf-8')

#发送邮件
smtp=smtplib.SMTP()
smtp.connect("smtp.163.com")
smtp.login("hehuaimei123@163.com","8uhb*UHB")
smtp.sendmail("hehuaimei123@163.com","hehuaimei@dangdang.com",msg.as_string())
smtp.quit()