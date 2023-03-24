# import allure
import os

import xlrd
import yaml
from com import BASE_DIR


def readExcel(*args):
    """
    param args: excel_path, sheet_name
    return: list [{'_number': '', '': '', ... }, {}]
    """
    case_list = []
    table = xlrd.open_workbook(args[0], 'r').sheet_by_name(args[1])
    table_values = ['_number', '_ame', '_host', '_path', '_method', '_type', '_data', '_assert', '_isSkip']
    for n in range(len(table.col_values(5, start_rowx=1))):
        _list = table.row_values(n + 1)
        case_dict = dict(zip(table_values, _list))
        case_list.append(case_dict)
    return case_list


def readYaml(*args):
    """
    param args:
    :return:
    """
    with open(args[0], 'r', encoding='utf-8') as fp:
        yaml_f = yaml.safe_load(fp)
    return yaml_f


if __name__ == '__main__':
    f_path = os.path.join(BASE_DIR, 'testCase', 'test_0001_register', 'test_register.yaml')
    print(readYaml(f_path))
