# -*- coding: utf-8 -*-

# *******************************************#
# project:InterFaceTestdemo
# fileName:useApi
# author:Merlin
# dataTime:2020/6/26-22:21
# *******************************************#
import requests
import json
from pprint import pprint
import sys
import os
BASE_DIR =os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #当前程序上上一级目录，这里为InterFaceTest
sys.path.append(BASE_DIR)
import config.cfg

class SendHttp:
    def getHttp(self, url, params):
        res = requests.request("GET", url=url, params=params)
        return res
    def postHttp(self, url, data):
        funcName = sys._getframe().f_code.co_name
        res = requests.request("POST", url=url, data=data)
        return res
if __name__=="__main__":
    data = {"s": "App.Scws.GetWords", "app_key": "B2F70096FD3977B3F183DFD952F4446B", "text": '可以免费使用'}
    print(type(data))
    try:
        res = SendHttp().getHttp(url='hn216.api.yesapi.cn', params=data)
        print(res.text)
    except MissingSchema as e:
        print('error')
        print(e)
