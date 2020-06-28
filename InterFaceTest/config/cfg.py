#-*- coding: utf-8 -*-
import os
import time
root_path = os.path.abspath(os.path.dirname(__file__)).split('InterFaceTestdemo')[0]
# 获取项目根路径
testCaseExcel_path = root_path+'InterFaceTestdemo\\InterFaceTest\\testcase\\testCase.xlsx'

report_path = root_path+'InterFaceTestdemo\\InterFaceTest\\report\\TestReport_{}.html'.format(str(time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())))
log_path = {
	'log_info_path': root_path+'InterFaceTestdemo\\InterFaceTest\\report\\info.log',
	'log_debug_path': root_path+'InterFaceTestdemo\\InterFaceTest\\report\\debug.log',
	'log_warn_path': root_path+'InterFaceTestdemo\\InterFaceTest\\report\\warning.log',
	'log_error_path': root_path+'InterFaceTestdemo\\InterFaceTest\\report\\error.log',
	'log_critical_path': root_path+'InterFaceTestdemo\\InterFaceTest\\report\\critical.log'
}
email = {
	'username': 'xxxxxx@163.com',   # 发件人账户
	'passwd': 'xxxxxxxx',           # 发件人密码（授权码）
	'recv': 'xxxx@163.com',         # 收件人
	'title': '主题',                 # 主题
	'content': '正文',               # 正文
	'mail_host': 'smtp.163.com',    # 邮箱服务器
	'port': 25,
	'file': None                    # 附件地址
}

if __name__ == "__main__":
	print(log_path['log_info_path'])
	print(testCaseExcel_path)
	root_path = os.path.abspath(os.path.dirname(__file__)).split('\\InterFaceTestdemo')[0]
	print(root_path)