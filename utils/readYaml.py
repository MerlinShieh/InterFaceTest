# -*- coding:utf-8 -*-
# @Time    : 2023/3/23
# @Author  : Merlin
# @File    : readYaml.py
# ***********************
import os

import yaml
from utils import log, logger, BASE_DIR


def read_yaml_data(yaml_file):
    """读取yaml文件数据
    :param yaml_file: yaml文件地址
    :return:
    """
    log.debug(f'读取文件:{yaml_file}')
    with open(yaml_file, 'r', encoding="utf-8") as fr:
        return yaml.load(fr, Loader=yaml.SafeLoader)


def write_yaml_file(yaml_file, obj):
    """把对象obj写入yaml文件
    :param yaml_file: yaml文件地址
    :param obj: 数据对象
    :return:
    """
    log.debug(f'写入文件:{yaml_file}')
    with open(yaml_file, encoding="utf-8", mode="w") as fw:
        yaml.dump(obj, stream=fw, allow_unicode=True)


if __name__ == '__main__':
    print(read_yaml_data(os.path.join(BASE_DIR, r'testCase/test_0001_HTTPMethods/test_HTTPMethods.yaml')))
