# -*- coding: utf-8 -*-
# *******************************************#
# project:InterFaceTestdemo
# fileName:set_log
# author:Merlin
# dataTime:2020/6/29-22:38
# *******************************************#
from  config.cfg import log_path
def write_log(message):
	with open(log_path, "a+") as f:
		f.write(message+"\n")