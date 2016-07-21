#!/usr/bin/python
#coding:utf-8

# Function:Synchronize data between two tables
# Description:
# Usage:
    # Function gzgsdata
# Author:Abelit
# Email:ychenid@live.com
# Date:2016-07-01

import __init__
from database.datasync import DataSync as datasync
from database.sqlquery import SQLQuery as sqlquery
from database.columnquery import ColumnQuery as columnquery

# Configuration
tablesrc=['A_BM_XZQH','A_QYZT']
tabledst=['A_BM_XZQH','A_QYMC']
ownersrc=['GZGS_GY']
ownerdst=['GZGS_HZ']
condition=""
method='merge'

class GZGS:
    """docstring for GZGS"""
    def __init__(self, arg):
        super(GZGS, self).__init__()
        self.arg = arg
        
    def gzgs_data(plan='manual',method=method,tablesrc=tablesrc,tabledst=tabledst,ownersrc=ownersrc,ownerdst=ownerdst,condition=condition):
        if plan=='all':
            ownersrc=['GZGS_GY','GZGS_ZY','GZGS_BJ','GZGS_RHX','GZGS_LPS','GZGS_WLX','GZGS_TR','GZGS_QN','GZGS_QXN','GZGS_QDN','GZGS_AS','GZGS_GA','GZGS_SGS']
            ownerdst=['GZGS_HZ']
            tablename='''
            select table_name from all_tables where owner='%s'
            '''
        for i in ownersrc:
            if plan=='all':
                tablesrc=sqlquery.query_sql(sqlquery.format_text(tablename,i))
            for j in tablesrc:
                for k in ownerdst:
                    if plan=='all':
                        tabledst=sqlquery.query_sql(sqlquery.format_text(tablename,k))
                    for m in tabledst:
                        if columnquery.query_column(m,k)['column_nm']==columnquery.query_column(j,i)['column_nm']:
                            datasync.sync_data(method=method,tablesrc=j,tabledst=m,ownersrc=i,ownerdst=k,condition=condition)
if __name__=='__main__':
    GZGS.gzgs_data()
