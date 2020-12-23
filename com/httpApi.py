# -*- coding: utf-8 -*-

# *******************************************#
# project:HeyMylody
# fileName:httpApi
# author:Merlin
# dataTime:2020/12/12
# *******************************************#

import requests
import json

import configparser
config = configparser.ConfigParser()
config.read('../config/config.ini', encoding='UTF-8')

from sign import getSign

class HttpError(Exception):
    def __init__(self):
        self.ErrorInfo = 'Error'
    def __str__(self):
        return self.ErrorInfo

class Http:
    def __init__(self):
        pass

    def get(self, url, data):
        resp = requests.request('GET', url=url, params=data)
        return resp

    def post(self, url, data, signKey=config.get('Country', 'Key')):
        data = json.dumps(data, separators=(',', ':'))
        sign = getSign(message=json.loads(data), key=signKey)
        headers = {
            'sign': sign,
            'Accept-Language': 'zh-CN',
            'Content-Type': 'application/json',
        }

        resp = requests.request('POST', url=url, data=data, headers=headers)
        return resp
