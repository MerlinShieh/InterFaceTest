# -*- coding: utf-8 -*-
# *******************************************#
# project:InterFaceTestdemo
# fileName:log
# author:Merlin
# dataTime:2020/6/26-22:34
# *******************************************#
import logging
import config.cfg

def setLog(leavel, message, path=(config.cfg.log_path['log_info_path'])):
	logger = logging.getLogger(__name__)
	if str(leavel).upper() == "INFO":
		logger.setLevel(logging.INFO)
		handler_info = logging.FileHandler(config.cfg.log_path['log_info_path'])
		handler_info.setLevel(logging.INFO)
		formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s -%(funcName)s - %(lineno)d - %(message)s')
		handler_info.setFormatter(formatter)
		logger.addHandler(handler_info)
		logger.info(message)
	elif str(leavel).upper() == "DEBUG":
		logger.setLevel(logging.DEBUG)
		handler_debug = logging.FileHandler(config.cfg.log_path['log_debug_path'])
		handler_debug.setLevel(logging.DEBUG)
		formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s -%(funcName)s - %(lineno)d - %(message)s')
		handler_debug.setFormatter(formatter)
		logger.addHandler(handler_debug)
		logger.debug(message)
	elif str(leavel).upper() == ("WARN" or "WARNING"):
		logger.setLevel(logging.WARNING)
		handler_warn = logging.FileHandler(config.cfg.log_path['log_warn_path'])
		handler_warn.setLevel(logging.WARNING)
		formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s -%(funcName)s - %(lineno)d - %(message)s')
		handler_warn.setFormatter(formatter)
		logger.addHandler(handler_warn)
		logger.warning(message)
	elif str(leavel).upper() == "ERROR":
		logger.setLevel(logging.ERROR)
		handler_error = logging.FileHandler(config.cfg.log_path['log_error_path'])
		handler_error.setLevel(logging.ERROR)
		formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s -%(funcName)s - %(lineno)d - %(message)s')
		handler_error.setFormatter(formatter)
		logger.addHandler(handler_error)
		logger.error(message)
	elif str(leavel).upper() =="CRITICAL":
		logger.setLevel(logging.CRITICAL)
		handler_critical = logging.FileHandler(config.cfg.log_path['log_critical_path'])
		handler_critical.setLevel(logging.CRITICAL)
		formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s -%(funcName)s - %(lineno)d - %(message)s')
		handler_critical.setFormatter(formatter)
		logger.addHandler(handler_critical)
		logger.critical(message)
	else:
		return False
if __name__=="__main__":
	setLog(leavel='info', message="测试")