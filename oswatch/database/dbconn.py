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
import config.config as dbconf


class DBConn:
    """docstring for ConnDB"""
    def __init__(self, arg):
        super(ConnDB, self).__init__()
        self.arg = arg
        
    #Connect to oracle
    def conn_oracle():
        if dbconf.oracle['username']=='sys':
            try:
                conn=cx_Oracle.connect(dbconf.oracle['username'],dbconf.oracle['password'],dbconf.oracle['db_host']+':'+dbconf.oracle['db_port']+'/'+dbconf.oracle['db_instance'],cx_Oracle.SYSDBA)
            except cx_Oracle.DatabaseError as cx_msg:
                print("[ERROR]\tFailed to connect to Database as sysdba.")
                print(cx_msg)
                conn.close()
                sys.exit()
        else:
            try:
                conn=cx_Oracle.connect(dbconf.oracle['username'],dbconf.oracle['password'],dbconf.oracle['db_host']+':'+dbconf.oracle['db_port']+'/'+dbconf.oracle['db_instance'])
            except cx_Oracle.DatabaseError as cx_msg:
                print("[ERROR]\tFailed to connect to Database as sysdba.")
                print(cx_msg)
                conn.close()
                sys.exit()
        return conn     

    #Connect to mysql
    def conn_mysql():
        pass
