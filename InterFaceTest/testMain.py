# -*- coding: utf-8 -*-
# *******************************************#
# project:InterFaceTestdemo
# fileName:testMain
# author:Merlin
# dataTime:2020/6/27-0:03
# *******************************************#
import unittest
import ddt
import public_func.useApi
import public_func.log
import public_func.readExcel
import public_func.HTMLTestRunner
import public_func.sendEmail
import config.cfg


excelCase = public_func.readExcel.getExeclTestCaseList()
@ddt.ddt()
class testApiData(unittest.TestCase):
	@ddt.data(*excelCase)
	def test_case_001(self, itme):
		'''测试数据: {0}'''
		if str(itme["model"]) == "GET":
			res = public_func.useApi.SendHttp().getHttp(url=itme["host"], params=itme["data"])
			self.assertEqual(str(res.status_code), '200')
			public_func.log.setLog(leavel='info', message=res.text)
		elif str(itme["model"]) == "POST":
			res = public_func.useApi.SendHttp().postHttp(url=itme["host"], data=itme["data"])
			self.assertEqual(str(res.status_code), '200')
			public_func.log.setLog(leavel='info', message=res.text)
		else:
			return False

if __name__=="__main__":
	cases = unittest.TestLoader().loadTestsFromTestCase(testApiData)
	report = config.cfg.report_path
	with open(report, 'wb') as f:
		runner = public_func.HTMLTestRunner.HTMLTestRunner(stream=f, verbosity=2, title="接口测试测试报告", description="测试案例执行结果")
		runner.run(cases)
	public_func.sendEmail.send_mail(title='接口测试测试报告', content='接口测试已完成，结果已附件发送', file=report)