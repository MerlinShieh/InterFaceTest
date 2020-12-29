
import configparser
import os
import time
from log import LogHandler
config = configparser.ConfigParser()
config.read('../config/config.ini', encoding='UTF-8')

try:
    # 创建已日期命名的文文件夹
    os.mkdir(r"../report/{}".format(str(time.strftime("%Y_%m_%d", time.localtime()))))
except FileExistsError:
    pass


COUNTRY = config.get('Country', 'country')

TestTime = str(time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()))
Log_path = r"../report/{}/TestReport_{}_{}.log".format(
    str(time.strftime('%Y_%m_%d', time.localtime())), COUNTRY, TestTime)
Report_path = r'../report/{}/TestReport_{}_{}.html'.format(
    str(time.strftime('%Y_%m_%d', time.localtime())), COUNTRY, TestTime)

# 创建logger
logger = LogHandler(log_name=Log_path,
                    log_level="DEBUG").create_logger()
reportHTML = Report_path

# 把日志地址和报告地址写入配置文件
config.set('path', 'Log_path', Log_path)
config.set('path', 'Report_path', reportHTML)

with open(r'../config/config.ini', 'w+') as f:
    config.write(f)
