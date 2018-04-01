# coding:utf-8
from common import HTMLTestRunner
import unittest
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from interface_frame.common import readConfig
import time
import os

class RunCase():
    def run_case(self,case_path,report_path):
        # 执行测试用例,并将测试结果放在report_path中
        discover=unittest.defaultTestLoader.discover(case_path,"test*.py",top_level_dir=None)
        # run=unittest.TextTestRunner()
        # run.run(discover)
        fp=open(report_path,"wb")
        run=HTMLTestRunner.HTMLTestRunner(fp,title=u"测试结果",description=u"读取excel数据进行测试的结果")
        run.run(discover)
        fp.close()
#
    def send_email(self,server, port, sender, pws,receiver,report_path):

        print("start send email！！！")
        #读取文件内容
        body=MIMEMultipart()
        #文本内容
        dd="<p>您有新的测试报告啦</p>"
        text=MIMEText(dd,"html","utf-8")
        body.attach(text)

        #附件内容

        att=MIMEText(open(report_path,"rb").read(),"base64","utf-8")
        att["content-type"]="application/octet-stream"
        att["content-disposition"]="attachment;filename='report.html'"
        body.attach(att)


        body["subject"]="%s测试邮件"%(time.strftime("%Y_%m_%d"))
        body["from"]=sender
        body["to"]=receiver


        #发送邮件
        try:
            #163邮箱
            smtp=smtplib.SMTP_SSL(server,port)
            smtp.login(sender,pws)
        except:
            #QQ邮箱
            smtp=smtplib.SMTP()
            smtp.connect(server)
            smtp.login(sender,pws)

        smtp.sendmail(sender, receiver, body.as_string())
        print("send email success!")

if __name__=="__main__":
    case_path=os.path.join(os.path.dirname(os.path.realpath("__file__")),"case")
    report_path=os.path.join(os.path.dirname(os.path.realpath("__file__")),"result\\report.html")
    run=RunCase()
    run.run_case(case_path,report_path)
    server=readConfig.server
    port=readConfig.port
    sender=readConfig.sender
    pws=readConfig.psw
    receiver=readConfig.receiver
    run.send_email(server,port,sender,pws,receiver,report_path)



