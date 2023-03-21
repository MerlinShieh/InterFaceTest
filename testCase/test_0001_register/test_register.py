import os

import pytest

from com import BASE_DIR
from com.log import log, logger
from com import readFile

yaml_f = readFile.readYaml(os.path.join(BASE_DIR, 'testCase', 'test_0001_register',  'test_register.yaml'))


class TestRegister:

    @pytest.mark.parametrize('caseinfo', yaml_f)
    @logger(__file__)
    def test_register(self, caseinfo):
        log.debug(caseinfo)


if __name__ == '__main__':
    print(yaml_f)