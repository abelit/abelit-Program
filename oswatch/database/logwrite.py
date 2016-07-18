# encoding:utf-8
import sys
import logging

def writelog(logdir='',message=''):
	logger=logging.getLogger()
	handler=logging.FileHandler(logdir)
	logger.addHandler(handler)
	logger.setLevel(logging.NOTSET)
	logger.info(message)