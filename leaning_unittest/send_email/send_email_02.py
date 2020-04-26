'''
报错
'''
# coding:utf-8
import smtplib
from email.mime.text import MIMEText


class SendEmail:

    global host
    global from_server
    global password
    host = "smtp.163.com"
    from_server = "hehuaimei123@163.com"
    password = "8uhb*UHB"

    def send_email(self, sub, to_list, content):
        msg = MIMEText(content, 'plain', 'utf-8')
        msg['Subject'] = sub
        msg['From'] = "username" + "<" + from_server + ">"
        msg['To'] = ";".join(to_list)

        smtp = smtplib.SMTP()
       # smtp.set_debuglevel(1)
        smtp.connect(host)
        smtp.login(from_server, password)
        smtp.sendmail(from_server, to_list, msg.as_string())
        smtp.quit()
        smtp.close()

if __name__ == '__main__':

    sen = SendEmail()
    sub = "测试"
    to_list = ["hehuaimei123@163.com", "hehuaimei@dangdang.com"]
    content = "第一封邮件"
    sen.send_email(sub, to_list, content)
