# -*- coding: utf-8 -*-

import os
import sys

import logbook
from logbook.more import ColorizedStderrHandler
from functools import wraps

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(BASE_DIR)
print(BASE_DIR)

check_path = '.'
LOG_DIR = os.path.join(BASE_DIR, 'log')
file_stream = False
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)
    print(LOG_DIR, '路径已存在')
    file_stream = True


def get_logger(name='interface_case_run', level=''):
    """ get logger Factory function """
    logbook.set_datetime_format('local')
    ColorizedStderrHandler(bubble=False, level=level).push_thread()
    logbook.TimedRotatingFileHandler(
        os.path.join(LOG_DIR, '%s.log' % name),
        date_format='%Y_%m_%d_%H', bubble=True, encoding='utf-8').push_thread()
    return logbook.Logger(name)


log = get_logger(level='DEBUG')


def logger(param):
    """ fcuntion from logger meta """

    def wrap(function):
        """ logger wrapper """

        @wraps(function)
        def _wrap(*args, **kwargs):
            """ wrap tool """
            log.info("当前模块 {}".format(param))
            log.info("全部args参数参数信息 , {}".format(str(args)))
            log.info("全部kwargs参数信息 , {}".format(str(kwargs)))
            result = function(*args, **kwargs)
            log.debug("当前函数执行结果 , {}".format(result))
            return result

        return _wrap

    return wrap


if __name__ == "__main__":
    # 在别的文件引入这个类， 然后用这个对象即可
    log.debug("1231231231sdsadasd")

    log.info(log.name)
