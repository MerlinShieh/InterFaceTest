# -*- coding:utf-8 -*-
# @Time    : 2023/3/22
# @Author  : Merlin
# @File    : APiSend.py
# *************************

import time
from config import INTERVAL, FAKE_HEADERS
from utils import log, logger, BASE_DIR
from utils import apiMethod
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def send_request(case_data, test_info=None):
    """
    封装请求
    :param test_info: 测试信息
    :param case_data: 用例数据
    :return:
    """
    try:
        # 获取用例基本信息
        _method = case_data["request"]["method"].upper()  # 请求方式
        _url = case_data["request"]["url"]  # 主机地址
        _path = case_data["request"]["path"]  # 接口地址
        _headers = case_data["request"]["headers"]  # 请求头
        if _headers:
            _headers.update(FAKE_HEADERS)
        else:
            _headers = FAKE_HEADERS
        _mime_type = case_data["request"]["mime_type"]
        _json = case_data["request"]["json"]  # json数据
        _data = case_data["request"]["data"]  # data类型数据
        _params = case_data["request"]["params"]  # get参数
        _file = case_data["request"]["file"]
        _cookies = case_data["request"]["cookies"]
        _timeout = case_data["request"]["timeout"]
        _validate = case_data["validate"]  # 断言描述
    except Exception as e:
        log.error('获取用例基本信息失败：{}'.format(e))
        raise KeyError('获取用例基本信息失败：{}'.format(e))

    request_url = _url + _path
    log.info("=" * 150)

    # 判断接口请求类型
    result = {"code": None, "data": f"{_method} Method error"}
    if _method == 'POST':
        log.info("请求方法: POST")
        # 判断是否上传文件
        if _file:
            # with allure.step("POST上传文件"):
            #     allure.attach(name="请求接口", body=str(summary))
            #     allure.attach(name="请求地址", body=request_url)
            #     allure.attach(name="请求头", body=str(headers))
            #     allure.attach(name="请求参数", body=str(parameter))
            # result = apiMethod.post(headers=headers,
            #                         address=request_url,
            #                         mime_type=mime_type,
            #                         files=parameter,
            #                         cookies=cookies,
            #                         timeout=timeout)
            ...
        else:
            result = apiMethod.post(headers=_headers,
                                    address=request_url,
                                    mime_type=_mime_type,
                                    data=_data,
                                    json=_json,
                                    cookies=_cookies,
                                    timeout=_timeout)
    elif _method == 'GET':
        log.info("请求方法: GET")
        result = apiMethod.get(headers=_headers,
                               address=request_url,
                               data=_params,
                               cookies=_cookies,
                               timeout=_timeout)
    elif _method == 'PUT':
        log.info("请求方法: PUT")
        # 判断是否上传文件
        # if _file:
        #     # with allure.step("PUT上传文件"):
        #     #     allure.attach(name="请求接口", body=str(summary))
        #     #     allure.attach(name="请求地址", body=request_url)
        #     #     allure.attach(name="请求头", body=str(headers))
        #     #     allure.attach(name="请求参数", body=str(parameter))
        #     result = apiMethod.put(headers=headers,
        #                            address=request_url,
        #                            mime_type=_mini_type,
        #                            files=parameter,
        #                            cookies=cookies,
        #                            timeout=timeout)
        # else:
        #     # with allure.step("PUT请求接口"):
        #     #     allure.attach(name="请求接口", body=str(summary))
        #     #     allure.attach(name="请求地址", body=request_url)
        #     #     allure.attach(name="请求头", body=str(headers))
        #     #     allure.attach(name="请求参数", body=str(parameter))
        #     result = apiMethod.put(headers=headers,
        #                            address=request_url,
        #                            mime_type=_mini_type,
        #                            data=parameter,
        #                            cookies=cookies,
        #                            timeout=timeout)
    elif _method == 'DELETE':
        log.info("请求方法: DELETE")
        result = apiMethod.delete(headers=_headers,
                                  address=request_url,
                                  data=_data,
                                  json=_json,
                                  cookies=_cookies,
                                  timeout=_timeout)
    else:
        ...
    log.info(f"请求接口结果：{str(result)}")
    time.sleep(INTERVAL)
    return result


if __name__ == '__main__':
    import readFile
    import os

    yaml_f = readFile.readYaml(os.path.join(BASE_DIR, 'testCase', 'test_0001_HTTPMethods', 'test_HTTPMethods.yaml'))
    for case_data in yaml_f:
        log.debug(case_data['request'])
        resp = send_request(case_data)
