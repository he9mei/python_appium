import yagmail


# 连接邮箱服务器
yag=yagmail.SMTP(user="hehuaimei123@163.com",
                 password="8uhb*UHB",
                 host="smtp.163.com")

# 定义邮件主题和内容
subject="just a test,haha"
contents="this is contents!haha"

# 发送邮件
# yag.send(["hehuaimei@dangdang.com"],subject,contents)
'''
出现问题：smtplib.SMTPDataError
解决办法：把发件人地址也添加到收件人地址当中---如下，发送成功
'''
# 如果有多个收件人，可以用list
# yag.send(["hehuaimei123@163.com","hehuaimei@dangdang.com"],subject,contents)
# 如果有附件，直接添加到后面
# yag.send(["hehuaimei123@163.com","hehuaimei@dangdang.com"],subject,contents,"/Users/hehuaimei/Desktop/log.txt")
# 如果有多个附件,可以用list
yag.send(["hehuaimei123@163.com","hehuaimei@dangdang.com"],
         subject,
         contents,
         ["/Users/hehuaimei/Desktop/log.txt","/Users/hehuaimei/Desktop/悬浮球.png"])