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
    'username':'sys',
    'password':'dba1d71f678513c02d0',
    'host':'172.28.1.222',
    'port':'1521',
    'instance':'gzgszxk'
}

# Configure log path
logpath={
    'dblog':'../logs/'+'dblog.log',
}
