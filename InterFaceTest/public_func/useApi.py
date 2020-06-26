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
import config.cfg
import public_func.log
from public_func.log import setLog
class SendHttp:
    def getHttp(self, url, params):
        res = requests.request("GET", url=url, params=params)
        public_func.log.setLog(leavel='debug', message=res.text)
        return res
    def postHttp(self, url, data):
        res = requests.request("POST", url=url, data=data)
        public_func.log.setLog(leavel='debug', message=res.text)
        return res
if __name__=="__main__":
    data = {"s": "App.Scws.GetWords", "app_key": "B2F70096FD3977B3F183DFD952F4446B", "text": '可以免费使用'}
    print(type(data))
    res = SendHttp().getHttp(url='http://hn216.api.yesapi.cn', params=data)
    setLog(message=data, leavel='info')
    setLog(message=res, leavel="info")
    print(res.status_code)
    print(res.text)