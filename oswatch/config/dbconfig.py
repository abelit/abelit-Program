#!/usr/bin/python
#coding:utf-8

# Function:Synchronize data between two tables
# Description:
# Author:Abelit
# Email:ychenid@live.com
# Date:2016-07-11
import time
import getpass
import os
        
# username = raw_input("Enter Your Username: ")
        # password = getpass.getpass()
        # db_host = raw_input("Enter Your Hostname: ")
        # db_port = raw_input("Enter Your Database Port: ")
        # db_instance = raw_input("Enter Your Database Instance: ")
        
# Oracle configuration
oracle={
    #Oracle DB configuration
    'username':'sys',
    'password':'dba1d71f678513c02d0',
    'host':'172.28.1.222',
    'port':'1521',
    'instance':'gzgszxk',
    #Oracle env variable
    'ORACLE_BASE':'/u01/app/oracle',
    'ORACLE_HOME':'/u01/app/oracle/product/11.2.0/db_1',
    'ORACLE_SID':'gzgszxk2',
    'NLS_DATE_FORMAT':'yyyy-mm-dd HH24:MI:SS',
    'NLS_LANG':'AMERICAN_AMERICA.ZHS16GBK',
    # Oracle backup info
    'BACKUP_DIR':'/u01/app/oracle/backup'
}

# Configure log path
logpath={
    'dblog':'../logs/'+'dblog.log',
}
