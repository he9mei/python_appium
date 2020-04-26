import yagmail
#需要先安装yagmail插件

yag=yagmail.SMTP(user="hehuaimei123@163.com",
                 password="8uhb*UHB",
                 host="smtp.163.com")
subject="测试主题"
contents="测试内容"
yag.send(["hehuaimei123@163.com","hehuaimei@dangdang.com"],
         subject,
         contents,
         "/Users/hehuaimei/Desktop/log/log.txt")