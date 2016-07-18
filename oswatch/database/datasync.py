#!/usr/bin/python
#coding:utf-8

# Function:Synchronize data between two tables
# Description:
# Author:Abelit
# Email:ychenid@live.com
# Date:2016-06-30
import cx_Oracle
import re
import time
import datetime
import logwrite
import column
import coredef

# Define default variable
tablesrc='A_BM_XZQH'
tabledst='A_BM_XZQH'
ownerdst='GZGS_HZ'
ownersrc='GZGS_GY'
condition=""
method='merge'

def sync_data(method=method,tablesrc=tablesrc,tabledst=tabledst,ownersrc=ownersrc,ownerdst=ownerdst,condition=condition):
	column_pk=column.query_column(tablesrc,ownersrc)['column_pk']
	column_nm=column.query_column(tablesrc,ownersrc)['column_nm']
	# Using merge method to synchorize data
	sql_merge='''
	MERGE INTO %s dst  USING %s src ON ( %s = %s )
	WHEN MATCHED THEN
	UPDATE SET %s %s
	WHEN NOT MATCHED THEN
	INSERT VALUES (%s)
	'''
	sql_diff='''
	select %s from (select * from %s %s minus select * from %s %s)
	'''
	sql_sync_delete='''
	delete from %s where %s in (select %s from (select * from %s %s minus select * from %s %s))
	'''
	sql_sync_insert='''
	insert into %s (select * from %s %s minus select * from %s %s)
	'''
	if len(column_pk):
		sql_diff_result=coredef.execute_sql(coredef.format_text(sql_diff,column_pk[0],ownersrc+'.'+tablesrc,condition,ownerdst+'.'+tabledst,condition))
		
		if sql_diff_result:
			# using merge sync data
			sql_diff_str="("
			for i in range(len(sql_diff_result)-1):
				sql_diff_str=sql_diff_str+"'"+sql_diff_result[i]+"'"+","
			sql_diff_str=sql_diff_str+sql_diff_result[len(sql_diff_result)-1]+")"
			condition=condition+' '+'WHERE'+' '+column_pk[0]+' '+'IN'+' '+sql_diff_str
			if method=='merge':
				if len(column_pk):
					sql_merge_col1=''
					for row in range(1,len(column_nm)-1):
						sql_merge_col1=sql_merge_col1+'dst'+'.'+column_nm[row]+'='+'src'+'.'+column_nm[row]+','
					sql_merge_col1=sql_merge_col1+'dst'+'.'+column_nm[len(column_nm)-1]+'='+'src'+'.'+column_nm[len(column_nm)-1]
					sql_merge_col2=''
					for row in range(len(column_nm)-1):
						sql_merge_col2=sql_merge_col2+'src'+'.'+column_nm[row]+','
					sql_merge_col2=sql_merge_col2+'src'+'.'+column_nm[len(column_nm)-1]
					
					sql_merge=coredef.format_text(sql_merge,ownerdst+'.'+tabledst,ownersrc+'.'+tablesrc,'dst'+'.'+column_pk[0],'src'+'.'+column_pk[0],sql_merge_col1,condition,sql_merge_col2)
				else:
					print("empty list, no primary key on the table")
				try:
					# coredef.execute_sql(sql_merge,isresult='false')
					# coredef.execute_sql('commit',isresult='false')
					coredef.execute_sql(sql_merge,isresult='false')
					print(sql_merge)
				except cx_Oracle.DatabaseError:
					print("Sync data error!")
				else:
					print("Sync data successfully!")	
			elif method=='insert':
				# using minus,delete,insert sync data
				if len(column_pk):
					sql_sync_delete=coredef.format_text(sql_sync_delete,ownerdst+'.'+tabledst,column_pk[0],column_pk[0],ownersrc+'.'+tablesrc,condition,ownerdst+'.'+tabledst,condition)
					sql_sync_insert=coredef.format_text(sql_sync_insert,ownerdst+'.'+tabledst,ownersrc+'.'+tablesrc,condition,ownerdst+'.'+tabledst,condition)
				else:
					print("empty list, no primary key on the table")

				print('The sql to sync data: '+'\n'+sql_sync_delete+'\n'+sql_sync_insert)
				try:
					coredef.execute_sql(sql_sync_delete,isresult='false')
					coredef.execute_sql(sql_sync_insert,isresult='false')
				except cx_Oracle.DatabaseError:
					print("Sync data error!")
				else:
					print("Sync data successfully!")
			else:
				print("Please input 'insert' or 'merge' to sync data,like syncdata(merge)")
		# Release resource
		else:
			print('no data need to syncthonize')
	else:
		print("empty list, no primary key on the table")



