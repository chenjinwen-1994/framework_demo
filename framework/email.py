import smtplib,os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

class Email(object):
    def __init__(self,email):
        self.email = email
    # 取最新测试报告
    def new_file(self,test_dir):
        #列举所有文件
        lists = os.listdir(test_dir)
        #getmtime输出最近修改时间getctime输出创建时间
        # key=lambda fn: os.path.getmtime(test_dir + '\\' + fn)相当于
        # def key(fn):
        #     return os.path.getmtime(test_dir + '\\' + fn)
        lists.sort(key=lambda fn: os.path.getmtime(test_dir + '\\' + fn))
        # 获取最新文件的绝对路径
        file_path = os.path.join(test_dir, lists[-1])
        return file_path
    #发送邮件
    def send_email(self,newfile):
        #读取文件内容
        f = open(newfile,'rb')
        filebody = f.read()
        f.close()
        #发送邮件服务器
        smtpserver = 'smtp.163.com'
        #用户名密码
        user = '18251896464@163.com'
        password = 'chen12345'
        sender = '18251896464@163.com'
        #发送邮箱
        receiver =['1130787276@qq.com']
        #邮件主题
        subject = '自动化测试报告'

        msg = MIMEMultipart('mixed')
        #正文
        f ='本轮自动化测试报告，请大家将附件下载后用Firefox或Chrome查看，谢谢！'
        msg.attach(MIMEText(f,'plain','utf-8'))

        # msg_html1 = MIMEText(filebody, 'html', 'utf-8')
        # msg.attach(msg_html1)

        #附件
        msg_html = MIMEText(filebody, 'html', 'utf-8')
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        msg_html["Content-Disposition"] = 'attachment; filename="TestReport.html"'
        msg.attach(msg_html)

        msg['From'] = '18251896464@163.com'
        msg['To'] = ";".join(receiver)
        msg['Subject'] = Header(subject, 'utf-8')

        # 连接发送邮件
        smtp = smtplib.SMTP()
        #默认端口25
        smtp.connect(smtpserver, 25)
        smtp.login(user, password)
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()



