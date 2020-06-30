# -*- coding: utf-8 -*-
# *******************************************#
# project:InterFaceTestdemo
# fileName:testMain
# author:Merlin
# dataTime:2020/6/27-0:03
# *******************************************#
import unittest
import ddt
import public_func.readExcel
import public_func.HTMLTestRunner
import public_func.sendEmail
import public_func.sendEmail
import public_func.setInfo
import config.cfg
import public_func.useApi
import sys

count = 1
excelCase = public_func.readExcel.getExeclTestCaseList()
@ddt.ddt()
class testApiData(unittest.TestCase):
	def setUp(self) -> None:
		funcName = sys._getframe().f_code.co_name
		public_func.setInfo.write_log(modle=funcName, message=str('----------测试开始---------'))
		public_func.setInfo.write_log(modle=funcName, message='第{}次执行用例'.format(count))
	@ddt.data(*excelCase)
	def test_case_001(self, itme):
		funcName = sys._getframe().f_code.co_name
		'''测试数据: {0}'''
		if str(itme["model"]) == "GET":
			try:
				res = public_func.useApi.SendHttp().getHttp(url=itme["host"], params=itme["data"])
				public_func.setInfo.write_log(modle=funcName, message=str(res.status_code))
				public_func.setInfo.write_log(modle=funcName, message=str(res.text))
			except Exception as e:
				public_func.setInfo.write_log(modle=funcName, message=str('----------接口错误---------'))
				public_func.setInfo.write_log(modle=funcName, message=str(e))
				public_func.setInfo.write_log(modle=funcName, message=str('----------接口错误---------'))
			finally:
				self.assertEqual(str(res.status_code), '200')
				public_func.setInfo.write_log(modle=funcName, message="----断言完成,实际结果status_code:{},预期结果:{}".format(res.status_code, '200'))

		elif str(itme["model"]) == "POST":
			try:
				res = public_func.useApi.SendHttp().postHttp(url=itme["host"], data=itme["data"])
				public_func.setInfo.write_log(modle=funcName, message=str(res.status_code))
				public_func.setInfo.write_log(modle=funcName, message=str(res.text))
			except Exception as e:
				public_func.setInfo.write_log(modle=funcName, message=str('----------接口错误---------'))
				public_func.setInfo.write_log(modle=funcName, message=str(e))
				public_func.setInfo.write_log(modle=funcName, pmessage=str('----------接口错误---------'))
			finally:
				self.assertEqual(str(res.status_code), '200')
				public_func.setInfo.write_log(modle=funcName,message="----断言完成,实际结果status_code:{},预期结果:{}".format(res.status_code, '200'))
		else:
			return False
		public_func.setInfo.write_log(modle=sys._getframe().f_code.co_name, message='测试中')
	def tearDown(self) -> None:
		public_func.setInfo.write_log(modle=sys._getframe().f_code.co_name, message=str('----------测试完成---------'))
		global count
		count += 1

# if __name__=="__main__":
# 	unittest.main(verbosity=2)
if __name__=="__main__":
	cases = unittest.TestLoader().loadTestsFromTestCase(testApiData)
	public_func.setInfo.write_log(modle=sys._getframe().f_code.co_name, message='cases加载完成')
	public_func.setInfo.write_log(modle=sys._getframe().f_code.co_name, message=str(cases))
	report = config.cfg.report_path
	with open(report, 'wb') as f:
		runner = public_func.HTMLTestRunner.HTMLTestRunner(stream=f, verbosity=2, title="接口测试测试报告", description="测试案例执行结果")
		runner.run(cases)
		public_func.setInfo.write_log(modle=sys._getframe().f_code.co_name, message="测试报告生成完成，stream=f, verbosity=2, title='接口测试测试报告', description='测试案例执行结果'")
	# public_func.sendEmail.send_mail(title='接口测试测试报告', content='接口测试已完成，结果已附件发送', file=report)
