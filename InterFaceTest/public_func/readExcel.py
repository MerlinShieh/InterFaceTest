# -*- coding: utf-8 -*-
# *******************************************#
# project:InterFaceTestdemo
# fileName:readExcel
# author:Merlin
# dataTime:2020/6/27-0:03
# *******************************************#
import xlrd
import sys
import os
BASE_DIR =os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #当前程序上上一级目录，这里为InterFaceTest
sys.path.append(BASE_DIR)
import config.cfg
import pprint
import public_func.setInfo
import os

'''
读取Excel表格里面的接口用例数据，以单条用例所有参数 封装成list
	[1.0,'正常GET','http://hn216.api.yesapi.cn','GET','app_key=B2F70096FD3977B3F183DFD952F4446B&text=可以免费使用，基本上应用需要的数据都有接口提供&s=App.Scws.GetWords']
每一条list都与table_values 合并为一个dict
	{1.0: 'number', '正常GET': 'name', 'http://hn216.api.yesapi.cn': 'host', 'GET': 'model', 'app_key=B2F70096FD3977B3F183DFD952F4446B&text=可以免费使用，基本上应用需要的数据都有接口提供&s=App.Scws.GetWords': 'data'}
'''

table_values = ["number", "name", "host", "model", "data"]

def getExeclTestCaseList():
	funcName = sys._getframe().f_code.co_name
	Case = []
	table = xlrd.open_workbook(config.cfg.testCaseExcel_path, 'r').sheet_by_name('interface')
	for n in range(len(table.col_values(4, start_rowx=1))):
		CaseList = table.row_values(n + 1)
		# print(CaseList[4])
		public_func.setInfo.write_log(modle=funcName, message="加载一条用例:{}".format(CaseList))
		CaseDict = dict(zip(table_values, CaseList))
		Case.append(CaseDict)
	return Case

if __name__=="__main__":
	getExeclTestCaseList()
