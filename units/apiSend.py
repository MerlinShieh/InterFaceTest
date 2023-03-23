# -*- coding:utf-8 -*-
# @Time    : 2023/3/22
# @Author  : Merlin
# @File    : ApiSend.py
# *************************

import os
import json
import random
import requests
import simplejson
from requests_toolbelt import MultipartEncoder

from log import log, logger, BASE_DIR


def post(headers, address, mime_type, timeout=10, data=None, files=None, cookies=None):
    """
    post请求
    :param headers: 请求头
    :param address: 请求地址
    :param mime_type: 请求参数格式（form_data,raw）
    :param timeout: 超时时间
    :param data: 请求参数
    :param files: 上传文件请求参数（dict）
    :param cookies:
    :return:
    """
    # 判断请求参数类型
    if 'form_data' in mime_type:
        for key in files:
            value = files[key]
            # 判定参数值是否为文件，如果是则替换为二进制值
            if '/' in value:
                files[key] = (os.path.basename(value), open(value, 'rb'))
        enc = MultipartEncoder(
            fields=files,
            boundary='--------------' + str(random.randint(1e28, 1e29 - 1))
        )
        headers['Content-Type'] = enc.content_type
        response = requests.post(url=address,
                                 data=enc,
                                 headers=headers,
                                 timeout=timeout,
                                 cookies=cookies,
                                 verify=False)
    elif 'application/json' in mime_type:
        response = requests.post(url=address,
                                 data=data,
                                 headers=headers,
                                 timeout=timeout,
                                 files=files,
                                 cookies=cookies,
                                 verify=False)
    else:
        response = requests.post(url=address,
                                 json=data,
                                 headers=headers,
                                 timeout=timeout,
                                 files=files,
                                 cookies=cookies,
                                 verify=False)
    try:
        if response.status_code != 200:
            return response.status_code, response.text
        else:
            return response.status_code, response.json()
    except json.decoder.JSONDecodeError:
        return response.status_code, None
    except simplejson.errors.JSONDecodeError:
        return response.status_code, None
    except Exception as e:
        logging.exception('ERROR')
        logging.error(e)
        raise

