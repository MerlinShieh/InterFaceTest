#-*- coding: utf-8 -*-
import os
testCaseExcel_path = os.getcwd()+'/testcase/testCase.xlsx'
report_path = '/report/TestReport.html'
log_path = {
	'log_info_path': os.path.dirname(os.getcwd())+'/InterFaceTest/report/log/info.log',
	'log_debug_path': os.path.dirname(os.getcwd())+'/InterFaceTest/report/log/debug.log',
	'log_warn_path': os.path.dirname(os.getcwd())+'/InterFaceTest/report/log/warning.log',
	'log_error_path': os.path.dirname(os.getcwd())+'/InterFaceTest/report/log/error.log',
	'log_critical_path': os.path.dirname(os.getcwd())+'/InterFaceTest/report/log/critical.log'
}
