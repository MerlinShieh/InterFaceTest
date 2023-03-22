# -*- coding: utf-8 -*-

# *******************************************#
# project:HeyMylody
# fileName:httpApi
# author:Merlin
# dataTime:2020/12/12
# *******************************************#

import configparser
import json

import requests

from com.log import logger, log, BASE_DIR

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
        resp = requests.request('GET', url=url, headers=headers, params=data)
        return resp

    @staticmethod
    @logger(__name__)
    def post(url: str, data: str, headers=None, isForm=True):
        """
        不需要做加密的可以把这里重写
        :param isForm: 默认采用表单提交 bool
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
            resp = requests.request('POST', url=url, data=json.loads(data), headers=headers)
        else:
            log.debug('isForm False')
            headers['Content-Type'] = "application/json; charset=UTF-8"
            resp = requests.request('POST', url=url, json=data, headers=headers)
            # resp.status_code
            # resp.json()
            # resp.text
        return resp
