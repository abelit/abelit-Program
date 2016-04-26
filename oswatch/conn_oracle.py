import cx_Oracle

conn=cx_Oracle.connect('sys','dba1d71f678513c02d0','172.28.1.25:1521/gzgszxk',cx_Oracle.SYSDBA)
cursor=conn.cursor()
cursor.execute("select username from all_users")
rows=cursor.fetchall()
print(rows)

cursor.close()
conn.close()

