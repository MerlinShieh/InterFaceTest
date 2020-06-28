## 框架结构
* InterFaceTest
	* config
		* cfg.py
	* public_func
		* HTMLTestRunner.py
		* log.py
		* readExcel.py
		* sendEmail.py
		* useApi.py
	* report
		* log
		* TestReport_2020_06_27_08_30_41.html
	* testcase
		* testcase.xlsx
* testMain.py

### 目录说明
- config：cfg.py保存各种文件路径配置，比如测试报告路径和info_log路径等
- public_func：包含各种公共函数，比如日志log.py、发送邮件sendEmail.py、读取表格readExcel.py和发送网络请求useApi.log，HTMLTestRunner是网上公开的文件，略作修改后用于Python3
- report：存放测试报告和log日志的
- testcase：用来存放接口的表格测试用例
- testMain：主函数