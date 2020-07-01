#-*- coding: utf-8 -*-
import os
import time
import sys
root_path = os.path.abspath(os.path.dirname(__file__)).split('InterFaceTestdemo')[0]
if str(sys.platform) == ('linux') or ('darwin'):
	# 检查当前是Linux、macOS还是Windows操作系统，因为Windows系统的路径与 *inux 不同
	report_path = root_path + 'InterFaceTestdemo/InterFaceTest/report/TestReport_{}.html'.format(
		str(time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())))
	testCaseExcel_path = root_path + 'InterFaceTestdemo/InterFaceTest/testcase/testCase.xlsx'
	log_path = root_path + 'InterFaceTestdemo/InterFaceTest/report/log_{}.txt'.format(
		str(time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())))
else:
	testCaseExcel_path = root_path+'InterFaceTestdemo\\InterFaceTest\\testcase\\testCase.xlsx'
	report_path = root_path+'InterFaceTestdemo\\InterFaceTest\\report\\TestReport_{}.html'.format(
		str(time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())))
	log_path = root_path+'InterFaceTestdemo\\InterFaceTest\\report\\log_{}.log'.format(
		str(time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())))
email = {
	'username': 'xxxx@163.com',
	'passwd': 'xxxxx',
	'recv': 'xxxx@163.com',
	'title': '主题',
	'content': '正文',
	'mail_host': 'smtp.163.com',
	'port': 25,
	'file': None
}


if __name__ == "__main__":
    print(testCaseExcel_path)