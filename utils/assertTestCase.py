# -*- coding:utf-8 -*-
# @Time    : 2023/7/28
# @Author  : Merlin
# @File    : readWriteYaml.py
# ***********************
import traceback
import json
import ast
import os
import yaml
import re
from string import Template
# from utils import log, logger, BASE_DIR
from typing import List, Tuple

validate = [
    {'isJSON': True}
]
resp = (
    200,
    {'args': {}, 'data': ''}
)


class AssertData:

    @staticmethod
    def inData(key, resp):
        return key in resp

    @staticmethod
    def isJSON(key, value: bool):
        print(key, value)
        return bool(key) == value


def testAssert(key, resp):
    # isJSON
    # True

    # getattr(AssertData, k)(resp, v)
    AssertData.isJSON(key=resp[1], value=v)


if __name__ == '__main__':
    print(testAssert(validate, resp))
