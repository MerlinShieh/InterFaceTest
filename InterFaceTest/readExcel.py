#-*- coding: utf-8 -*-
import xlrd
from pprint import pprint

table_values = ["number", "name", "host", "model", "data"]
def getExcelTestCaseList():
    CASELIST = []
    table = xlrd.open_workbook("testCase.xlsx", "r").sheet_by_name("interface")
    for n in range(len(table.col_values(4, start_rowx=1))):
        '''
        单条用例所有参数 封装成list
        [1.0,'正常GET','http://hn216.api.yesapi.cn','GET','app_key=B2F70096FD3977B3F183DFD952F4446B&text=可以免费使用，基本上应用需要的数据都有接口提供&s=App.Scws.GetWords']
        每一条list都与table_values 合并为一个dict
        {1.0: 'number', '正常GET': 'name', 'http://hn216.api.yesapi.cn': 'host', 'GET': 'model', 'app_key=B2F70096FD3977B3F183DFD952F4446B&text=可以免费使用，基本上应用需要的数据都有接口提供&s=App.Scws.GetWords': 'data'}
        '''
        CaseList = table.row_values(n + 1)
        CaseDict = dict(zip(table_values, CaseList))
        CASELIST.append(CaseDict)
    return CASELIST
# if __name__=="__main__":
#     # 打开Excel
#     wb = xlrd.open_workbook("testCase.xlsx", "r")
#     # 打开其中一个sheet
#     table = wb.sheet_by_name("interface")
#     '''
#     rowx 就是某一列，由于我们第一列为编号存在数据，使用第1列 rowx=0
#     '''
#     col_len = len(table.col_values(4, start_rowx=1))
#     for n in range(col_len):
#         print(table.row_values(n + 1))
#     # 获取每一行的参数，返回一个list
if __name__ == "__main__":
    pprint(getExcelTestCaseList())