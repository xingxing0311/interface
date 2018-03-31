# # coding:utf-8
# from common import HTMLTestRunner
# import unittest
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# import time
# import os
#
# class RunCase():
#     def run_case(self,case_path,report_path):
#         # 执行测试用例,并将测试结果放在report_path中
#         discover=unittest.defaultTestLoader.discover(case_path,"test*.py",top_level_dir=None)
#         run=unittest.TextTestRunner()
#         run.run(discover)
#         # fp=open(report_path,"wb")
#         # run=HTMLTestRunner.HTMLTestRunner(fp,title=u"测试结果",description=u"读取excel数据进行测试的结果")
#         # run.run(discover)
#         # fp.close()
#
#     def send_email(self,server,port,sender,pws,receiver,report):
#         #读取文件内容
#         body=MIMEMultipart()
#         #文本内容
#         dd="<p>您有新的测试报告啦</p>"
#         data=MIMEText(dd,"html","utf-8")
#         body.attach(data)
#         #附件内容
#         fp=open(report_path,"rb")
#         att=MIMEMultipart(fp,"base64","utf-8")
#         att["content-type"]="application/octet-stream"
#         att["content-disposition"]="attachment;filename='report.html'"
#         body.attach(att)
#
#         body["subject"]="%s测试邮件"%(time.strftime("%Y_%m_%d"))
#         body["sender"]=sender
#         body["receiver"]=receiver
#
#         #发送邮件
#         try:
#             #163邮箱
#             smtp=smtplib.SMTP()
#             smtp.connect(server,port)
#             smtp.login(sender,pws)
#         except:
#             #QQ邮箱
#             smtp=smtplib.SMTP_SSL(server,port)
#             smtp.login(sender,pws)
#         finally:
#             smtp.sendmail(sender,pws,body.as_string())
#             print("send email success!")
#
# if __name__=="__main__":
#     case_path=os.path.join(os.path.dirname(os.path.realpath("__file__")),"case")
#     report_path=os.path.join(os.path.dirname(os.path.realpath("__file__")),"result\\report.html")
#     run=RunCase()
#     print case_path,report_path
#     run.run_case(case_path,report_path)
    # server="smtp.qq.com"
    # port=465
    # sender="1693753028@qq.com"
    # pws="omgelznghrasdgcg"
    # receiver="2075134579@qq.com"
    # run.send_email(server,port,sender,pws,receiver,report_path)

# coding=utf-8
import unittest
import time
from interface_frame.common import HTMLTestRunner
import os

curpath = os.path.dirname(os.path.realpath(__file__))
report_path = os.path.join(curpath, "result")
if not os.path.exists(report_path): os.mkdir(report_path)
case_path = os.path.join(curpath, "case")

def add_case(casepath=case_path, rule="test*.py"):
    '''加载所有的测试用例'''
    # 定义discover方法的参数
    discover = unittest.defaultTestLoader.discover(casepath,
                                                  pattern=rule,)

    return discover

def run_case(all_case, reportpath=report_path):
    '''执行所有的用例, 并把结果写入测试报告'''
    htmlreport = reportpath+r"\result.html"
    print("测试报告生成地址：%s"% htmlreport)
    fp = open(htmlreport, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                               verbosity=2,
                                               title="测试报告",
                                               description="用例执行情况")

    # 调用add_case函数返回值
    runner.run(all_case)
    fp.close()

if __name__ == "__main__":
    cases = add_case()
    run_case(cases)


