# -*- coding: utf-8 -*-
# *******************************************#
# project:InterFaceTestdemo
# fileName:testMain
# author:Merlin
# dataTime:2020/12/12
# *******************************************#

import unittest
import ddt
import sys
import traceback
from httpApi import Http
from httpApi import HttpError
from readExcel import getExcelTestCaserList

count = 1
excelCase = getExcelTestCaserList()


@ddt.ddt()
class testApiData(unittest.TestCase):
    def setUpClass(cls) -> None:
        pass

    def setUp(self) -> None:
        print('Test Start, Test Count: {}'.format(count))

    def tearDown(self) -> None:
        print('Test Over')
        global count
        count += 1

    @ddt.data(*excelCase)
    def test_Case(self, itme):

        if str(itme['model']) == 'GET':
            url = itme['host']
            data = itme['data'].replace(' ', '')
            result = str(int(itme['result']))
            try:
                resp = Http().get(url=url, data=data)
                if not resp.status_code == '200':
                    raise HttpError
                code = str(resp.json()['code'])
                print(resp.text)
                self.assertEqual(result, code)
            except HttpError:
                print('requests Error, status != 200')
                raise HttpError
            except NameError:
                error = traceback.format_exc()
                print(error)
                raise NameError
            except Exception:
                raise

        elif str(itme['model']) == 'POST':
            url = itme['host']
            data = eval(itme['data'].replace(' ', ''))
            result = str(int(itme['result']))

            try:
                resp = Http().post(url=url, data=data, signKey=None)
                if not resp.status_code == '200':
                    raise HttpError
                code = str((resp.json()['code']))
                print(resp.text)
                self.assertEqual(result, code)
            except HttpError:
                print('requests Error, status != 200')
                raise HttpError

            except NameError:
                error = traceback.format_exc()
                print(error)
                raise NameError
            except Exception:
                raise
        else:
            return False


if __name__ == "__main__":
    unittest.main(verbosity=2)
