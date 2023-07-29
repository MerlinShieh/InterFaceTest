# -*- coding:utf-8 -*-
# @Time    : 2023/7/27
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
from utils import log, logger, BASE_DIR


@log.catch
def read_yaml_data(yaml_file, **kwargs):
    """读取yaml文件数据
    :param yaml_file: yaml文件地址
    :return:
    """
    log.debug(f'读取文件:{yaml_file}')
    log.debug(f'字典参数 {kwargs}')
    new_list = []
    with open(yaml_file, 'r', encoding="utf-8") as fr:
        yaml_list = yaml.load(fr, Loader=yaml.SafeLoader)
        log.info('读取到的用例源数据:')
        dic = {}
        for key in kwargs:
            dic[key] = kwargs[key]
        for _data_dict in yaml_list:
            template_data_str = Template(json.dumps(_data_dict))
            _data_str = template_data_str.safe_substitute(dic)
            _data_list = json.loads(_data_str)
            log.debug('原始数据\n{}', _data_dict)
            log.debug('替换模板\n{}\n\n ', _data_list)
            new_list.append(_data_list)
    return new_list


@log.catch
def write_yaml_file(yaml_file, obj):
    """把对象obj写入yaml文件
    :param yaml_file: yaml文件地址
    :param obj: 数据对象
    :return:
    """
    log.debug(f'写入文件:{yaml_file}')
    with open(yaml_file, encoding="utf-8", mode="w") as fw:
        yaml.dump(obj, stream=fw, allow_unicode=True)
        return True


if __name__ == '__main__':
    file = read_yaml_data(
        os.path.join(BASE_DIR, r'testCase/test_0001_HTTPMethods/test_HTTPMethods.yaml'),
        TOKEN='token123')
