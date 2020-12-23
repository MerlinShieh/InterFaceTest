# -*- coding: utf-8 -*-
# *******************************************#
# project:InterFaceTestdemo
# fileName:testMain
# author:Merlin
# dataTime:2020/12/12
# *******************************************#

import unittest
import ddt
import os
import traceback

import HTMLTestRunner
from httpApi import Http
import time
from readExcel import getExcelTestCaserList
from log import LogHandler, logger
import configparser
config = configparser.ConfigParser()
config.read('../config/config.ini', encoding='UTF-8')

'''
import configparser
config = configparser.ConfigParser()
config.read('../config/config.ini', encoding='UTF-8')


COUNTRY = config.get('Country', 'country')
TestTime = str(time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()))
Log_path = r"../report/{}/TestReport_{}_{}.log".format(
    str(time.strftime('%Y_%m_%d', time.localtime())), COUNTRY, TestTime)
Report_path = r'../report/{}/TestReport_{}_{}.html'.format(
    str(time.strftime('%Y_%m_%d', time.localtime())), COUNTRY, TestTime)


logger = LogHandler(log_name=Log_path,
                    log_level="DEBUG").create_logger()
reportHTML = Report_path

config.set('path', 'Log_path', Log_path)
config.set('path', 'Report_path', reportHTML)

with open(r'../config/config.ini', 'w+') as f:
    config.write(f)
'''


count = 1
excelCase = getExcelTestCaserList()


@ddt.ddt()
class testApiData(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        try:
            os.mkdir(r"../report/{}".format(str(time.strftime("%Y_%m_%d", time.localtime()))))
        except FileExistsError:
            pass

    def setUp(self) -> None:
        global STATUS
        logger.info('Test Start, Test Count: {}'.format(count))

    def tearDown(self) -> None:
        logger.info('Test Over\n')

        logger.info('{}{}{}{}{}'.format('\n', '*' * 30, STATUS, '*' * 30, '\n'))
        global count
        count += 1

    @ddt.data(*excelCase)
    def test_Case(self, itme):
        if str(itme['model']) == 'GET':
            url = itme['host']
            data = itme['data'].replace(' ', '')
            result = str(int(itme['result']))
            try:
                logger.debug('request GET url={}, data={}'.format(url, data))
                resp = Http().get(url=url, data=data)

                logger.debug('response  {}   {}'.format(resp.status_code, resp.text))
                self.assertEqual(str(result), str(resp.json()['code']))

                logger.info('result:{}  code:{}'.format(result, resp.json()['code']))
                global STATUS
                STATUS = 'PASS'


            except Exception:
                error = traceback.format_exc()
                logger.error('{}'.format(error))
                print(error)

                STATUS = 'FAIL'
                raise Exception

        elif str(itme['model']) == 'POST':
            url = itme['host']
            data = eval(itme['data'].replace(' ', ''))
            result = str(int(itme['result']))

            try:
                logger.debug('request  POST  url={}, data={}, signkey={}'
                             .format(url, data, '***'))
                resp = Http().post(url=url, data=data)
                logger.debug('response  {}   {}'.format(resp.status_code, resp.text))

                self.assertEqual(str(result), str(resp.json()['code']))
                logger.info('result:{}  code:{}'.format(result, resp.json()['code']))


                STATUS = 'PASS'


            except Exception:
                error = traceback.format_exc()
                logger.error('{}'.format(error))
                print(error)

                STATUS = 'FAIL'
                raise Exception
        else:
            return False


# if __name__ == "__main__":
#     unittest.main(verbosity=2)
if __name__ == "__main__":
    # run()
    cases = unittest.TestLoader().loadTestsFromTestCase(testApiData)

    COUNTRY = config.get('Country', 'country')
    if COUNTRY == "test":
        env = "测试环境接口测试测试报告"
    elif COUNTRY == "CN":
        env = "国内线上环境接口测试测试报告"
    elif COUNTRY == "EU":
        env = "欧盟线上环境接口测试测试报告"
    elif COUNTRY == "SG":
        env = "新加坡线上环境接口测试测试报告"
    else:
        env = "接口测试测试报告"
    with open(config.get('path', 'Report_path'), 'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, verbosity=2, title=env, description="测试案例执行结果")
        runner.run(cases)