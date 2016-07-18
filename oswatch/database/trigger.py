#!/usr/bin/python
#coding:utf-8

# Function:Synchronize data between two tables
# Description:
# Usage:
    # Function gzgsdata
# Author:Abelit
# Email:ychenid@live.com
# Date:2016-07-06

import datetime
import logwrite
from sqlquery import SQLQuery as sqlquery
import column
class Trigger():
    """docstring for Trigger"""
    def __init__(self, arg):
        super(Trigger, self).__init__()
        self.arg = arg
        
    def create_datasync_trigger(trigger_name,tablesrc,tabledst,ownersrc,ownerdst):
        column_pk=column.query_column(tablesrc,ownersrc)['column_pk']
        column_nm=column.query_column(tablesrc,ownersrc)['column_nm']
        # Create trigger sql
        trigger_text='''
        create or replace trigger %s
        after insert or update or delete on %s
        for each row
        begin
        if deleting then
        dbms_output.put_line('deleting');
        delete from %s where %s;
        end if;
        if inserting then
        dbms_output.put_line('inserting');
        insert into %s
        values(%s);
        end if;
        if updating then
        dbms_output.put_line('updating');
        update %s set %s where %s;
        end if;
        end %s;
        '''
        if len(column_pk):
            str1=trigger_name
            str2=ownersrc+'.'+tablesrc
            str3=ownerdst+'.'+tabledst
            str4=column_pk[0]+'=:old.'+column_pk[0]
            str5=ownerdst+'.'+tabledst
            str6=''
            for row in range(0,len(column_nm)-1):
                str6=str6+':new.'+column_nm[row]+','
            str6=str6+':new.'+column_nm[len(column_nm)-1]

            str7=ownerdst+'.'+tabledst
            str8=''
            for row in range(0,len(column_nm)-1):
                str8=str8+column_nm[row]+'=:new.'+column_nm[row]+','
            str8=str8+column_nm[len(column_nm)-1]+'=:new.'+column_nm[len(column_nm)-1]

            str9=column_pk[0]+'=:old.'+column_pk[0]
            str10=trigger_name
            print(sqlquery.format_text(trigger_text,str1,str2,str3,str4,str5,str6,str7,str8,str9,str10))
            sqlquery.query_sql(sqlquery.format_text(trigger_text,str1,str2,str3,str4,str5,str6,str7,str8,str9,str10),isresult='false')
        else:
            print('No primary key on the table!')

Trigger.create_datasync_trigger('syncdata','A_BM_XZQH','A_BM_XZQH','GZGS_GY','GZGS_HZ')

