# -*- coding:utf-8 -*-
# @Time    : 2023/3/23
# @Author  : Merlin
# @File    : readYaml.py
# ***********************
import traceback

import json
import ast
import os
import yaml
import re
from utils import log, logger, BASE_DIR


@log.catch
def read_yaml_data(yaml_file, **kwargs):
    """读取yaml文件数据
    :param yaml_file: yaml文件地址
    :return:
    """
    log.debug(f'读取文件:{yaml_file}')
    # TOKEN = '12332'
    with open(yaml_file, 'r', encoding="utf-8") as fr:
        yaml_list = yaml.load(fr, Loader=yaml.SafeLoader)
        log.info('读取到的用例源数据:')
        [log.debug(_) for _ in yaml_list]
        re_kw = r"""\$.*?(?="|')"""
        # 遍历找到所有的$关键字
        lst = []
        _yaml_list = []
        for _lst in yaml_list:
            # _lst 原始列表里面的数据
            kw_list = re.findall(re_kw, str(_lst))  # 这个查出来的都是每一条用例关键字 ${TOKEN}这种组成的列表
            # lst += __lst    # 把上面的关键字列表
            log.debug('__lst每条用例关键字组成的列表:')
            [log.debug(_) for _ in kw_list]
            for _sourceData in kw_list:
                # 遍历每一个关键字列表,
                log.debug('_sourceData每个列表的单个源数据 {}', _sourceData)

                # 把格式化完成的数据重新替换到源数据
                _evalData = _sourceData.replace('${', '').replace('}', '')
                log.debug('_evalData 每个列表的单个源数据进行去除$符号 {}', _evalData)
                try:
                    # 判断源数据格式化时有没有定义
                    # 每次判断完就更新这条用例数据
                    log.debug(f'{_evalData}格式化关键字数据类型: {type(_evalData)}')
                    log.debug(f'{_evalData}格式化关键字: {eval(_evalData)}')
                    _strEvalData = str(eval(_evalData))
                    log.debug('_evalData格式化关键字转str: {}', _strEvalData)
                except NameError as e:
                    log.error('eval格式化数据失败,存在未定义数据, {}', traceback.extract_stack())

                    log.debug('_evalData格式化关键字: {}', _evalData)
                    # 实际不进行更新
                    _strEvalData = _sourceData
                finally:
                    # 如果是文件路径,就把斜杠替换下
                    if os.path.isfile(_strEvalData):
                        log.debug('检测到文件路径 {}', _strEvalData)
                        _strEvalData = _strEvalData.replace('\\', '/')
                        log.debug('进行斜杠替换 --->{}', _strEvalData)
                    _lst = str(_lst).replace(_sourceData, _strEvalData)
                    _lst = json.loads(json.dumps(eval(_lst)))
            # 每条用例更新完成,把新用例添加进新列表
            log.debug('_lst每条用例更新完成,把新用例添加进新列表 {} {}', type(_lst), _lst)
            _yaml_list.append(_lst)
            [log.debug(f'{_}') for _ in _lst]
        log.debug('_yaml_list转换完成的所有用例:')
        [log.debug(f'{_}') for _ in _yaml_list]
    return _yaml_list


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
    TOKEN = '12332'
    file = read_yaml_data(os.path.join(BASE_DIR, r'testCase/test_0001_HTTPMethods/test_HTTPMethods.yaml'))
    [print(f) for f in file]