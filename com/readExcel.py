# -*- coding: utf-8 -*-

# *******************************************#
# project:HeyMylody
# fileName:readExcel
# author:Merlin
# dataTime:2020/12/12
# *******************************************#
import os
import xlrd
import configparser
from com.log import log, logger, BASE_DIR

config = configparser.ConfigParser()
config.read(f'{BASE_DIR}/config/config.ini', encoding='UTF-8')

Excelpath = os.path.join(BASE_DIR, config.get('path', 'Excelpath'))
sheetName = config.get('path', 'sheet')

table_values = ['_number', '_ame', '_host', '_path', '_method', '_type', '_data', '_assert']


@logger(__name__)
def getExcelTestCaseList():
    case_list = []
    log.info('Start Read Excel\n')
    table = xlrd.open_workbook(Excelpath, 'r').sheet_by_name(sheetName)

    for n in range(len(table.col_values(5, start_rowx=1))):
        _list = table.row_values(n + 1)
        case_dict = dict(zip(table_values, _list))
        case_list.append(case_dict)
        log.debug('{}'.format(case_dict))
    log.info('Read Excel End\n')
    return case_list


if __name__ == '__main__':
    case = getExcelTestCaseList()
    log.debug(case)
