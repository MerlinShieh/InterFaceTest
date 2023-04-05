import json

import os

import pytest

# from com import
from log import log, logger, BASE_DIR
import readFile
from utils import apiSend

yaml_f = readFile.readYaml(os.path.join(BASE_DIR, 'testCase', 'test_0001_HTTPMethods', 'test_HTTPMethods.yaml'))
'''
{'feature': 'HTTP 方法', 'story': 'POST方式', 'title': 'POST使用json参数', 
    'request': 
        {'method': 'post', 'url': 'https://echo.apifox.com', 'path': '/post', 
        'headers': {'Content-Type': 'application/json'}, 'mime_type': 'application/json', 
        'json': 
            {'username': 'PostMethod', 'passwd': 'json'}, 'data': None, 'params': None, 'file': None, 'cookies': None, 'timeout': 1}, 
    'validate': None}
        '''


class TestRegister:
    @pytest.mark.parametrize('caseinfo', yaml_f)
    @logger(__name__)
    def test_register(self, caseinfo):
        log.debug(f'开始运行用例 {caseinfo}')
        # if caseinfo['request']['method'] == 'post':
        #     resp = httpApi.Http.post(
        #         url=caseinfo['request']['url'],
        #         data=json.dumps(caseinfo['request']['json'])
        #     )
        #     return resp.status_code, resp.text
        # elif caseinfo['request']['method'] == 'get':
        #     resp = httpApi.Http.post(
        #         url=caseinfo['request']['url'],
        #         data=caseinfo['request']['params']
        #     )
        #     return resp.status_code, resp.text
        # else:
        #     exit(-1)
        resp = apiSend.send_request(caseinfo)
        print(resp)


if __name__ == '__main__':
    print(yaml_f)
