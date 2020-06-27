#-*- coding: utf-8 -*-
import os
import time
testCaseExcel_path = os.getcwd()+'/testcase/testCase.xlsx'
report_path = '/report/TestReport_{}.html'.format(str(time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())))
# report_path = '/report/TestReport.html'
log_path = {
	'log_info_path': os.path.dirname(os.getcwd())+'/InterFaceTest/report/info.log',
	'log_debug_path': os.path.dirname(os.getcwd())+'/InterFaceTest/report/debug.log',
	'log_warn_path': os.path.dirname(os.getcwd())+'/InterFaceTest/report/warning.log',
	'log_error_path': os.path.dirname(os.getcwd())+'/InterFaceTest/report/error.log',
	'log_critical_path': os.path.dirname(os.getcwd())+'/InterFaceTest/report/critical.log'
}
if __name__ == "__main__":
	print(report_path)