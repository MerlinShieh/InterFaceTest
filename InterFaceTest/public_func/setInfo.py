# -*- coding: utf-8 -*-
# *******************************************#
# project:InterFaceTestdemo
# fileName:set_log
# author:Merlin
# dataTime:2020/6/29-22:38
# *******************************************#

import sys
import os
import time
BASE_DIR =os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #当前程序上上一级目录，这里为InterFaceTest
sys.path.append(BASE_DIR)
from config.cfg import log_path
# 使用装饰器来获取函数名称



def write_log(modle=None, path=log_path,*args, **kwargs):
	with open(path, "a+") as f:
		nowtime = str(time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime()))
		f.write(nowtime + '      ' + str(modle) + '      ' + str(args) + '      ' + str(kwargs) + "\n\n")

# def logInfo(main, message):
# 	def run(*argv):
# 		print(main.__name__)
# 		write_log(message=message)
# 		if argv:
# 			ret = main(*argv)
# 		else:
# 			ret = main()
# 		return ret
# 	return run
#
def logInfo(msg):  # 工厂函数，用来接受@get_parameter('index.html/')的'index.html/'
	def run(func):
		def writeLog():
			func()
			with open(log_path, "a+") as f:
				f.write(time + '  ' + str(func.__name__) + '   ' + str(msg) + "\n")
		return writeLog

	return run
