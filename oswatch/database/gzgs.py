#!/usr/bin/python
#coding:utf-8

# Function:Synchronize data between two tables
# Description:
# Usage:
	# Function gzgsdata
# Author:Abelit
# Email:ychenid@live.com
# Date:2016-07-01

import syncdata

tablename=['A_BM_XZQH']
ownersrc=['GZGS_GY']
ownerdst=['GZGS_HZ']
condition=""
method='merge'

# gzgs syncdata
def gzgsdata(type='manual',method=method,tablename=tablename,ownersrc=ownersrc,ownerdst=ownerdst,condition=condition):
	def syncall():
		ownersrc=['GZGS_GY','GZGS_ZY','GZGS_BJ','GZGS_RHX','GZGS_LPS','GZGS_WLX','GZGS_TR','GZGS_QN','GZGS_QXN','GZGS_QDN','GZGS_AS','GZGS_GA','GZGS_SGS']
		tablename='''
		select table_name from all_tables where owner='%s'
		'''
		for i in ownersrc:
			tables_sql=syncdata.sqlformat(tablename,i)
			tablename=syncdata.sqlresult(tables_sql)
			for j in tablename:
				for k in ownerdst:
					syncdata.syncdata(method=method,tablename=j,ownersrc=i,ownerdst=k,condition=condition)
	def syncmanual():
		for i in ownersrc:
			for j in tablename:
				for k in ownerdst:
					syncdata.syncdata(method=method,tablename=j,ownersrc=i,ownerdst=k,condition=condition)

	result = {
	  'all': lambda: syncall(),
	  'manual': lambda:syncmanual()
	}[type]()



#gzgsdata(ownersrc=['GZGS_HZ'],ownerdst=['GZGS_GY','GZGS_ZY'])
gzgsdata(type='manual',method='merge',ownersrc=['GZGS_ZY'],ownerdst=['GZGS_GY'])

