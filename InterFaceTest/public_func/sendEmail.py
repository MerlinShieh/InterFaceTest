# -*- coding: utf-8 -*-
# *******************************************#
# project:InterFaceTestdemo
# fileName:sendEmail
# author:Merlin
# dataTime:2020/6/28-22:28
# *******************************************#
# coding: utf-8
import sys
import os
BASE_DIR =os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #当前程序上上一级目录，这里为InterFaceTest
sys.path.append(BASE_DIR)
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
from email.mime.text import MIMEText
import pathlib
from config import cfg
def send_mail(username=cfg.email['username'], passwd=cfg.email['passwd'], recv=cfg.email['recv'], title=cfg.email['title'], content=cfg.email['content'], mail_host=cfg.email['mail_host'], port=cfg.email['port'], file=cfg.email['file']):
    '''
    发送邮件函数，默认使用163smtp
    :param username: 邮箱账号 xx@163.com
    :param passwd: 邮箱密码
    :param recv: 邮箱接收人地址，多个账号以逗号隔开
    :param title: 邮件标题
    :param content: 邮件内容
    :param mail_host: 邮箱服务器
    :param port: 端口号
    :return:
    '''
    if file:
        msg = MIMEMultipart()
        # 构建正文
        part_text = MIMEText(content)
        msg.attach(part_text)  # 把正文加到邮件体里面去

        # 构建邮件附件
        part_attach1 = MIMEApplication(open(file, 'rb').read())  # 打开附件
        part_attach1.add_header('Content-Disposition', 'attachment', filename=pathlib.Path(file).name)  # 为附件命名
        msg.attach(part_attach1)  # 添加附件
    else:
        msg = MIMEText(content)  # 邮件内容
    msg['Subject'] = title  # 邮件主题
    msg['From'] = username  # 发送者账号
    msg['To'] = recv  # 接收者账号列表
    smtp = smtplib.SMTP(mail_host, port=port)
    smtp.login(username, passwd)  # 登录
    smtp.sendmail(username, recv, msg.as_string())
    smtp.quit()



if __name__ == "__main__":
    send_mail(username='xxxxxx@163.com', passwd='xxxxxx', recv='xxxxxxx@163.com',
              title='测试邮件标题', content='测试邮件正文')
    print('send mail success!')