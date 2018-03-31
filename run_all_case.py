# coding:utf-8
from common import HTMLTestRunner
import unittest
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class RunCase():
    def __init__(self,report_path):
        self.report_path=report_path

    def run_case(self,case_path):
        # 执行测试用例,并将测试结果放在report_path中
        discover=unittest.defaultTestLoader.discover(case_path,"test.py")
        fp=open(self.report_path)
        run=HTMLTestRunner.HTMLTestRunner(fp,title=u"测试结果",description=u"读取excel数据进行测试的结果")
        run.run(discover)
        fp.close()

    def send_email(self,server,port,sender,pws,receiver):
        #读取文件内容
        body=MIMEMultipart()
        #文本内容
        dd="<p>您有新的测试报告啦</p>"
        data=MIMEText(dd,"html","utf-8")
        body.attach(data)
        #附件内容
        fp=open(self.report_path,"rb")
        att=MIMEMultipart(fp,"base64","utf-8")
        att["content-type"]="application/octet-stream"
        att["content-disposition"]="attachment;filename='report.html'"
        body.attach(att)

        #发送邮件
        smtp=smtplib.SMTP()
        try:
            smtp.connect()

