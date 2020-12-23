# -*- coding: utf-8 -*-

# *******************************************#
# project:HeyMylody
# fileName:readExcel
# author:Merlin
# dataTime:2020/12/12
# *******************************************#
import json

import xlrd
import sign

import configparser
config = configparser.ConfigParser()
config.read('../config/config.ini', encoding='UTF-8')

Excelpath = config.get('path', 'Excelpath')
sheetName = config.get('Country', 'country')

table_values = ['number', 'name', 'host', 'model', 'data', 'result']

def getExcelTestCaserList():
    Case = []
    table = xlrd.open_workbook('{}/{}'.format('../..', Excelpath), 'r').sheet_by_name(sheetName)

    for n in range(len(table.col_values(5, start_rowx=1))):
        CaseList = table.row_values(n + 1)
        CaseDict = dict(zip(table_values, CaseList))
        Case.append(CaseDict)
    return Case

if __name__=='__main__':
    case = getExcelTestCaserList()
    print(case[0]['data'])
    message = json.loads(case[0]['data'])
    print(sign.getSign(message))

