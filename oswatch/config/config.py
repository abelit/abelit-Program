#!/usr/bin/python
#coding:utf-8

# Function:Synchronize data between two tables
# Description:
# Author:Abelit
# Email:ychenid@live.com
# Date:2016-07-11
import time

# Oracle configuration
oracle={
	'username':'sys',
	'password':'dba1d71f678513c02d0',
	'db_host':'172.28.1.221',
	'db_port':'1521',
	'db_instance':'gzgszxk'
}

# Configure log path
logpath={
	'logdir_trigger_error':"./log/"+'trigger-'+time.strftime('%Y-%m-%d',time.localtime(time.time()))+'-error.log',
	'logdir_trigger_history':"./log/"+'trigger-'+time.strftime('%Y-%m-%d',time.localtime(time.time()))+'-history.log',
	'logdir_syncdata_error':"./log/"+'syncdata-'+time.strftime('%Y-%m-%d',time.localtime(time.time()))+'-error.log',
	'logdir_syncdata_history':"./log/"+'syncdata-'+time.strftime('%Y-%m-%d',time.localtime(time.time()))+'-history.log'
}