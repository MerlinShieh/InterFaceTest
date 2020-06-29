#-*- coding: utf-8 -*-
import os
import time
root_path = os.path.abspath(os.path.dirname(__file__)).split('InterFaceTestdemo')[0]
# 获取项目根路径
testCaseExcel_path = root_path+'InterFaceTestdemo\\InterFaceTest\\testcase\\testCase.xlsx'

report_path = root_path+'InterFaceTestdemo\\InterFaceTest\\report\\TestReport_{}.html'.format(str(time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())))
log_path = root_path+'InterFaceTestdemo\\InterFaceTest\\report\\log.log'

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
	print(log_path['log_info_path'])
	print(testCaseExcel_path)
	root_path = os.path.abspath(os.path.dirname(__file__)).split('\\InterFaceTestdemo')[0]
	print(root_path)