# -*- coding: utf-8 -*-
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from email.mime.image import MIMEImage

mailto_list = ['hzgnjupt@gmail.com']

# 创建邮件
msg = MIMEMultipart()
msg['Subject'] = 'Using Python to Send Mail'
msg['From'] = 'he.zhigang7@zte.com.cn'
msg['To'] = ';'.join(mailto_list)

# 添加纯文本
att1 = MIMEText(u'测试文本', _subtype='plain', _charset='utf-8')
msg.attach(att1)

# 添加html
att2 = MIMEText(u'<a href="http://www.baidu.com/">测试超链接</a><br/><img src="cid:testimage">', _subtype='html', _charset='utf-8')
msg.attach(att2)

# 添加图片
att3 = MIMEImage(open(u'G:\\下载\\测试图片.png', 'rb').read())
att3.add_header('Content-ID','<testimage>')
msg.attach(att3)

# 添加附件
att4 = MIMEText(open('sendmail.py', 'rb').read(), 'base64', 'utf-8')
att4['Content-Type'] = 'application/octet-stream'
att4['Content-Disposition'] = 'attachment; filename="sendmail.py"'
msg.attach(att4)

server = smtplib.SMTP()
server.connect('smtp.gmail.com')
server.docmd("EHLO server" )
server.starttls()
server.login('hzgnjupt@gmail.com', '?????????')
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()
