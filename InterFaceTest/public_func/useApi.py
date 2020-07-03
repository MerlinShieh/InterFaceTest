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
import json
import xlrd

import public_func.setInfo

BASE_DIR =os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #当前程序上上一级目录，这里为InterFaceTest
sys.path.append(BASE_DIR)
import config.cfg

class SendHttp:
    def getHttp(self, url, params):
        '''
        发送get请求
        :param url:
        :param params:
        :return:
        '''
        funcName = sys._getframe().f_code.co_name
        res = requests.request("GET", url=url, params=params)
        return res
    def postHttp(self, url, data):
        res = requests.request("POST", url=url, data=data)
        return res
if __name__=="__main__":
    import requests
    import public_func.readExcel
    case = public_func.readExcel.getExeclTestCaseList()
    data = str(case[-1:][0]['data'])
    print(type(data))
    url = str(case[-1:][0]['host'])
    data = eval(data)
    print(type(data))
    resp = SendHttp().postHttp(url=url, data=data)
    print(resp.text)
    print(resp.status_code)
