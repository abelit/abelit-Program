#!/usr/bin/python
#coding:utf-8

#Function:Auto getting information about os
#Description:
#Author:Abelit
#Email:ychenid@live.com
#Date:2016-04-28

import cx_Oracle
import sys

import __init__
from config import dbconfig
# import configparser

# # Read variable from database configuration
# cf=configparser.ConfigParser()
# cf.read('../config/database.conf')

# username = cf.get("oracle","username")
# password = cf.get("oracle","password")
# host = cf.get("oracle","host")
# port = cf.getint("oracle","port")
# instance = cf.get("oracle","instance")
username = dbconfig.oracle['username']
password = dbconfig.oracle['password']
host = dbconfig.oracle['host']
port = dbconfig.oracle['port']
instance = dbconfig.oracle['instance']

class DBConn:

    """docstring for ConnDB"""
    def __init__(self, arg):
        super(ConnDB, self).__init__()
        self.arg = arg
        
    #Connect to oracle
    def conn_oracle():
        if username=='sys':
            try:
                conn=cx_Oracle.connect(username,password,host+':'+str(port)+'/'+instance,cx_Oracle.SYSDBA)
            except cx_Oracle.DatabaseError as cx_msg:
                print("[ERROR]\tFailed to connect to Database as sysdba.")
                print(cx_msg)
                conn.close()
                sys.exit()
        else:
            try:
                conn=cx_Oracle.connect(username,password,host+':'+str(port)+'/'+instance)
            except cx_Oracle.DatabaseError as cx_msg:
                print("[ERROR]\tFailed to connect to Database as sysdba.")
                print(cx_msg)
                conn.close()
                sys.exit()
        return conn     

    #Connect to mysql
    def conn_mysql():
        pass
