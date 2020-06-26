#-*- coding: utf-8 -*-
import unittest
import ddt
import useApi
import readExcel
import HTMLTestRunner
import log
excelCase = readExcel.getExcelTestCaseList()
@ddt.ddt()
class ApiData(unittest.TestCase):
    @ddt.data(*excelCase)
    # @unpack
    def test_01_case(self, itme):
        '''测试数据{0}'''
        log.Log().info('测试数据{}'.format(itme))
        if str(itme["model"]) == "GET":
            res = useApi.SendHttp().getHttp(url=itme["host"], params=itme["data"])
            self.assertEqual(str(res.status_code), '200')
            log.Log().info('{}'.format(str(res.text)), filename='test1.log')
            log.Log().info('{}'.format(str(res.status_code)))
        elif str(itme["model"]) == "POST":
            res = useApi.SendHttp().postHttp(url=itme["host"], data=itme["data"])
            self.assertEqual(str(res.status_code), '200')
            log.Log().info('{}'.format(str(res.status_code)))
            log.Log().info('{}'.format(str(res.text)))
        else:
            log.Log().error('{}'.format(itme["model"]))
            return False
    @ddt.data(*excelCase)
    def test_02_case(self, itme):
        '''测试数据{0}'''
        if str(itme["model"]) == "GET":
            res = useApi.SendHttp().getHttp(url=itme["host"], params=itme["data"])
            self.assertEqual(str(res.status_code), '200')
        elif str(itme["model"]) == "POST":
            res = useApi.SendHttp().postHttp(url=itme["host"], data=itme["data"])
            self.assertEqual(str(res.status_code), '200')

    def suite(self):
        cases = unittest.TestLoader().loadTestsFromTestCase(ApiData)
        suite = unittest.TestSuite([cases])
        report_path = 'HTMLReport.html'
        print(suite)
        
if __name__=="__main__":

    cases = unittest.TestLoader().loadTestsFromTestCase(ApiData)
    report_path = 'HTMLReport.html'
    f = open(report_path, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, verbosity=2, title="接口测试测试报告", description="测试案例执行结果")
    runner.run(cases)
    f.close()