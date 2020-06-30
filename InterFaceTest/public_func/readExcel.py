# -*- coding: utf-8 -*-
# *******************************************#
# project:InterFaceTestdemo
# fileName:readExcel
# author:Merlin
# dataTime:2020/6/27-0:03
# *******************************************#
import xlrd
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
@public_func.setInfo.logInfo('列表获取')
def getExeclTestCaseList():
	Case = []
	table = xlrd.open_workbook(config.cfg.testCaseExcel_path, 'r').sheet_by_name('interface')

	for n in range(len(table.col_values(4, start_rowx=1))):
		CaseList = table.row_values(n + 1)
		public_func.setInfo.write_log(message="表格用例加载一条:{}".format(CaseList))
		CaseDict = dict(zip(table_values, CaseList))
		Case.append(CaseDict)
	return Case

if __name__=="__main__":
	pprint.pprint(getExeclTestCaseList())