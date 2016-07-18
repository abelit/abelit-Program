#!/usr/bin/python
#coding:utf-8

# Function:Synchronize data between two tables
# Description:
# Author:Abelit
# Email:ychenid@live.com
# Date:2016-07-07
from sqlquery import SQLQuery as sqlquery

def add_column():
	add_column='''
	alter table %s add %s
	'''

def query_column(tablename,owner):
	# Query primary key of the table
	column_pk='''
	select col.column_name  from all_constraints con,  all_cons_columns col where con.constraint_name = col.constraint_name and con.constraint_type='P' and col.table_name = '%s' and col.owner='%s' and con.owner=col.owner
	'''
	# Count the number of total columns of the table
	column_ct='''
	select count(*) from all_tab_columns where table_name ='%s' and owner='%s'
	'''
	# Query all columns of the table
	column_nm='''
	select column_name from all_tab_columns where table_name ='%s' and owner='%s'
	'''
	# Return result of formatting sql text
	return {
		'column_pk':sqlquery.query_sql(sqlquery.format_text(column_pk,tablename,owner)),
		'column_ct':sqlquery.query_sql(sqlquery.format_text(column_ct,tablename,owner)),
		'column_nm':sqlquery.query_sql(sqlquery.format_text(column_nm,tablename,owner))
	}

#print(query_column('A_BM_XZQH','GZGS_GY'))
