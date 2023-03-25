# -*- coding:utf-8 -*-
# @Time    : 2023/3/22
# @Author  : Merlin
# @File    : APiSend.py
# *************************

import time

from log import log, logger, BASE_DIR
from utils import apiMethod
from config import INTERVAL


@logger(__name__)
def send_request(case_data, test_info=None):
    """
    封装请求
    :param test_info: 测试信息
    :param case_data: 用例数据
    :return:
    """
    try:
        # 获取用例基本信息
        host = case_data["host"]  # 主机地址
        scheme = case_data["scheme"]  # 请求协议 http/https
        method = case_data["method"].upper()  # 请求方式 POST GET
        address = case_data["address"]  # 接口地址
        mime_type = case_data["mime_type"]  # 请求参数格式（form_data,raw, json）
        headers = case_data["headers"]  # 请求头
        cookies = case_data["cookies"]  # Cookies
        file = case_data["file"]  # 上传的文件
        timeout = case_data["timeout"]  # 超时
        summary = case_data["summary"]  # 接口描述
        parameter = case_data["parameter"]  # 请求参数
    except Exception as e:
        raise KeyError('获取用例基本信息失败：{}'.format(e))

    request_url = scheme + "://" + host + address
    log.info("=" * 150)

    # 判断是否保存cookies
    if summary == 'save_cookies':
        # with allure.step("保存cookies信息"):
        #     allure.attach(name="请求接口", body=str(summary))
        #     allure.attach(name="请求地址", body=request_url)
        #     allure.attach(name="请求头", body=str(headers))
        #     allure.attach(name="请求参数", body=str(parameter))
        apiMethod.save_cookie(headers=headers,
                              address=request_url,
                              mime_type=mime_type,
                              data=parameter,
                              cookies=cookies,
                              timeout=timeout)
    # 判断接口请求类型
    if method == 'POST':
        log.info("请求方法: POST")
        # 判断是否上传文件
        if file:
            # with allure.step("POST上传文件"):
            #     allure.attach(name="请求接口", body=str(summary))
            #     allure.attach(name="请求地址", body=request_url)
            #     allure.attach(name="请求头", body=str(headers))
            #     allure.attach(name="请求参数", body=str(parameter))
            result = apiMethod.post(headers=headers,
                                    address=request_url,
                                    mime_type=mime_type,
                                    files=parameter,
                                    cookies=cookies,
                                    timeout=timeout)
        else:
            # with allure.step("POST请求接口"):
            #     allure.attach(name="请求接口", body=str(summary))
            #     allure.attach(name="请求地址", body=request_url)
            #     allure.attach(name="请求头", body=str(headers))
            #     allure.attach(name="请求参数", body=str(parameter))
            result = apiMethod.post(headers=headers,
                                    address=request_url,
                                    mime_type=mime_type,
                                    data=parameter,
                                    cookies=cookies,
                                    timeout=timeout)
    elif method == 'GET':
        log.info("请求方法: GET")
        # with allure.step("GET请求接口"):
        #     allure.attach(name="请求接口", body=str(summary))
        #     allure.attach(name="请求地址", body=request_url)
        #     allure.attach(name="请求头", body=str(headers))
        #     allure.attach(name="请求参数", body=str(parameter))
        result = apiMethod.get(headers=headers,
                               address=request_url,
                               data=parameter,
                               cookies=cookies,
                               timeout=timeout)
    elif method == 'PUT':
        log.info("请求方法: PUT")
        # 判断是否上传文件
        if file:
            # with allure.step("PUT上传文件"):
            #     allure.attach(name="请求接口", body=str(summary))
            #     allure.attach(name="请求地址", body=request_url)
            #     allure.attach(name="请求头", body=str(headers))
            #     allure.attach(name="请求参数", body=str(parameter))
            result = apiMethod.put(headers=headers,
                                   address=request_url,
                                   mime_type=mime_type,
                                   files=parameter,
                                   cookies=cookies,
                                   timeout=timeout)
        else:
            # with allure.step("PUT请求接口"):
            #     allure.attach(name="请求接口", body=str(summary))
            #     allure.attach(name="请求地址", body=request_url)
            #     allure.attach(name="请求头", body=str(headers))
            #     allure.attach(name="请求参数", body=str(parameter))
            result = apiMethod.put(headers=headers,
                                   address=request_url,
                                   mime_type=mime_type,
                                   data=parameter,
                                   cookies=cookies,
                                   timeout=timeout)
    elif method == 'DELETE':
        log.info("请求方法: DELETE")
        # with allure.step("DELETE请求接口"):
        #     allure.attach(name="请求接口", body=str(summary))
        #     allure.attach(name="请求地址", body=request_url)
        #     allure.attach(name="请求头", body=str(headers))
        #     allure.attach(name="请求参数", body=str(parameter))
        result = apiMethod.delete(headers=headers,
                                  address=request_url,
                                  data=parameter,
                                  cookies=cookies,
                                  timeout=timeout)
    else:
        result = {"code": None, "data": None}
    log.info("请求接口结果：\n %s" % str(result))
    time.sleep(INTERVAL)
    return result


if __name__ == '__main__':
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
    data = {
        'username': 'abc',
        'passwd': '123'
    }
    case_data = {
        'host': '127.0.0.1:5000',
        'scheme': 'http',
        'method': 'post',
        'address': '/register',
        'mime_type': 'json',
        'headers': headers,
        'cookies': None,
        'file': None,
        'timeout': 1,
        'summary': '第一个接口',
        'parameter': data

    }
    add = send_request(case_data)
    case_data['address'] = '/delete'
    dele = send_request(case_data)