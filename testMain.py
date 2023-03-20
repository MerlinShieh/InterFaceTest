# -*- encoding: utf-8 -*-
"""
@File        :testMain.py
@README      :接口测试主要文件，进入到当前文件夹 com ，执行 Python ./testMain.py
                直接 python ./com/testMain.py 会出现 FileNotFount
@Time        :2020/12/29 19:29:35
@Author      :Merlin
@Version     :1.0
"""
import json
import unittest
import ddt
import os
import traceback
import time
import configparser
# from com.HTMLTestRunner import HTMLTestRunner
from XTestRunner import HTMLTestRunner

from com.log import log, logger, BASE_DIR
from com.httpApi import Http
from com.readExcel import getExcelTestCaseList

config = configparser.ConfigParser()
config.read(os.path.join(BASE_DIR, 'config/config.ini'), encoding='UTF-8')

count = 1
excelCase = getExcelTestCaseList()


@ddt.ddt()
class TestApiData(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        global STATUS

    def setUp(self) -> None:

        log.info('Test Start, Test Count: {}'.format(count))

    def tearDown(self) -> None:
        log.info('Test Over\n\n')
        global count
        count += 1

    @ddt.data(*excelCase)
    def test_Case(self, itme: dict):

        # table_values = ['_number', '_ame', '_host', '_path', '_method', '_type', '_data', '_assert']
        global resp, STATUS

        _number, _ame, _host, _path, _method, _type, _data, _assert = itme.values()
        log.debug(itme.values())
        try:
            if str(itme['_method']) == 'GET':
                resp = Http().get(url=_host + _path, data=_data)
            elif str(itme['_method']) == 'POST':
                resp = Http().post(url=_host + _path, data=_data)
            log.info(f"resp.text: {resp.text}")
        except Exception as e:
            log.debug('Test Error')
            log.error(e)
            STATUS = 'FAIL'
        if self.assertEqual(int(_assert), int(resp.json()['code'])) is None:
            log.debug('Test Pass')
            STATUS = 'PASS'
        else:
            log.debug('Test Fail')
            STATUS = 'FAIL'
        self.assertEqual(int(_assert), int(resp.json()['code']))


#
# if __name__ == "__main__":
#     unittest.main(verbosity=2)
if __name__ == "__main__":
    # run()
    cases = unittest.TestLoader().loadTestsFromTestCase(TestApiData)

    SHEET = config.get('path', 'sheet')
    if SHEET == "test":
        env = "测试环境接口测试测试报告"
    else:
        env = "接口测试测试报告"

    report_path = os.path.join(BASE_DIR, r'report', str(time.strftime("%Y_%m_%d", time.localtime())))
    try:
        os.mkdir(report_path)
        log.debug('create success')
    except FileExistsError:
        log.debug('directory FileExistsError')

    report_path = os.path.join(BASE_DIR, r'report', str(time.strftime("%Y_%m_%d", time.localtime())),
                               log.name + '.html')
    log.info(report_path)
    with open(report_path, 'wb') as f:
        runner = HTMLTestRunner(
            stream=f, verbosity=2, title=env, description="测试案例执行结果")
        runner.run(cases)
