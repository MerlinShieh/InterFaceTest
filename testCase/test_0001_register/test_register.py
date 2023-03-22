import json

import os

import pytest

# from com import
from log import log, logger, BASE_DIR
import readFile
import httpApi

yaml_f = readFile.readYaml(os.path.join(BASE_DIR, 'testCase', 'test_0001_register',  'test_register.yaml'))


class TestRegister:
    @pytest.mark.parametrize('caseinfo', yaml_f)
    @logger(__name__)
    def test_register(self, caseinfo):
        log.debug(f'开始运行用例 {caseinfo}')
        if caseinfo['request']['method'] == 'post':
            resp = httpApi.Http.post(
                url=caseinfo['request']['url'],
                data=json.dumps(caseinfo['request']['json'])
            )
            return resp.status_code, resp.text
        elif caseinfo['request']['method'] == 'get':
            resp = httpApi.Http.post(
                url=caseinfo['request']['url'],
                data=caseinfo['request']['params']
            )
            return resp.status_code, resp.text
        else:
            exit(-1)


if __name__ == '__main__':
    print(yaml_f)