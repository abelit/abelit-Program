import dbconn

# Define function format_sql to replace the string for new sqltext
def format_text(text,*x):
	strings=text % (x)
	return strings

# Get cursor
def execute_sql(sql,isresult='true',column=0):
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

def exesql(sql):
	# Connect to oracle
	conn=dbconn.conn_oracle()
	curs=conn.cursor()
	curs.execute(sql)
	curs.execute('commit')
