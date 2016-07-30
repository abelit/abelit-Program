import threading
import os
import datetime

# Import customize modules
import __init__
from dbconnect import DBConnect
from core.texthandler import TextHandler
from logwrite import LogWrite
from config import dbconfig

class DB(object):      
    # Define function format_sql to replace the string for new sqltext
    pass

class Oracle(DB):
    """docstring for Oracle"""
    class SQLQuery(object):
        """docstring for SQLQuery"""
        # def __init__(self, sql):
        #     super(SQLQuery, self).__init__()
        #     self.sql = sql
            
        # Get cursor
        def query_sql(self,sql,params='',isresult=True):
            # Connect to oracle
            conn=DBConnect.conn_oracle()
            # Declare cursor
            curs=conn.cursor()
            curs.execute(sql,params)
            if isresult:
                result=curs.fetchall()
                return result
            curs.execute('commit')
            # Release resource
            curs.close()
            conn.close()
            
    class Users(SQLQuery):
        """docstring for Users"""
        def query_user(self):
            sql='''
            select * from all_users  where username like :username
            '''
            return self.query_sql(sql,{'username':'GZGS%'})
            
    class Tables(SQLQuery):
        """docstring for Tables"""
        # def __init__(self, arg):
        #     super(Tables, self).__init__()
        #     self.arg = arg
        def query_column(self,tablename,owner):
            # Query primary key of the table
            sql_pk='''
            select col.column_name  from all_constraints con,  all_cons_columns col where con.constraint_name = col.constraint_name and con.constraint_type='P' and col.table_name = :table_name and col.owner = :owner and con.owner=col.owner
            '''
            # Query all columns of the table
            sql_nm='''
            select column_name from all_tab_columns where table_name = :table_name and owner = :owner
            '''
            # Return result of formatting sql text
            return {
                'column_pk':[row[0] for row in self.query_sql(sql_pk,{'table_name':tablename,'owner':owner})],
                'column_nm':[row[0] for row in self.query_sql(sql_nm,{'table_name':tablename,'owner':owner})]
            }

    class Tablespaces(object):
        """docstring for Tablespaces"""
        def __init__(self, arg):
            super(Tablespaces, self).__init__()
            self.arg = arg

        def query_tablespace():
            pass
            
        def create_tablespace():
            pass

        def set_tablespace():
            pass

        def drop_tablespace():
            pass

    class Datafiles(object):
        """docstring for Datafiles"""
        def __init__(self, arg):
            super(Datafiles, self).__init__()
            self.arg = arg

        def query_datafile():
            pass

        def create_datafile():
            pass

        def set_datafile():
            pass
            
        def drop_datafile():
            pass

    class Onlinelogs(object):
        """docstring for Onlinelogs"""
        def __init__(self, arg):
            super(Onlinelogs, self).__init__()
            self.arg = arg

        def query_onlinelog():
            pass

        def add_onlinelog():
            pass

        def delete_onlinelog():
            pass

        def set_onlinelog():
            pass
            
    class Archivelogs(object):
        """docstring for Archivelogs"""
        def __init__(self, arg):
            super(Archivelogs, self).__init__()
            self.arg = arg
            

    class Sessions(SQLQuery):
        """docstring for Sessions"""
        def query_session(self):
            sql='''
                select * from v$session where status=:status
                '''
            params={'status':'ACTIVE'}
            #return [(row[1],row[2]) for row in self.query_sql(sql,params)]
            return {
                'session_counts':len(self.query_sql(sql,params)),
                'session_sid_serial':[(row[1],row[2]) for row in self.query_sql(sql,params)]
            }

        def close_session():
            pass

            

    class Locks(object):
        """docstring for Locks"""
        def __init__(self, arg):
            super(Locks, self).__init__()
            self.arg = arg
        
        def query_lock():
            pass

        def release_lock():
            pass
        

    class DataRecovery(SQLQuery):
        """docstring for DataRecovery"""
        # def __init__(self, arg):
        #     super(DataRecovery, self).__init__()
        #     self.arg = arg
        script_dir=__init__.PathGet(__init__.PROJECT_INFO['project_name']).get_dir()+'/scripts'
        
        action='exp'

        from_users=[]
        from_tables=[]
        from_tablespaces=[]

        to_users=[]
        to_tables=[]
        to_tablespaces=[]
        
        #Parameter for exp
        exp_user='user/password'
        exp_dir=dbconfig.oracle['BACKUP_DIR']
        exp_type='byuser'
        exp_parameter=''
        #Parameter for imp
        imp_user='user/password'
        imp_dir=dbconfig.oracle['BACKUP_DIR']
        imp_type='byuser'
        imp_parameter=''
        # Parameter for expdp
        expdp_user='user/password'
        expdp_dir='BACKUP'
        expdp_type='byuser'
        expdp_parameter=''
        # Parameter for impdp
        impdp_user='user/password'
        impdp_dir='BACKUP'
        impdp_type='byuser'
        impdp_parameter=''

        def query_scn(self):
            sql='''select dbms_flashback.get_system_change_number, 
            SCN_TO_TIMESTAMP(dbms_flashback.get_system_change_number) from dual'''
            return [(row[0],row[1]) for row in self.query_sql(sql)]

        def exp(self):
            if self.exp_type.lower() == 'byuser':
                for i in self.from_users:
                    text = "exp %s owner=%s file=%s log=%s %s"
                    cmd = TextHandler.format_text(
                        text, self.exp_user, i, self.exp_dir + '/' + i + '_exp_' +
                        datetime.datetime.now().strftime('%Y%m%d') + '.dmp',
                        self.exp_dir + '/' + i + '_exp_' +
                        datetime.datetime.now().strftime('%Y%m%d') + '.log',self.exp_parameter)
                    LogWrite(logmessage=cmd, loglevel='infoLogger').write_log()
            elif self.exp_type.lower() == 'bytable':
                for i in self.from_users:
                    text = "exp %s table=%s file=%s log=%s %s"
                    cmd = TextHandler.format_text(
                        text, self.exp_user, i, self.exp_dir + '/' + i + '_exp_' +
                        datetime.datetime.now().strftime('%Y%m%d') + '.dmp',
                        self.exp_dir + '/' + i + '_exp_' +
                        datetime.datetime.now().strftime('%Y%m%d') + '.log',self.exp_parameter)
                    LogWrite(logmessage=cmd, loglevel='infoLogger').write_log()
            elif self.exp_type.lower() == 'byfull':
                text = "exp %s full=y file=%s log=%s %s"
                cmd = TextHandler.format_text(
                    expt_ext, self.exp_user,
                    self.exp_dir + '/' + dbconfig.oracle['instance'] + '_exp_' +
                    datetime.datetime.now().strftime('%Y%m%d') + '.dmp',
                    self.exp_dir + '/' + dbconfig.oracle['instance'] + '_exp_' +
                    datetime.datetime.now().strftime('%Y%m%d') + '.log',self.exp_parameter)
                LogWrite(logmessage=cmd, loglevel='infoLogger').write_log()
            else:
                LogWrite(
                    logmessage="Please asign the type of backup data. Like byuser|bytable|byfull.",
                    loglevel='warnLogger').write_log()
        def expdp(self):
            if self.expdp_type.lower() == 'byuser':
                for i in self.from_users:
                    text = "expdp %s schemas=%s directory=%s dumpfile=%s logfile=%s  parallel=%s cluster=n REUSE_DUMPFILES=Y"
                    cmd = TextHandler.format_text(
                        expdp_text, backup_user, i, backup_name, i + '_expdp_' +
                        datetime.datetime.now().strftime('%Y%m%d') + '.dmp',
                        i + '_expdp_' + datetime.datetime.now().strftime('%Y%m%d') +
                        '.log', parallels)
                    LogWrite(logmessage=expdpcmd, loglevel='infoLogger').write_log()
            elif backup_type.lower() == 'bytable':
                for i in table_src:
                    text = "expdp %s tables=%s directory=%s dumpfile=%s logfile=%s  parallel=%s cluster=n REUSE_DUMPFILES=Y"
                    cmd = TextHandler.format_text(
                        expdptext, backup_user, i, backup_name, i + '_expdp_' +
                        datetime.datetime.now().strftime('%Y%m%d') + '.dmp',
                        i + '_expdp_' + datetime.datetime.now().strftime('%Y%m%d') +
                        '.log', parallels)
                    LogWrite(logmessage=expdpcmd, loglevel='infoLogger').write_log()
            elif backup_type.lower() == 'bytablespace':
               for i in tablespace_src:
                   expdptext = "expdp %s tablespaces=%s directory=%s dumpfile=%s logfile=%s  parallel=%s cluster=n REUSE_DUMPFILES=Y"
                   expdpcmd = TextHandler.format_text(
                       expdptext, backup_user, i, backup_name, i + '_expdp_' +
                       datetime.datetime.now().strftime('%Y%m%d') + '.dmp',
                       i + '_expdp_' + datetime.datetime.now().strftime('%Y%m%d') +
                       '.log', parallels)
                   LogWrite(logmessage=expdpcmd, loglevel='infoLogger').write_log()
            elif backup_type.lower() == 'byfull':
               expdptext = "expdp %s full=y directory=%s dumpfile=%s logfile=%s  parallel=%s cluster=n REUSE_DUMPFILES=Y"
               expdpcmd = TextHandler.format_text(
                   expdptext, backup_user, backup_name, dbconfig.oracle['instance'] +
                   '_expdp_' + datetime.datetime.now().strftime('%Y%m%d') + '.dmp',
                   dbconfig.oracle['instance'] + '_expdp_' +
                   datetime.datetime.now().strftime('%Y%m%d') + '.log', parallels)
               LogWrite(logmessage=expdpcmd, loglevel='infoLogger').write_log()
            else:
               LogWrite(
                   logmessage="Please asign the type to backup data.Like byuser|bytable|bytablespace|byfull.",
                   loglevel='warnLogger').write_log() 
        def imp(self):
            if recover_type.lower() == 'byuser':
                for (i,j) in zip(self.user_src, self.user_dst):
                    imptext = "imp %s fromuser=%s touser=%s file=%s log=%s"
                    impcmd = TextHandler.format_text(
                        imptext, self.backup_user, i, j, backup_dir + '/' + i + '_imp_' +
                        datetime.datetime.now().strftime('%Y%m%d') + '.dmp',
                        backup_dir + '/' + i + '_imp_' +
                        datetime.datetime.now().strftime('%Y%m%d') + '.log')
                    LogWrite(logmessage=impcmd, loglevel='infoLogger').write_log()
            elif recover_type.lower() == 'bytable':
                for (i,j) in zip(self.user_src,self.user_dst):
                    for k in self.table_src:
                        imptext = "imp %s fromuser=%s touser=%s table=%s file=%s log=%s"
                        impcmd = TextHandler.format_text(
                            imptext, self.backup_user, i, j, k, backup_dir + '/' + k + '_imp_' +
                            datetime.datetime.now().strftime('%Y%m%d') + '.dmp',
                            backup_dir + '/' + k + '_imp_' +
                            datetime.datetime.now().strftime('%Y%m%d') + '.log')
                        LogWrite(logmessage=impcmd, loglevel='infoLogger').write_log()
            elif recover_type.lower() == 'byfull':
                imptext = "imp %s full=y file=%s log=%s ignore=y"
                impcmd = TextHandler.format_text(
                    imptext, self.backup_user,
                    backup_dir + '/' + dbconfig.oracle['instance'] + '_imp_' +
                    datetime.datetime.now().strftime('%Y%m%d') + '.dmp',
                    backup_dir + '/' + dbconfig.oracle['instance'] + '_imp_' +
                    datetime.datetime.now().strftime('%Y%m%d') + '.log')
                LogWrite(logmessage=impcmd, loglevel='infoLogger').write_log()
            else:
                LogWrite(
                    logmessage="Please asign the type of import data.Like byuser|bytable|byfull.",
                    loglevel='warnLogger').write_log()
        def impdp(self):
            if recover_type.lower() == 'byuser':
                for (i,j) in zip(self.user_src,self.user_dst):
                    impdptext = "impdp %s remap_schemma=%s directory=%s dumpfile=%s logfile=%s  parallel=%s cluster=n REUSE_DUMPFILES=Y"
                    impdpcmd = TextHandler.format_text(
                       impdptext, backup_user, i+':'+j, self.backup_name, i + '_impdp_' +
                       datetime.datetime.now().strftime('%Y%m%d') + '.dmp',
                       i + '_impdp_' + datetime.datetime.now().strftime('%Y%m%d') +
                       '.log', self.parallels)
                    LogWrite(logmessage=impdpcmd, loglevel='infoLogger').write_log()
            elif recover_type.lower() == 'bytable':
                for (i ,j) in zip(self.user_src,self.user_dst): 
                    for (k,m) in zip(self.table_src,self.table_dst):
                        impdptext = "impdp %s tables=%s remap_schemma=%s directory=%s dumpfile=%s logfile=%s  parallel=%s cluster=n REUSE_DUMPFILES=Y"
                        impdpcmd = TextHandler.format_text(
                           impdptext, backup_user, i+'.'+k, i+':'+j, self.backup_name, k + '_impdp_' +
                           datetime.datetime.now().strftime('%Y%m%d') + '.dmp',
                           k + '_impdp_' + datetime.datetime.now().strftime('%Y%m%d') +
                           '.log', self.parallels)
                        LogWrite(logmessage=impdpcmd, loglevel='infoLogger').write_log()
            elif recover_type.lower() == 'bytablespace':
                for (i ,j) in zip(self.user_src,self.user_dst): 
                    for (k,m) in zip(self.table_src,self.table_dst):
                        impdptext = "impdp %s remap_schemma=%s remap_tablespace=%s directory=%s dumpfile=%s logfile=%s  parallel=%s cluster=n REUSE_DUMPFILES=Y"
                        impdpcmd = TextHandler.format_text(
                           impdptext, backup_user, i+':'+j, k+':'+m, self.backup_name, k + '_impdp_' +
                           datetime.datetime.now().strftime('%Y%m%d') + '.dmp',
                           k + '_impdp_' + datetime.datetime.now().strftime('%Y%m%d') +
                           '.log', self.parallels)
                        LogWrite(logmessage=impdpcmd, loglevel='infoLogger').write_log()
            elif recover_type.lower() == 'byfull':
                impdptext = "impdp %s full=y directory=%s dumpfile=%s logfile=%s  parallel=%s cluster=n REUSE_DUMPFILES=Y"
                impdpcmd = TextHandler.format_text(
                   impdptext, self.backup_user, self.backup_name, dbconfig.oracle['instance'] +
                   '_impdp_' + datetime.datetime.now().strftime('%Y%m%d') + '.dmp',
                   dbconfig.oracle['instance'] + '_impdp_' +
                   datetime.datetime.now().strftime('%Y%m%d') + '.log', parallels)
                LogWrite(logmessage=impdpcmd, loglevel='infoLogger').write_log()
            else:
                LogWrite(
                   logmessage="Please asign the type to import data.Like byuser|bytable|bytablespace|byfull.",
                   loglevel='warnLogger').write_log()
        result = {
            'exp': lambda:exp(),
            'expdp': lambda:expdp(),
            'imp': lambda:imp(),
            'impdp': lambda:impdp()
        }[self.action]()


class MySQL(DB):
    """docstring for MySQL"""
    pass
          

if __name__ == '__main__':
    #print(DataRecovery().query_scn())
    #print(Oracle.Tables().query_column('A_BM_XZQH','GZGS_GY'))
    print(Oracle.DataRecovery().exp())
    #print(Database.Sessions().active_session())
    #print(Oracle.Users().query_user())