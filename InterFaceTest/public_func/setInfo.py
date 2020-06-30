# -*- coding: utf-8 -*-
# *******************************************#
# project:InterFaceTestdemo
# fileName:set_log
# author:Merlin
# dataTime:2020/6/29-22:38
# *******************************************#
import time
import sys
from config.cfg import log_path
# 使用装饰器来获取函数名称

time = str(time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime()))

def write_log(message):
	with open(log_path, "a+") as f:
		f.write(time+'  '+str(message)+"\n")

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
			print(func.__name__)
			with open(log_path, "a+") as f:
				f.write(time + '  ' + str(func.__name__) + '   ' + str(msg) + "\n")
			print('现在结束装饰')
		return writeLog

	return run

if __name__=="__main__":

	@logInfo('测试日志')
	def test():
		print('我是被装饰的函数')
	# return num+1
	test()