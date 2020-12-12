import logging.handlers
import logging.config
import os
import sys
import logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


class LogHandler(object):

    def __init__(self, log_name='log.log', dir='../report/', debug=True, log_level="INFO"):

        self.debug = debug
        self.log_name = log_name
        self.dir = dir
        self.log_level = log_level

    def create_logger(self):
        # logging的初步日志对象， 后面用来add, StreamHandler， FileHandler, 总是单例，加上name就是初始化对象

        self.logger = logging.getLogger(name=self.log_name)
        self.logger.setLevel(logging.DEBUG)  # 过滤该level以下的日志消息, 此设置会影响单个handler的设置，如果此级别高于handler则使用此级别

        # 日志输出格式
        fmt = logging.Formatter('%(asctime)s    %(levelname)s   %(filename)s   %(funcName)s %(lineno)d  %(message)s')
        # 日志级别
        lvl = eval("logging." + self.log_level)

        # 输出流的级别和格式保持和文件保持一致
        # 如果是测试模式，创建控制台输出流
        if self.debug:
            self.console = logging.StreamHandler()
            self.console.setLevel(lvl)
            self.console.setFormatter(fmt)
            self.logger.addHandler(self.console)
        file_handler = logging.FileHandler(self.log_name)
        # 在设置之前的日志模式上加入文件
        file_handler.setLevel(lvl)
        file_handler.setFormatter(fmt)
        self.logger.addHandler(file_handler)

        return self.logger


if __name__ == "__main__":
    # 在别的文件引入这个类， 然后用这个对象即可
    logger = LogHandler(log_name=r"../report/log.log", log_level="DEBUG").create_logger()
    logger.debug("video")
