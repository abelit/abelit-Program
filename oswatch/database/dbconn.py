#!/usr/bin/python
#coding:utf-8

#Function:Auto getting information about os
#Description:
#Author:Abelit
#Email:ychenid@live.com
#Date:2016-04-28

import cx_Oracle
import config.dbconf as dbconf

#Connect to oracle
def conn_oracle():
	if dbconf.oracle['username']=='sys':
		conn=cx_Oracle.connect(dbconf.oracle['username'],dbconf.oracle['password'],dbconf.oracle['db_host']+':'+dbconf.oracle['db_port']+'/'+dbconf.oracle['db_instance'],cx_Oracle.SYSDBA)
	else:
		conn=cx_Oracle.connect(dbconf.oracle['username'],dbconf.oracle['password'],dbconf.oracle['db_host']+':'+dbconf.oracle['db_port']+'/'+dbconf.oracle['db_instance'])
	return conn		