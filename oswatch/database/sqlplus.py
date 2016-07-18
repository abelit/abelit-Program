#!/usr/bin/python
#coding:utf-8

# Function:Synchronize data between two tables
# Description:
# Author:Abelit
# Email:ychenid@live.com
# Date:2016-07-07

import os
from subprocess import Popen, PIPE

sqlplus = Popen(["sqlplus", "-S", "sys/dba1d71f678513c02d0@gzgszxk_new1", "as", "sysdba"], stdout=PIPE, stdin=PIPE)
sqlplus.stdin.write("select sysdate from dual;"+os.linesep)
#sqlplus.stdin.write("select count(*) from all_objects;"+os.linesep)
#sqlplus.stdin.write("execute dbms_logmnr.add_logfile(LogFileName=>'+DATA/gzgszxk/onlinelog/group_3.391.913367235',Options=>dbms_logmnr.new);"+os.linesep)

out, err = sqlplus.communicate()
print(out)

