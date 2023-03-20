
### 本次测试采用的是本地flask服务,如果有实际测试项目,可以更改Excel里面的内容,如果想学习又没有接口,可以fork我这个项目
https://github.com/MerlinShieh/flask.git
##### 直接安装运行python app.py就行

### 目录说明
- com：
  - HTMLTestRunner.py(已废弃), 生成测试报告,现在使用XTestRunner
  - httpApi.py 对requests的封装
  - log.py 对日志的封装,用的logbook
  - readExcel.py 对excel表格读取的封装
  - sign.py 对签名方法的封装
- log
  - interface_case_run.log 日志文件保存位置
- report
  - 2023-03-22 测试报告的保存位置
    - interface_case_run.html
- testcase：用来存放接口的表格测试用例
- testMain：主函数
- README.md
- requirements.txt