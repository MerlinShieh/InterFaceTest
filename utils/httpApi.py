# -*- coding: utf-8 -*-

# *******************************************#
# project:HeyMylody
# fileName:httpApi
# author:Merlin
# dataTime:2020/12/12
# *******************************************#

import configparser
import http
import json
import requests

from utils import log, logger, BASE_DIR

config = configparser.ConfigParser()
config.read(f'{BASE_DIR}/config/config.ini', encoding='UTF-8')


class HttpError(Exception):
    def __init__(self):
        self.ErrorInfo = 'Error'

    def __str__(self):
        return self.ErrorInfo


class Http:
    def __init__(self):
        pass

    @staticmethod
    @logger(__name__)
    def get(url, data, headers=None):
        if not headers:
            headers = {
                'Accept': '<Accept>',
                'Accept-Language': '<Accept-Language>',
                'Connection': '<Connection>',
                'Host': '<Host>',
                'kbn-version': '<kbn-version>',
                'Origin': '<Origin>',
                'Referer': '<Referer>',
                'User-Agent': '<User-Agent>',
                'Cookie': '<Cookie>',
                'content-type': '<content-type>'
            }

        log.debug(f'GET+ {url}{data}')
        resp = requests.request('GET', url=url, params=data)
        return resp

    @staticmethod
    @logger(__name__)
    def post(url: str, data=None, json=None, headers=None, isForm=False):
        """
        不需要做加密的可以把这里重写
        :param json:
        :param isForm: 默认采用json提交 bool
        :param headers:
        :param url:
        :param data: dict格式
        :return:
        """

        if not headers:
            headers = {
                'Accept': '<Accept>',
                'Accept-Language': '<Accept-Language>',
                'Connection': '<Connection>',
                'Host': '<Host>',
                'kbn-version': '<kbn-version>',
                'Origin': '<Origin>',
                'Referer': '<Referer>',
                'User-Agent': '<User-Agent>',
                'Cookie': '<Cookie>',
            }

        # sign = getSign(msg=json.loads(data), key=signKey)
        # log.debug(sign)
        # headers['sign'] = sign
        log.info(f'data: {data}')

        if isForm:
            log.debug('isForm True')
            headers['Content-Type'] = "application/x-www-form-urlencoded; charset=UTF-8"
            resp = requests.request('POST', url=url, data=data, headers=headers)
        else:
            log.debug('isForm False')
            headers['Content-Type'] = "application/json; charset=UTF-8"
            resp = requests.request('POST', url=url, json=json, headers=headers)
            # resp.status_code
            # resp.json()
            # resp.text
        return resp

if __name__ == '__main__':
    resp = Http.get(url='https://www.baidu.com/s', data="wd=2022中国人均gdp")
    print(resp.status_code)
    print(resp.text)