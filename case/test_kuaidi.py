# coding:utf-8
import unittest
from interface_frame.common.send_request import SendRequest
from interface_frame.common.read_excel import ExcelUtil
from interface_frame.common.write_excel import copy_excel,UpdataData
import requests
import os
import ddt
from interface_frame.common.log import Log
import time

# data_path:原数据    test_data_path:测试数据
# data_path=os.path.join(os.path.dirname(os.path.dirname(os.path.realpath("__file__"))),"data\\kuaidi.xlsx")
# test_data = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath("__file__"))), "result\\%s"%time.strftime("%Y%m"))
data_path="e:\\python work\\interface_frame\\data\\kuaidi.xlsx"
test_data="e:\\python work\\interface_frame\\result"
if not os.path.exists(test_data):
    os.mkdir(test_data)
test_data_path=os.path.join(test_data,"result.xlsx")
print("测试数据源地址:"+data_path)
print("测试结果地址:"+test_data_path)
print test_data_path

# 将一个月的数据放在一个文件夹下面
# if not os.path.exists(test_data):
#     os.mkdir(test_data)
# test_data_path=os.path.join(test_data,"%s"%time.strftime("%Y_%m_%d.xlsx"))

#复制表
copy_excel=copy_excel(data_path,test_data_path)
#读取数据
test=ExcelUtil()
test_data=test.read_excel(test_data_path,0)

@ddt.ddt
class SelectKuaiDi(unittest.TestCase):
    def setUp(self):
        self.send=SendRequest()
        self.s=requests.session()
        self.updata=UpdataData(test_data_path)

    @ddt.data(*test_data)
    def test_select_kuaidi(self,data):
        print("当前测试数据%s"%data)
        res=self.send.send_request(self.s,data)
        id=data["id"]
        id=int(id)
        print res
        try:
            self.updata.updata_value(id+1,9,res["result_code"])
            self.updata.updata_value(id+1,10,res["result"])
            if res.has_key("msg"):
                self.updata.updata_value(id+1,11,res["msg"])
        except Exception as msg:
            log=Log()
            log.error(msg)

        self.assertEqual(data["check"],res["companytype"])

if __name__=="__main__":
    unittest.main()



