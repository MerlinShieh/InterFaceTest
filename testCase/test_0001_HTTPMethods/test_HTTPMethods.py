import json

import os
import pytest
import readFile
from utils import apiSend, log, logger, BASE_DIR

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


class TestHTTP:
    @pytest.mark.parametrize('caseinfo', yaml_f)
    @logger(__name__)
    def test_http(self, caseinfo):
        log.debug(f'开始运行用例 {caseinfo}')
        resp = apiSend.send_request(caseinfo)
        log.debug('code: {}; data: {}', resp[0], resp[1])


if __name__ == '__main__':
    print(yaml_f)
