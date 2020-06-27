#-*- coding: utf-8 -*-
import os
import time
root_path = os.path.abspath(os.path.dirname(__file__)).split('InterFaceTestdemo')[0]
# 获取项目根路径
testCaseExcel_path = root_path+'InterFaceTestdemo\\InterFaceTest\\testcase\\testCase.xlsx'

report_path = root_path+'InterFaceTestdemo\\InterFaceTest\\report\\TestReport_{}.html'.format(str(time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())))
# report_path = '/report/TestReport.html'
log_path = {
	'log_info_path': root_path+'InterFaceTestdemo\\InterFaceTest\\report\\info.log',
	'log_debug_path': root_path+'InterFaceTestdemo\\InterFaceTest\\report\\debug.log',
	'log_warn_path': root_path+'InterFaceTestdemo\\InterFaceTest\\report\\warning.log',
	'log_error_path': root_path+'InterFaceTestdemo\\InterFaceTest\\report\\error.log',
	'log_critical_path': root_path+'InterFaceTestdemo\\InterFaceTest\\report\\critical.log'
}
if __name__ == "__main__":
	print(log_path['log_info_path'])
	print(testCaseExcel_path)
	root_path = os.path.abspath(os.path.dirname(__file__)).split('\InterFaceTestdemo')[0]

	print(root_path)