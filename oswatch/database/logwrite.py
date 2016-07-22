#!/usr/bin/python
# encoding:utf-8
# Function:Synchronize data between two tables
# Description:
# Author:Abelit
# Email:ychenid@live.com
# Date:2016-07-21
import sys
import os
import platform
import logging
import logging.config
import logging.handlers
import configparser

import __init__
from config import dbconfig


class PathGet(object):
    """docstring for PathGet"""
    def __init__(self, file=__init__.PROJECT_INFO['project_name']):
        super(PathGet, self).__init__()
        self.file = file
        
    def get_separator(self):
        if 'Windows' in platform.system():
            separator = '\\'
        else:
            separator = '/'
        return separator

    def get_path(self):
        os_path = os.getcwd()
        separator = self.get_separator()
        str = os_path
        str = str.split(separator)
        while len(str) > 0:
            spath = separator.join(str)+separator+self.file
            leng = len(str)
            if os.path.exists(spath):
                return spath
            str.remove(str[leng-1])
            
    def get_dir(self):
        return os.path.dirname(self.get_path())

class LogWrite:
    """docstring for LogWrite"""
    def __init__(self, logpath=PathGet().get_dir()+'/logs/dblog.log', loglevel='debugLogger', logmessage='', logconf=PathGet().get_dir()+'/config/logging.conf'):
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
        cf.set("handler_rotatingHandler","args",'('+"'"+self.logpath+"'"+','+"'"+'a'+"'"+',10*1024*1024, 5'+')')
        fp=open(self.logconf,'w')
        cf.write(fp)
        fp.close()

    def write_log(self):
        if os.path.isfile(self.logconf):
            self.config_log()
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
                datefmt='',
                filename=self.logpath,
                filemode='a'
                )
            # Log Rollback
            logging.handlers.RotatingFileHandler(self.logpath, maxBytes=10*1024*1024,backupCount=5)
            
            # Output log to screen
            console = logging.StreamHandler()
            console.setLevel(logging.DEBUG)
            formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
            console.setFormatter(formatter)
            logging.getLogger('').addHandler(console)

            result = {
                'debugLogger': lambda:logging.debug(self.logmessage),
                'infoLogger': lambda:logging.info(self.logmessage),
                'errorLogger': lambda:logging.error(self.logmessage) 
            }[self.loglevel]()  

if __name__=='__main__':
    #LogWrite(logpath=PathGet('__oswatch__.py').get_dir()+'/logs/dblog.log',logmessage='This is a test message',logconf=PathGet('__oswatch__.py').get_dir()+'/config/logging.conf').write_log()
    LogWrite(logmessage="This is a info message", loglevel='infoLogger').write_log()