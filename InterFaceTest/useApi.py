#-*- coding: utf-8 -*-
import requests,json
from pprint import pprint

class SendHttp:
    def getHttp(self, url, params):
        res = requests.request("GET", url=url, params=params)
        return res
    def postHttp(self, url, data):
        res = requests.request("POST", url=url, data=data)
        return res
if __name__=="__main__":
    data = {"s": "App.Scws.GetWords", "app_key": "B2F70096FD3977B3F183DFD952F4446B", "text": '可以免费使用'}
    print(type(data))
    res = SendHttp().getHttp(url='http://hn216.api.yesapi.cn', params=data)
    print(res.status_code)
    print(res.text)