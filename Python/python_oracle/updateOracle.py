import cx_Oracle
conn=cx_Oracle.connect('c##scott/tiger@orcl')
curs=conn.cursor()
sql="update emp set sal=9900 where ename='LOVE'"
curs.execute(sql)
