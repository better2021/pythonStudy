
import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'from@runoob.com'
receiver = ['709463253@qq.com'] # 接受邮件的邮箱
#三个参数：第一个为文本内容，第二个plain设置文本格式，第三个utf-8设置编码
message = MIMEText('Python 邮件发发送测试','plain','utf-8')
message['From'] = Header('菜鸟教程','utf-8') # 发送者
message['To'] = Header('测试','utf-8') # 接受者

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject,'utf-8')

try:
  smtpObj =smtplib.SMTP('192.168.51.79')
  smtpObj.sendmail(sender,receiver,message.as_string())
  print('邮件发送成功')
except smtplib.SMTPException:
  print('Error:无法发送邮件')  