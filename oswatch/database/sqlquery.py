from dbconn import DBConn as dbconn

# Define function format_sql to replace the string for new sqltext
class SQLQuery:
    """docstring for CoreDef"""
    def __init__(self, arg):
        super(CoreDef, self).__init__()
        self.arg = arg

    def format_text(text,*x):
        strings=text % (x)
        return strings

    # Get cursor
    def query_sql(sql,isresult='true',column=0):
        # Connect to oracle
        conn=dbconn.conn_oracle()

        curs=conn.cursor()
        curs.execute(sql)
        if isresult=='true':
            result=curs.fetchall()
            result_list=[]
            for row in result:
                result_list.append(row[column])
            return result_list
        curs.execute('commit')
        curs.close()
        conn.close()

    def execute_sql(sql):
        # Connect to oracle
        conn=dbconn.conn_oracle()
        curs=conn.cursor()
        curs.execute(sql)
        curs.execute('commit')
        curs.close()
        conn.close()
        
    def __init__(self, arg):
        super(SQL, self).__init__()
        self.arg = arg

    def users():
        pass

    def tables():
        pass

    def tablespaces():
        pass

    def datafiles():
        pass

    def olinelogs():
        pass

    def archivelogs():
        pass

    def sessions():
        pass

    def locks():
        pass