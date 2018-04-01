# coding:utf-8
import ConfigParser
import os
import sys

cur_path=os.path.dirname(os.path.realpath("__file__"))
# cur_path=os.path.dirname(os.getcwd())
config_path=os.path.join(cur_path,"common\\config.ini")
print("配置文件路径:%s"%config_path)
conf=ConfigParser.ConfigParser()
conf.read(config_path)
server=conf.get("email","server")
port=conf.get("email","port")
sender=conf.get("email","sender")
psw=conf.get("email","psw")
receiver=conf.get("email","receiver")
