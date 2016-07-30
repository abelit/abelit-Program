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
import sys
import datetime

# Import customize modules 
import __init__
# from sqlquery import SQLQuery
# from sqlquery import Tables
from database.db import Oracle
from core.texthandler import TextHandler
from logwrite import LogWrite
class DataSync:
    def sync_data(method,tablesrc,tabledst,ownersrc,ownerdst,condition):
        column_pk_src=Oracle.Tables().query_column(tablesrc,ownersrc)['column_pk']
        column_nm_src=Oracle.Tables().query_column(tablesrc,ownersrc)['column_nm']
        column_pk_dst=Oracle.Tables().query_column(tabledst,ownerdst)['column_pk']
        column_nm_dst=Oracle.Tables().query_column(tabledst,ownerdst)['column_nm']
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
        if column_nm_src==column_nm_dst:
            # If the table has the primary key
            if len(column_pk_src) and len(column_pk_dst) and column_pk_src==column_pk_dst:
                # Query the diffrence data between two table
                sql_diff_result=Oracle.SQLQuery().query_sql(TextHandler.format_text(sql_diff,column_pk_src[0],ownersrc+'.'+tablesrc,condition,ownerdst+'.'+tabledst,condition))
                if sql_diff_result:
                    sql_diff_result=sql_diff_result[0]
                    data_diff=Oracle.SQLQuery().query_sql(TextHandler.format_text(sql_diff,'*',ownersrc+'.'+tablesrc,condition,ownerdst+'.'+tabledst,condition))
                    sql_diff_str="("
                    for i in range(len(sql_diff_result)-1):
                        sql_diff_str=sql_diff_str+"'"+sql_diff_result[i]+"'"+","
                    sql_diff_str=sql_diff_str+sql_diff_result[len(sql_diff_result)-1]+")"
                    condition=condition+' '+'WHERE'+' '+column_pk_src[0]+' '+'IN'+' '+sql_diff_str
                    # Using merge sync data
                    if method=='merge':
                        sql_merge_col1=''
                        for row in range(1,len(column_nm_src)-1):
                            sql_merge_col1=sql_merge_col1+'dst'+'.'+column_nm_src[row]+'='+'src'+'.'+column_nm_src[row]+','
                        sql_merge_col1=sql_merge_col1+'dst'+'.'+column_nm_src[len(column_nm_src)-1]+'='+'src'+'.'+column_nm_src[len(column_nm_src)-1]
                        
                        sql_merge_col2=''
                        for row in range(len(column_nm_src)-1):
                            sql_merge_col2=sql_merge_col2+'src'+'.'+column_nm_src[row]+','
                        sql_merge_col2=sql_merge_col2+'src'+'.'+column_nm_src[len(column_nm_src)-1]
                        
                        sql_merge=TextHandler.format_text(sql_merge,ownerdst+'.'+tabledst,ownersrc+'.'+tablesrc,'dst'+'.'+column_pk_src[0],'src'+'.'+column_pk_src[0],sql_merge_col1,condition,sql_merge_col2)
                  
                        try:
                            # Call logwrite modules to write different data into log
                            LogWrite(logmessage=data_diff, loglevel='infoLogger').write_log()
                            # Call modules to excute sql
                            Oracle.SQLQuery().query_sql(sql_merge,isresult=False)
                            # Call logwrite modules to write log
                            LogWrite(logmessage=sql_merge, loglevel='infoLogger').write_log()
                        except cx_Oracle.DatabaseError:
                            LogWrite(logmessage="Sync data error", loglevel='errorLogger').write_log()
                        else:
                            LogWrite(logmessage="Sync data successfully between "+ownersrc+'.'+tablesrc+' and '+ownerdst+'.'+tabledst, loglevel='infoLogger').write_log()    
                    # Using minus,delete,insert sync data
                    elif method=='insert':
                        # Call logwrite modules to write different data into log
                        LogWrite(logmessage=data_diff, loglevel='infoLogger').write_log()
                        # Delete data
                        sql_sync_delete=TextHandler.format_text(sql_sync_delete,ownerdst+'.'+tabledst,column_pk_dst[0],column_pk_dst[0],ownersrc+'.'+tablesrc,condition,ownerdst+'.'+tabledst,condition)
                        # Insert data
                        sql_sync_insert=TextHandler.format_text(sql_sync_insert,ownerdst+'.'+tabledst,ownersrc+'.'+tablesrc,condition,ownerdst+'.'+tabledst,condition)
                        try:
                            Oracle.SQLQuery().query_sql(sql_sync_delete,isresult=False)
                            Oracle.SQLQuery().query_sql(sql_sync_insert,isresult=False)
                            LogWrite(logmessage='The sql to sync data: '+sql_sync_delete+sql_sync_insert, loglevel='infoLogger').write_log()
                        except cx_Oracle.DatabaseError:
                            LogWrite(logmessage="Sync data error", loglevel='errorLogger').write_log()
                        else:
                            LogWrite(logmessage="Sync data successfully between "+ownersrc+'.'+tablesrc+' and '+ownerdst+'.'+tabledst, loglevel='infoLogger').write_log()
                    else:
                        LogWrite(logmessage="Please input 'insert' or 'merge' to sync data,like syncdata(merge)", loglevel='errorLogger').write_log()
                else:
                    LogWrite(logmessage="No data need to syncthonize between "+ownersrc+'.'+tablesrc+' and '+ownerdst+'.'+tabledst, loglevel='warnLogger').write_log()
            else:
                LogWrite(logmessage="Empty list, no primary key on table "+ownersrc+'.'+tablesrc+' or '+ownersrc+'.'+tablesrc, loglevel='errorLogger'+' or there are diffrences on two tables').write_log()
      
# Call function to sync data
if __name__=='__main__':
    tablesrc='A_BM_XZQH'
    tabledst='A_BM_XZQH'
    ownersrc='GZGS_GY'
    ownerdst='GZGS_HZ'
    condition=""
    method='merge'
    DataSync.sync_data(method=method,tablesrc=tablesrc,tabledst=tabledst,ownersrc=ownersrc,ownerdst=ownerdst,condition=condition)