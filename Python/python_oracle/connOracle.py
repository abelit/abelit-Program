#!/usr/bin/python
#coding:utf-8

#Function:Auto getting information about os
#Description:
#Author:Abelit
#Email:ychenid@live.com
#Date:2016-04-28

import cx_Oracle
#conn=cx_Oracle.connect('abelit','cy123','172.28.1.25:1521/gzgszxk')
#conn=cx_Oracle.connect('abelit/cy123@172.28.1.25:1521/gzgszxk')
username='abelit'
password='dba1d71f678513c02d0'
db_host='172.28.1.30'
db_port='1521'
db_instance='gzgszxk'
host=db_host+':'+db_port+'/'+db_instance
if username=='sys':
	conn=cx_Oracle.connect(username,password,host,cx_Oracle.SYSDBA)
else:
	conn=cx_Oracle.connect(username,password,host)
#conn=cx_Oracle.connect('sys','dba1d71f678513c02d0','172.28.1.30:1521/gzgszxk',cx_Oracle.SYSDBA)
#Get cursor
curs=conn.cursor()
# sql='''SELECT a.tablespace_name "表空间名", 
# total / (1024 * 1024 * 1024) "表空间大小(G)", 
# free / (1024 * 1024 * 1024) "表空间剩余大小(G)", 
# (total - free) / (1024 * 1024 * 1024) "表空间使用大小(G)", 
# round((total - free) / total, 4) * 100 "使用率 %" 
# FROM (SELECT tablespace_name, SUM(bytes) free 
# FROM dba_free_space 
# GROUP BY tablespace_name) a, 
# (SELECT tablespace_name, SUM(bytes) total 
# FROM dba_data_files 
# GROUP BY tablespace_name) b 
# WHERE a.tablespace_name = b.tablespace_name '''
sql='''
	select * from all_users
	'''
curs.execute(sql)
result=curs.fetchall()
list1=[]
#print(type(result))
for row in result:
	list1.append(row[0])

print('总共有%s个用户' % len(list1))
print(list1)
#Release resource
curs.close()
conn.close()
