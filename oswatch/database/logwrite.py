#!/usr/bin/python
# encoding:utf-8
# Function:Synchronize data between two tables
# Description:
# Author:Abelit
# Email:ychenid@live.com
# Date:2016-07-21
import sys
import os
import logging
import logging.config
import logging.handlers
import configparser

import __init__
from config import dbconfig

class LogWrite:
    """docstring for LogWrite"""
    def __init__(self, logpath='', loglevel='debugLogger', logmessage='', logconf=''):
        super(LogWrite, self).__init__()
        self.logpath=logpath
        self.loglevel=loglevel
        self.logconf=logconf
        self.logmessage=logmessage

    def config_log(self):
        #Change logconf
        cf=configparser.ConfigParser()
        cf.read(self.logconf)
        cf.set("handler_fileHandler","args",'('+"'"+self.logpath+"'"+','+"'"+'a'+"'"+')')
        fp=open(self.logconf,'w')
        cf.write(fp)
        fp.close()

    def write_log(self):
        if os.path.isfile(self.logconf):
            # Read logging configuration
            logging.config.fileConfig(self.logconf)
            # Get logger name
            logger=logging.getLogger(self.loglevel)
            # Call lambda function to do switch statement
            result = {
                'debugLogger': lambda:logger.debug(self.logmessage),
                'infoLogger': lambda: logger.info(self.logmessage),
                'errorLogger': lambda:  logger.error(self.logmessage)
            }[self.loglevel]()  
        else:
            # Configure logging parameters
            logging.basicConfig(
                level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S',
                filename=self.logpath,
                filemode='a'
                )

            result = {
                'debugLogger': lambda:logging.debug(self.logmessage),
                'infoLogger': lambda:logging.info(self.logmessage),
                'errorLogger': lambda:logging.error(self.logmessage) 
            }[self.loglevel]()  

if __name__=='__main__':
    LogWrite(logpath='../logs/dblog.log',logmessage='This is a test message',logconf='../config/logging.conf').config_log()
    LogWrite(logpath='../logs/dblog.log',logmessage='This is a test message',logconf='../config/logging.conf').write_log()
