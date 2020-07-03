# -*- coding: utf-8 -*-
# *******************************************#
# project:InterFaceTestdemo
# fileName:testMain
# author:Merlin
# dataTime:2020/6/27-0:03
# *******************************************#
import unittest
import ddt
import sys
import traceback
import public_func.readExcel
import public_func.HTMLTestRunner
import public_func.sendEmail
import public_func.sendEmail
import public_func.setInfo
import public_func.useApi
import config.cfg

# 测试用例执行次数
count = 1
# 导入所有的Excelcase
excelCase = public_func.readExcel.getExeclTestCaseList()
@ddt.ddt()
class testApiData(unittest.TestCase):
	def setUp(self) -> None:
		# 获取当前函数名称 放入日志中
		funcName = sys._getframe().f_code.co_name
		public_func.setInfo.write_log(modle=funcName, message=str('----------测试开始---------'))
		public_func.setInfo.write_log(modle=funcName, message='第{}次执行用例'.format(count))
	@ddt.data(*excelCase)
	def test_case_001(self, itme):
		'''
		测试用例
		:param itme:迭代器，每次获取一个测试用例数据的字典
		:return:
		'''
		funcName = sys._getframe().f_code.co_name
		'''测试数据: {0}'''
		if str(itme["model"]) == "GET":
			try:
				public_func.setInfo.write_log(modle=funcName, message=itme)
				url = itme['host']
				data = itme['data'].replace(" ", "")
				public_func.setInfo.write_log(modle=funcName, url=url, type=data)
				resp = public_func.useApi.SendHttp().getHttp(url=url, params=data)
				public_func.setInfo.write_log(modle=funcName, param="status", resp=(str(resp.text)[:300]))
				assert resp.status_code == "200"
			except:
				error = traceback.format_exc()
				public_func.setInfo.write_log(modle=funcName, param="Error", Error=error)
			finally:
				self.assertEqual(str(resp.status_code), '200')
			pass
		elif str(itme["model"]) == "POST":

			public_func.setInfo.write_log(modle=funcName, message=itme)
			url = itme['host']
			data = eval(itme['data'].replace(" ", ""))
			public_func.setInfo.write_log(modle=funcName, param="参数:", url=url, type=data)
			try:
				resp = public_func.useApi.SendHttp().postHttp(url=url, data=data)
				public_func.setInfo.write_log(modle=funcName, param="status", resp=(str(resp.text)[:300]))
			except:
				error = traceback.format_exc()
				public_func.setInfo.write_log(modle=funcName, param="Error", Error=error)
			finally:
				self.assertEqual(str(resp.status_code), '200')
				public_func.setInfo.write_log(modle=funcName, param="status_code", code=(str(resp.status_code), '200'))
			pass
		else:
			return False
		public_func.setInfo.write_log(modle=funcName, message='测试中')
	def tearDown(self) -> None:
		funcName = sys._getframe().f_code.co_name
		public_func.setInfo.write_log(modle=funcName, message=str('----------测试完成---------'))
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
	'''
	发送邮件
	public_func.sendEmail.send_mail(title='接口测试测试报告', content='接口测试已完成，结果已附件发送', file=report)
	'''
