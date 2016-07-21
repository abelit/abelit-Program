# encoding:utf-8
import sys
import logging

import __init__
from config import dbconfig

class LogWrite:
    """docstring for LogWrite"""
    def __init__(self, arg):
        super(LogWrite, self).__init__()
        self.arg = arg
        
    def write_log(logdir=dbconfig.logpath['dblog'],message='a'):
        logger=logging.getLogger()
        handler=logging.FileHandler(logdir)
        logger.addHandler(handler)
        logger.setLevel(logging.NOTSET)
        logger.info(message)