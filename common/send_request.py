# coding:utf-8
from interface_frame.common.read_excel import ExcelUtil
import json
import requests



class SendRequest():
    def send_request(self,s,data):
        #data为字典
        # print(data)
        #头部
        try:
            header=eval(data["header"])
        except:
            header=None

        try:
            method=data["method"]
            # print(method)
        except:
            method=None

        try:
            url=data["url"]
            # print(url)
        except:
            url=None
        # method=data["method"]
        # url=data["url"]

        #请求的body值
        try:
            body=eval(data["data"])
        except:
            body=None

        #post请求的URL参数
        try:
            params=eval(data["params"])
        except:
            params=None

        #json类型的数据格式传json格式
        # if data["way"]=="data":
        #     body=body
        # elif data["way"]=="json":
        #     body=json.dump(body)
        # else:
        #     body=body

        if data["way"] == "json":
            body = json.dump(body)
        else:
            body = body


        #接受返回信息
        res={}
        #SSL验证
        verify=False
        print("---接口测试正在进行---")
        # print "接口类型:%s"%(method)
        r=s.request(method=method,url=url,headers=header,params=params,data=body,verify=verify)
        res["result_code"]=r.status_code
        res["companytype"]=r.json()["companytype"]
        try:
            res["result"]=r.json()["success"]
        except Exception as msg:
            res["msg"]=msg
        return res

if __name__=="__main__":
    excel = ExcelUtil()
    file_path = "e:\\python work\\interface_frame\\data\\kuaidi.xlsx"
    data = excel.read_excel(file_path, index=0)
    data_dict=data[0]
    sr=SendRequest()
    s = requests.session()
    res=sr.send_request(s,data_dict)
    print(res)

