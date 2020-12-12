# -*- coding: utf-8 -*-

# *******************************************#
# project:HeyMylody
# fileName:readExcel
# author:Merlin
# dataTime:2020/12/12
# *******************************************#

import xlrd
Excelpath=None
sheetName=None

table_values = ['number', 'name', 'host', 'model', 'data', 'result']

def getExcelTestCaserList():
    Case = []
    table = xlrd.open_workbook(Excelpath, 'r').sheet_by_name(sheetName)

    for n in range(len(table.col_values(5, start_rowx=1))):
        CaseList = table.row_values(n + 1)
        CaseDict = dict(zip(table_values, CaseList))
        Case.append(CaseDict)
    return CaseDict