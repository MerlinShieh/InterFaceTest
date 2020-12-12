# -*- coding: utf-8 -*-

# *******************************************#
# project:HeyMylody
# fileName:httpApi
# author:Merlin
# dataTime:2020/12/12
# *******************************************#

import requests
import json
from sign import getSign

class HttpError(Exception):
    def __init__(self, ErrorInfo):
        self.ErrorInfo = ErrorInfo
    def __str__(self):
        return self.ErrorInfo

class Http:
    def __init__(self):
        pass

    def get(self, url, data):
        resp = requests.request('GET', url=url, params=data)
        return resp

    def post(self, url, data, signKey):
        data = json.dumps(data)
        sign = getSign(message=data, key=signKey)
        headsers = {
            'sign': sign,
            'Accept-Language': 'zh-CN',
            'Content-Type': 'application/json',
        }

        resp = requests.request('POST', url=url, data=data, headsers=headsers)
        return resp
